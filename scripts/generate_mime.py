#!/usr/bin/env python3

# This script generates a language list for the interface. The code is atrocious
# and slow but I probably won't fix it until I decide to rewrite things again for
# some reason.
#
# Run like below to generate the supported language list. This sorts and formats by
# the "supported" list below and just tacks on anything else Pygments supports
# because why not.
#
# $ ./generate_mime.py >mime.py
#
# Warnings should be address as follows then the above script rerun:
#   Name change:
#     Options:
#     * Change the name in the "supported" list below to the new Pygments name.
#     * Add the desired name in "moves" dictionary as "PygmentsName": "DesiredName".
#
#   Duplicate {MIME,name}:
#     Resolve the conflict either by adjusting one of the names to better describe
#     the language or removing an obsolete entry. Entries under a heading of
#     "Popular" if it is the first one encountered will be ignored as duplicates.
#
# Languages under the "Other" heading in the output should be reviewed for whether
# they should be sorted into a section or a new section created in the "supported"
# list below. Languages under the "Other" heading should __not__ be added to the
# "supported" list below unless they are put into another section before it.
#
# After manual review, copy the new "mime.py" to the "paste" package and push.

import sys

from pygments.lexers import get_all_lexers, get_lexer_by_name, get_lexer_for_mimetype
from pygments.util import ClassNotFound


