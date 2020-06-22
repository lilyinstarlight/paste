import datetime
import html
import logging
import os.path
import re
import string
import urllib.parse

import dateutil.tz

import fooster.web
import fooster.web.form
import fooster.web.page

import pygments
import pygments.lexers
import pygments.formatters

from paste import config, mime, paste


alias_regex = '(?P<alias>[a-zA-Z0-9._-]+)'

filename_safe = string.ascii_letters + string.digits + ' ()._-'

http = None

routes = {}
error_routes = {}


log = logging.getLogger('paste')


class Interface(fooster.web.form.FormMixIn, fooster.web.page.PageHandler):
    nonatomic = True

    directory = config.template
    page = 'index.html'
    message = ''

    def format(self, page):
        return page.format(message=self.message, languages=mime.languages)

    def do_post(self):
        try:
            alias = self.request.body['alias']
            name = self.request.body['name']
            language = self.request.body['language']
            code = self.request.body['code']
        except (KeyError, TypeError):
            raise fooster.web.HTTPError(400)

        if alias == '.' or alias == '..':
            raise fooster.web.HTTPError(400)

        try:
            if alias and not re.fullmatch(alias_regex, alias):
                raise NameError('alias ' + repr(alias) + ' invalid')

            alias = paste.put(alias, name, language, code)

            self.message = 'Successfully created at <a href="' + config.service.rstrip('/') + '/' + urllib.parse.quote(alias) + '">' + config.service.rstrip('/') + '/' + html.escape(alias) + '</a>.'
        except KeyError:
            self.message = 'This alias already exists. Wait until it expires or choose another.'
        except NameError:
            self.message = 'This alias is not valid. Choose one made up of alphanumeric characters only.'
        except RuntimeError:
            self.message = 'Could not create paste for some reason. Perhaps you should try again.'

        return self.do_get()


class ErrorInterface(fooster.web.page.PageErrorHandler):
    directory = config.template
    page = 'error.html'


class Paste(fooster.web.page.PageHandler):
    directory = config.template
    page = 'paste.html'

    def format(self, page):
        alias = self.groups['alias']

        if alias == '.' or alias == '..':
            raise fooster.web.HTTPError(400)

        try:
            if not re.fullmatch(alias_regex, alias):
                raise KeyError(alias)

            name, date, expire, language, code = paste.get(alias)
        except KeyError:
            raise fooster.web.HTTPError(404)

        date = datetime.datetime.strptime(date, '%a, %d %b %Y %H:%M:%S %Z').replace(tzinfo=datetime.timezone.utc).astimezone(dateutil.tz.gettz(config.timezone))
        expire = datetime.datetime.strptime(expire, '%a, %d %b %Y %H:%M:%S %Z').replace(tzinfo=datetime.timezone.utc).astimezone(dateutil.tz.gettz(config.timezone))

        try:
            if language.startswith('x-'):
                lexer = pygments.lexers.get_lexer_by_name(language.split('/', 1)[1])
            else:
                lexer = pygments.lexers.get_lexer_for_mimetype(language)

            formatter = pygments.formatters.HtmlFormatter(linenos=True)

            highlighted = pygments.highlight(code, lexer, formatter)
        except Exception:
            log.exception('Caught exception while highlighting "' + alias + '"')

            highlighted = html.escape(code)

        try:
            language_txt = mime.types[language]
        except KeyError:
            language_txt = 'Text'

        return page.format(pygments=pygments.formatters.HtmlFormatter().get_style_defs('.highlight'), name=html.escape(name), date=date.strftime(config.datetime_format), expire=expire.strftime(config.datetime_format), language=language_txt, code=highlighted, raw=urllib.parse.quote(self.request.resource) + '/raw')


class Raw(fooster.web.HTTPHandler):
    def do_get(self):
        alias = self.groups['alias']

        if alias == '.' or alias == '..':
            raise fooster.web.HTTPError(400)

        try:
            if not re.fullmatch(alias_regex, alias):
                raise KeyError(alias)

            name, date, expire, language, code = paste.get(alias)
        except KeyError:
            raise fooster.web.HTTPError(404)

        # add extension if necessary
        ext = os.path.splitext(name)[1]
        if ext not in mime.extmap or language not in mime.extmap[ext]:
            name += mime.extensions[language]

        # make sanitized filename
        filename = ''.join(char for char in os.path.basename(name) if char in filename_safe)
        if filename == '.' or filename == '..':
            filename = 'download.txt'

        # set headers
        self.response.headers['Content-Type'] = language
        self.response.headers['Content-Disposition'] = 'attachment; filename="' + filename + '"'
        self.response.headers['Last-Modified'] = date
        self.response.headers['Expires'] = expire

        # return data
        return 200, code


routes.update({'/': Interface, '/' + alias_regex: Paste, '/' + alias_regex + '/raw': Raw})
error_routes.update(fooster.web.page.new_error(handler=ErrorInterface))


def start():
    global http

    http = fooster.web.HTTPServer(config.addr, routes, error_routes)
    http.start()


def stop():
    global http

    http.stop()
    http = None


def join():
    global http

    http.join()
