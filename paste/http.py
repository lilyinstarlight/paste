import html
import mimetypes
import time
import urllib.parse

import fooster.web, fooster.web.form, fooster.web.page

import pygments
import pygments.lexers
import pygments.formatters

from paste import config, mime, paste


alias = '([a-zA-Z0-9._-]+)'

http = None

routes = {}
error_routes = {}


class Interface(fooster.web.page.PageHandler, fooster.web.form.FormHandler):
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

        try:
            alias = paste.put(alias, name, language, code)

            self.message = 'Successfully created at <a href="' + config.service + '/' + urllib.parse.quote(alias) + '">' + config.service + '/' + html.escape(alias) + '</a>.'
        except KeyError:
            self.message = 'This alias already exists. Wait until it expires or choose another.'

        return self.do_get()


class ErrorInterface(fooster.web.page.PageErrorHandler):
    directory = config.template
    page = 'error.html'


class Paste(fooster.web.page.PageHandler):
    directory = config.template
    page = 'paste.html'

    def format(self, page):
        alias = self.groups[0]

        try:
            name, date, expire, language, code = paste.get(alias)
        except KeyError:
            raise fooster.web.HTTPError(404)

        try:
            if language.startswith('x-'):
                lexer = pygments.lexers.get_lexer_by_name(language.split('/', 1)[1])
            else:
                lexer = pygments.lexers.get_lexer_for_mimetype(language)

            formatter = pygments.formatters.HtmlFormatter(linenos=True)

            highlighted = pygments.highlight(code, lexer, formatter)
        except:
            log.pastelog.exception()

            highlighted = html.escape(code)

        try:
            language_txt = mime.types[language]
        except KeyError:
            language_txt = 'Text'

        return page.format(pygments=pygments.formatters.HtmlFormatter().get_style_defs('.highlight'), name=html.escape(name), date=date, expire=expire, language=language_txt, code=highlighted, raw=urllib.parse.quote(self.request.resource) + '/raw')


class Raw(fooster.web.HTTPHandler):
    def do_get(self):
        alias = self.groups[0]

        try:
            name, date, expire, language, code = paste.get(alias)
        except KeyError:
            raise fooster.web.HTTPError(404)

        # add extension if necessary
        if mimetypes.guess_type(name)[0] != language:
            try:
                name += mime.extensions[language]
            except KeyError:
                pass

        # set headers
        self.response.headers['Content-Type'] = language
        self.response.headers['Content-Disposition'] = 'attachment; filename="' + name + '"'
        self.response.headers['Last-Modified'] = date
        self.response.headers['Expires'] = expire

        # return data
        return 200, code

routes.update({'/': Interface, '/' + alias: Paste, '/' + alias + '/raw': Raw})
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