supported = [
    ('text/plain', '.txt', 'Text'),

    ('heading', '', 'Popular Languages'),

    ('text/x-python', '.py', 'Python'),
    ('application/x-ruby', '.rb', 'Ruby'),
    ('text/x-gosrc', '.go', 'Go'),
    ('text/x-swift', '.swift', 'Swift'),
    ('text/x-csrc', '.c', 'C'),
    ('text/x-csharp', '.cs', 'C#'),
    ('text/x-c++src', '.cpp', 'C++'),
    ('text/x-java', '.java', 'Java'),
    ('text/html', '.html', 'HTML'),
    ('text/css', '.css', 'CSS'),
    ('application/javascript', '.js', 'JavaScript'),
    ('application/json', '.json', 'JSON'),
    ('text/x-markdown', '.md', 'Markdown'),

    ('heading', '', 'Programming Languages'),

    ('application/x-actionscript3', '.as', 'ActionScript 3'),
    ('text/x-ada', '.adb', 'Ada'),
    ('text/x-arduino', '.ino', 'Arduino'),
    ('text/x-boo', '.boo', 'Boo'),
    ('text/x-csrc', '.c', 'C'),
    ('text/x-csharp', '.cs', 'C#'),
    ('text/x-c++src', '.cpp', 'C++'),
    ('text/coffeescript', '.coffee', 'CoffeeScript'),
    ('text/x-common-lisp', '.cl', 'Common Lisp'),
    ('text/x-crystal', '.cr', 'Crystal'),
    ('text/x-dsrc', '.d', 'D'),
    ('text/x-dart', '.dart', 'Dart'),
    ('text/x-pascal', '.pas', 'Delphi'),
    ('text/x-erlang', '.erl', 'Erlang'),
    ('text/x-fortran', '.f', 'Fortran'),
    ('text/x-glslsrc', '.glsl', 'GLSL'),
    ('text/x-gosrc', '.go', 'Go'),
    ('text/x-haskell', '.hs', 'Haskell'),
    ('text/x-java', '.java', 'Java'),
    ('application/javascript', '.js', 'JavaScript'),
    ('text/x-julia', '.jl', 'Julia'),
    ('text/x-kotlin', '.kt', 'Kotlin'),
    ('text/x-lua', '.lua', 'Lua'),
    ('text/matlab', '.m', 'Matlab'),
    ('text/x-ocaml', '.ml', 'OCaml'),
    ('text/x-objective-c', '.m', 'Objective-C'),
    ('text/x-perl', '.pl', 'Perl'),
    ('application/x-php', '.php', 'HTML+PHP'),
    ('text/x-prolog', '.ecl', 'Prolog'),
    ('text/x-python', '.py', 'Python'),
    ('text/basic', '.bas', 'QBasic'),
    ('application/x-ruby', '.rb', 'Ruby'),
    ('text/rust', '.rs', 'Rust'),
    ('text/x-scala', '.scala', 'Scala'),
    ('text/x-scheme', '.scm', 'Scheme'),
    ('text/x-swift', '.swift', 'Swift'),
    ('text/x-typescript', '.ts', 'TypeScript'),
    ('text/x-vala', '.vala', 'Vala'),
    ('text/x-vbnet', '.vb', 'VB.NET'),

    ('heading', '', 'Low-Level Languages'),

    ('text/x-gas', '.s', 'GAS'),
    ('x-pygments/hexdump', '.hex', 'Hexdump'),
    ('text/x-llvm', '.ll', 'LLVM'),
    ('text/x-nasm', '.asm', 'NASM'),
    ('text/x-nasm-objdump', '.objdump-intel', 'NASM Objdump'),
    ('text/x-vhdl', '.vhdl', 'VHDL'),
    ('text/x-verilog', '.v', 'Verilog'),

    ('heading', '', 'Markup Languages'),

    ('text/x-bbcode', '.txt', 'BBCode'),
    ('text/css', '.css', 'CSS'),
    ('text/x-gnuplot', '.plot', 'Gnuplot'),
    ('application/x-troff', '.man', 'Groff'),
    ('text/html', '.html', 'HTML'),
    ('application/json', '.json', 'JSON'),
    ('text/x-less-css', '.less', 'Less'),
    ('text/x-markdown', '.md', 'Markdown'),
    ('application/postscript', '.ps', 'PostScript'),
    ('application/x-qml', '.qml', 'QML'),
    ('text/x-rst', '.rst', 'reStructuredText'),
    ('text/x-sass', '.sass', 'Sass'),
    ('text/x-scss', '.scss', 'SCSS'),
    ('x-pygments/scdoc', '.scd', 'scdoc'),
    ('text/x-tex', '.tex', 'TeX'),
    ('x-pygments/toml', '.toml', 'TOML'),
    ('text/x-trac-wiki', '.wiki', 'Trac Wiki'),
    ('text/xml', '.xml', 'XML'),
    ('text/x-yaml', '.yaml', 'YAML'),

    ('heading', '', 'Templating Languages'),

    ('x-pygments/html+ng2', '.ng2', 'HTML+Angular2'),
    ('text/html+django', '.html', 'HTML+Django/Jinja'),
    ('application/x-ruby-templating', '.erb', 'ERB'),
    ('text/html+handlebars', '.handlebars', 'HTML+Handlebars'),

    ('heading', '', 'Shell Languages'),

    ('application/x-awk', '.awk', 'Awk'),
    ('application/x-fish', '.fish', 'Fish'),
    ('text/x-powershell', '.ps1', 'PowerShell'),
    ('application/x-sh', '.sh', 'Bash'),
    ('application/x-csh', '.tcsh', 'tcsh'),
    ('application/x-dos-batch', '.bat', 'Batchfile'),

    ('heading', '', 'Configuration Languages'),

    ('text/x-apacheconf', '.conf', 'Apache'),
    ('text/x-dockerfile-config', '.docker', 'Docker'),
    ('text/x-ini', '.ini', 'INI'),
    ('text/x-kconfig', '', 'Kconfig'),
    ('text/x-nginx-conf', '.conf', 'Nginx'),
    ('x-pygments/pkgconfig', '.pc', 'PkgConfig'),
    ('text/x-java-properties', '.properties', 'Properties'),
    ('text/x-windows-registry', '.reg', 'Windows Registry'),
    ('text/x-vim', '.vim', 'Vim'),
    ('text/x-elisp', '.el', 'EmacsLisp'),

    ('heading', '', 'Automation Languages'),

    ('x-pygments/applescript', '.applescript', 'AppleScript'),
    ('text/x-autohotkey', '.ahk', 'AutoHotkey'),
    ('text/x-autoit', '.au3', 'AutoIt'),

    ('heading', '', 'Code Building Languages'),

    ('text/x-cmake', '.cmake', 'CMake'),
    ('text/x-makefile', '.mk', 'Makefile'),

    ('heading', '', 'Packaging Languages'),

    ('x-pygments/debcontrol', '', 'Debian Control'),
    ('text/x-nix', '.nix', 'Nix'),
    ('text/x-nsis', '.nsi', 'NSIS'),
    ('text/x-rpm-spec', '.spec', 'RPMSpec'),

    ('heading', '', 'Specification Languages'),

    ('text/x-bibtex', '.bib', 'BibTeX'),
    ('text/x-bnf', '.bnf', 'BNF'),
    ('application/xml-dtd', '.dtd', 'DTD'),
    ('text/x-ebnf', '.ebnf', 'EBNF'),
    ('x-pygments/protobuf', '.proto', 'Protocol Buffer'),
    ('x-pygments/puppet', '.pp', 'Puppet'),

    ('heading', '', 'Esoteric Languages'),

    ('application/x-befunge', '.befunge', 'Befunge'),
    ('application/x-brainfuck', '.bf', 'Brainfuck'),

    ('heading', '', 'Domain-Specific Languages'),

    ('x-pygments/zeek', '.zeek', 'Zeek'),
    ('text/x-cuda', '.cu', 'CUDA'),
    ('text/x-diff', '.diff', 'Diff'),
    ('text/x-irclog', '.txt', 'IRC Logs'),
    ('application/mathematica', '.nb', 'Mathematica'),
    ('text/x-mysql', '.sql', 'MySQL'),
    ('text/x-postgresql', '.sql', 'PostgreSQL'),
    ('text/swig', '.swig', 'SWIG'),

    ('heading', '', 'Protocol Languages'),

    ('message/rfc822', '.eml', 'Email'),
    ('x-pygments/http', '.http', 'HTTP'),
    ('multipart/mixed', '.mime', 'MIME'),

    ('heading', '', 'Other Languages'),
]


