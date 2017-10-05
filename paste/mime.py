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

    ('application/x-actinoscript', '.as', 'ActionScript'),
    ('application/x-actionscript3', '.as', 'ActionScript3'),
    ('text/x-ada', '.adb', 'Ada'),
    ('text/x-arduino', '.ino', 'Arduino'),
    ('text/x-boo', '.boo', 'Boo'),
    ('text/x-csrc', '.c', 'C'),
    ('text/x-csharp', '.cs', 'C#'),
    ('text/x-c++src', '.cpp', 'C++'),
    ('text/coffeescript', '.coffee', 'CoffeeScript'),
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
    ('text/x-common-lisp', '.cl', 'Lisp'),
    ('text/x-lua', '.lua', 'Lua'),
    ('text/matlab', '.m', 'Matlab'),
    ('text/x-ocaml', '.ml', 'OCaml'),
    ('text/x-objective-c', '.m', 'Objective-C'),
    ('application/x-php', '.php', 'PHP'),
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
    ('text/x-vbnet', '.vb', 'Visual Basic.NET'),

    ('heading', '', 'Low-Level Languages'),

    ('text/x-gas', '.s', 'ASM'),
    ('x-text/hexdump', '.hex', 'Hexdump'),
    ('text/x-llvm', '.ll', 'LLVM'),
    ('text/x-nasm', '.asm', 'NASM'),
    ('text/x-nasm-objdump', '.objdump-intel', 'NASM Objdump'),
    ('text/x-vhdl', '.vhdl', 'VHDL'),
    ('text/x-verilog', '.v', 'Verilog'),

    ('heading', '', 'Markup Languages'),

    ('text/x-bbcode', '.txt', 'BBCode'),
    ('text/css', '.css', 'CSS'),
    ('text/x-gnuplot', '.plot', 'Gnuplot'),
    ('text/html', '.html', 'HTML'),
    ('application/json', '.json', 'JSON'),
    ('text/x-less-css', '.less', 'Less'),
    ('text/x-markdown', '.md', 'Markdown'),
    ('application/postscript', '.ps', 'Postscript'),
    ('application/x-qml', '.qml', 'QML'),
    ('text/x-rst', '.rst', 'reStructuredText'),
    ('text/x-sass', '.sass', 'Sass'),
    ('text/x-scss', '.scss', 'SCSS'),
    ('text/x-tex', '.tex', 'TeX'),
    ('application/x-troff', '.man', 'Troff'),
    ('text/x-trac-wiki', '.wiki', 'Wiki'),
    ('text/xml', '.xml', 'XML'),
    ('text/x-yaml', '.yaml', 'YAML'),

    ('heading', '', 'Templating Languages'),

    ('x-text/html+ng2', '.ng2', 'Angular'),
    ('text/html+django', '.html', 'Django'),
    ('application/x-ruby-templating', '.erb', 'ERB'),
    ('text/html+handlebars', '.handlebars', 'Handlebars'),

    ('heading', '', 'Shell Languages'),

    ('application/x-awk', '.awk', 'Awk'),
    ('application/x-fish', '.fish', 'Fish'),
    ('text/x-powershell', '.ps1', 'PowerShell'),
    ('application/x-sh', '.sh', 'Bash'),
    ('application/x-sh', '.tcsh', 'tcsh'),

    ('heading', '', 'Configuration Languages'),

    ('text/x-apacheconf', '.conf', 'Apache'),
    ('text/x-dockerfile-config', '.docker', 'Docker'),
    ('text/x-ini', '.ini', 'INI'),
    ('text/x-kconfig', '', 'Kconfig'),
    ('text/x-nginx-conf', '.conf', 'Nginx'),
    ('x-text/pkgconfig', '.pc', 'pkg-config'),
    ('text/x-java-properties', '.properties', 'Properties'),
    ('text/x-windows-registry', '.reg', 'Registry'),
    ('text/x-vim', '.vim', 'Vim'),

    ('heading', '', 'Automation Languages'),

    ('x-text/applescript', '.applescript', 'AppleScript'),
    ('text/x-autohotkey', '.ahk', 'AutoHotkey'),
    ('text/x-autoit', '.au3', 'AutoIt'),

    ('heading', '', 'Code Building Languages'),

    ('text/x-cmake', '.cmake', 'CMake'),
    ('text/x-makefile', '.mk', 'Makefile'),

    ('heading', '', 'Packaging Languages'),

    ('x-text/debcontrol', '', 'Debian Control'),
    ('text/x-nix', '.nix', 'Nix'),
    ('text/x-nsis', '.nsi', 'NSIS'),
    ('text/x-rpm-spec', '.spec', 'RPMSpec'),

    ('heading', '', 'Specification Languages'),

    ('text/x-bnf', '.bnf', 'BNF'),
    ('application/xml-dtd', '.dtd', 'DTD'),
    ('text/x-ebnf', '.ebnf', 'EBNF'),
    ('x-text/protobuf', '.proto', 'ProtoBuf'),
    ('x-text/puppet', '.pp', 'Puppet'),

    ('heading', '', 'Esoteric Languages'),

    ('application/x-befunge', '.befunge', 'Befunge'),
    ('application/x-brainfuck', '.bf', 'BrainFuck'),

    ('heading', '', 'Other Languages'),

    ('text/x-bibtex', '.bib', 'BibTeX'),
    ('x-text/bro', '.bro', 'Bro'),
    ('text/x-cobol', '.cob', 'COBOL'),
    ('text/x-cuda', '.cu', 'CUDA'),
    ('text/x-diff', '.diff', 'Diff'),
    ('application/x-forth', '.frt', 'Forth'),
    ('text/x-irclog', '.txt', 'IRC'),
    ('application/mathematica', '.nb', 'Mathematica'),
    ('text/x-mysql', '.sql', 'MySQL'),
    ('text/x-postgresql', '.sql', 'PostgreSQL'),
    ('text/swig', '.swig', 'SWIG'),
]

types = {entry[0]: entry[2] for entry in supported if entry[0] != 'heading'}
extensions = {entry[0]: entry[1] for entry in supported if entry[0] != 'heading'}

languages = '\n'.join('<option value={}>{}</option>'.format(entry[0], entry[2]) if entry[0] != 'heading' else '<option disabled>──────────</option>\n<option disabled>{}</option>'.format(entry[2]) for entry in supported)
