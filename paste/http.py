import html
import mimetypes
import time
import urllib.parse

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
    directory = config.template
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

            self.message = 'Successfully created at <a href="' + config.service + '/' + urllib.parse.quote(alias) + '">' + config.service + '/' + html.ecsape(alias) + '</a>.'
        except KeyError:
            self.message = 'This alias already exists. Wait until it expires or choose another.'

        return self.do_get()


class ErrorInterface(web.page.PageErrorHandler):
    directory = config.template
    page = 'error.html'


class Paste(web.page.PageHandler):
    directory = config.template
    page = 'paste.html'

    def format(self, page):
        alias = self.groups[0]

        try:
            name, date, expire, language, code = paste.get(alias)
        except KeyError:
            raise web.HTTPError(404)

        try:
            lexer = pygments.lexers.get_lexer_for_mimetype(language, stripall=True)
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


class Raw(web.HTTPHandler):
    extensions = {
        # plain
        'text/plain': '.txt',

        # popular languages
        'text/x-python': '.py',
        'application/x-ruby': '.rb',
        'text/x-gosrc': '.go',
        'application/javascript': '.js',
        'text/x-java': '.java',
        'text/x-swift': '.swift',
        'text/x-csharp': '.cs',
        'text/x-csrc': '.c',
        'text/x-c++src': '.cpp',

        # programming languages
        'application/x-actionscript': '.as',
        'application/x-actionscript3': '.as',
        'text/x-arduino': '.ino',
        'text/coffeescript': '.coffee',
        'text/x-dsrc': '.d',
        'text/x-erlang': '.erl',
        'text/x-fortran': '.f',
        'text/x-glslsrc': '.glsl',
        'text/x-haskell': '.hs',
        'text/x-julia': '.jl',
        'text/x-common-lisp': '.lisp',
        'text/x-lua': '.lua',
        'text/matlab': '.m',
        'text/x-ocaml': '.ml',
        'text/x-objective-c': '.m',
        'application/x-php': '.php',
        'text/rust': '.rs',
        'text/x-scala': '.scala',
        'text/x-scheme': '.scm',
        'text/x-typescript': '.ts',
        'text/x-vala': '.vala',

        # low-level languages
        'text/x-gas': '.s',
        'text/x-nasm': '.asm',
        'text/x-windows-registry': '.reg',
        'text/x-vhdl': '.vhdl',
        'text/x-verilog': '.v',

        # markup languages
        'text/html': '.html',
        'text/css': '.css',
        'text/x-gnuplot': '.gpi',
        'application/json': '.json',
        'text/x-less-css': '.less',
        'application/postscript': '.ps',
        'text/x-sass': '.sass',
        'text/x-scss': '.scss',
        'text/x-tex': '.tex',
        'text/xml': '.xml',
        'text/x-yaml': '.yaml',

        # shell languages
        'application/x-fish': '.fish',
        'text/x-powershell': '.ps1',
        'application/x-sh': '.sh',

        # configuration languages
        'text/x-apacheconf': '.conf',
        'text/x-dockerfile-config': '.docker',
        'text/x-ini': '.ini',
        'text/x-nginx-conf': '.conf',
        'text/x-java-properties': '.properties',
        'text/x-vim': '.vim',

        # code building languages
        'text/x-cmake': '.cmake',
        'text/x-makefile': '.makefile',

        # other languages
        'text/x-diff': '.patch',
        'text/x-irclog': '.irc',
        'text/x-sql': '.sql',
    }

    def do_get(self):
        alias = self.groups[0]

        try:
            name, date, expire, language, code = paste.get(alias)
        except KeyError:
            raise web.HTTPError(404)

        # add extension if necessary
        if mimetypes.guess_type(name)[0] != language:
            try:
                name += self.extensions[language]
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
error_routes.update(web.page.new_error(handler=ErrorInterface))


def start():
    global http

    http = web.HTTPServer(config.addr, routes, error_routes, log=log.httplog)
    http.start()


def stop():
    global http

    http.stop()
    http = None
