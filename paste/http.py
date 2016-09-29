import os
import time

import web, web.form, web.page

import pygments
import pygments.lexers
import pygments.formatters

from paste import config, log, mime, paste


alias = '([a-zA-Z0-9._-]+)'

http = None

routes = {}
error_routes = {}


class Interface(web.page.PageHandler, web.form.FormHandler):
    directory = os.path.dirname(__file__) + '/html'
    page = 'index.html'
    message = ''

    def format(self, page):
        return page.format(message=self.message)

    def do_post(self):
        try:
            alias = self.request.body['alias']
            name = self.request.body['name']
            language = self.request.body['language']
            code = self.request.body['code']
        except (KeyError, TypeError):
            raise web.HTTPError(400)

        try:
            alias = paste.put(alias, name, language, code)

            self.message = 'Successfully created at <a href="' + config.service + '/' + alias + '">' + config.service + '/' + alias + '</a>.'
        except KeyError:
            self.message = 'This alias already exists. Wait until it expires or choose another.'

        return self.do_get()


class ErrorInterface(web.page.PageErrorHandler):
    directory = os.path.dirname(__file__) + '/html'
    page = 'error.html'


class Paste(web.page.PageHandler):
    directory = os.path.dirname(__file__) + '/html'
    page = 'paste.html'

    def format(self, page):
        alias = self.groups[0]

        try:
            name, date, language, code = paste.get(alias)
        except KeyError:
            raise web.HTTPError(404)

        try:
            lexer = pygments.lexers.get_lexer_for_mimetype(language, stripall=True)
            formatter = pygments.formatters.HtmlFormatter(linenos=True)

            highlighted = pygments.highlight(code, lexer, formatter)
        except:
            log.pastelog.exception()

            highlighted = code

        try:
            language_txt = mime.types[language]
        except KeyError:
            language_txt = 'Text'

        return page.format(pygments=pygments.formatters.HtmlFormatter().get_style_defs('.highlight'), name=name, date=date, language=language_txt, code=highlighted)

routes.update({'/': Interface, '/' + alias: Paste})
error_routes.update(web.page.new_error(handler=ErrorInterface))


def start():
    global http

    http = web.HTTPServer(config.addr, routes, error_routes, log=log.httplog)
    http.start()


def stop():
    global http

    http.stop()
    http = None