moves = {
    'Text only': 'Text',
    'markdown': 'Markdown',
    'VB.net': 'VB.NET',
    'objdump-nasm': 'NASM Objdump',
    'vhdl': 'VHDL',
    'verilog': 'Verilog',
    'LessCss': 'Less',
    'markdown': 'Markdown',
    'MoinMoin/Trac Wiki markup': 'Trac Wiki',
    'HTML + Angular2': 'HTML+Angular2',
    'Tcsh': 'tcsh',
    'ApacheConf': 'Apache',
    'Nginx configuration file': 'Nginx',
    'reg': 'Windows Registry',
    'VimL': 'Vim',
    'autohotkey': 'AutoHotkey',
    'Debian Control file': 'Debian Control',
    'IRC logs': 'IRC Logs',
    'PostgreSQL SQL dialect': 'PostgreSQL',
    'E-mail': 'Email',
}


def check(list, idx, val):
    for list_idx, entry in enumerate(list):
        if entry[idx] == val:
            return list_idx

    return -1


last = None

def print_warning(heading, message):
    global last

    if not last or last != heading:
        if last:
            print(file=sys.stderr)

        print('Warn: ' + heading, file=sys.stderr)
        print('======' + '='*len(heading), file=sys.stderr)

        last = heading

    print(message, file=sys.stderr)


generated = supported.copy()

for language in supported:
    mime, extension, name = language

    if mime == 'heading':
        continue

    try:
        if mime.startswith('x-'):
            lexer = get_lexer_by_name(mime.split('/', 1)[1])
        else:
            lexer = get_lexer_for_mimetype(mime)
    except ClassNotFound:
        generated.remove(language)

    if name != moves.get(lexer.name, lexer.name):
        print_warning('Name change', '{} -> {} (Current -> Pygments)'.format(repr(name), repr(lexer.name)))

for name, short, filename, mime in get_all_lexers():
    if not short:
        short = (name.lower(),)

    filename = tuple(f[1:] for f in filename if f[:2] == '*.')

    if not filename:
        filename = ('',)

    if not mime:
        mime = tuple('x-pygments/' + s for s in short)

    if any(check(supported, 0, m) >= 0 for m in mime):
        continue

    generated.append((mime[0], filename[0], name))

full_idx = -1

for idx, language in enumerate(generated):
    if language[0] == 'heading':
        if full_idx < 0 and not language[2].lower().startswith('popular'):
            full_idx = idx

        continue

    mime_idx = check(generated, 0, language[0])
    if mime_idx >= full_idx and mime_idx != idx:
        print_warning('Duplicate entry', 'Same MIME:\n{} - {}\n{} - {}'.format(idx, repr(language), mime_idx, repr(generated[mime_idx])))

    name_idx = check(generated, 2, language[2])
    if name_idx >= full_idx and name_idx != idx:
        print_warning('Duplicate entry', 'Same name:\n{} - {}\n{} - {}'.format(idx, repr(language), name_idx, repr(generated[name_idx])))

if language[2].lower().startswith('other'):
    generated.pop()


print(r'''# generated by scripts/generate_mime.py
import html

supported = [''')
for language in generated:
    if language[0] == 'heading':
        print()

    print('    {},'.format(repr(language)))

    if language[0] == 'heading':
        print()
print(r''']

types = {entry[0]: entry[2] for entry in supported if entry[0] != 'heading'}
extensions = {entry[0]: entry[1] for entry in supported if entry[0] != 'heading'}

languages = '\n'.join('<option value="{}">{}</option>'.format(entry[0], html.escape(entry[2])) if entry[0] != 'heading' else '<option disabled>──────────</option>\n<option disabled>{}</option>'.format(html.escape(entry[2])) for entry in supported)''')
