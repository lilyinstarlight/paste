# generated by scripts/generate_mime.py
import html

supported = [
    ('text/plain', '.txt', 'Text'),

    ('heading', '', 'Popular Languages'),

    ('text/rust', '.rs', 'Rust'),
    ('text/x-nix', '.nix', 'Nix'),
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
    ('x-pygments/lilypond', '.ly', 'LilyPond'),
    ('text/x-markdown', '.md', 'Markdown'),
    ('application/postscript', '.ps', 'PostScript'),
    ('application/x-qml', '.qml', 'QML'),
    ('text/x-rst', '.rst', 'reStructuredText'),
    ('text/x-sass', '.sass', 'Sass'),
    ('text/x-scss', '.scss', 'SCSS'),
    ('x-pygments/scdoc', '.scd', 'scdoc'),
    ('text/x-tex', '.tex', 'TeX'),
    ('application/toml', '.toml', 'TOML'),
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

    ('text/x-cuda', '.cu', 'CUDA'),
    ('text/x-diff', '.diff', 'Diff'),
    ('application/mathematica', '.nb', 'Mathematica'),
    ('text/x-mysql', '.sql', 'MySQL'),
    ('text/x-postgresql', '.sql', 'PostgreSQL'),
    ('text/swig', '.swig', 'SWIG'),
    ('x-pygments/zeek', '.zeek', 'Zeek'),

    ('heading', '', 'Protocol Languages'),

    ('message/rfc822', '.eml', 'Email'),
    ('x-pygments/http', '.http', 'HTTP'),
    ('multipart/mixed', '.mime', 'MIME'),

    ('heading', '', 'Logs'),

    ('text/x-irclog', '.txt', 'IRC Logs'),
    ('x-pygments/kmsg', '.kmsg', 'Kernel Log'),

    ('heading', '', 'Other Languages'),

    ('text/x-abap', '.abap', 'ABAP'),
    ('x-pygments/amdgpu', '.isa', 'AMDGPU'),
    ('x-pygments/apl', '.apl', 'APL'),
    ('text/x-abnf', '.abnf', 'ABNF'),
    ('application/x-actionscript', '.as', 'ActionScript'),
    ('x-pygments/adl', '.adl', 'ADL'),
    ('text/x-agda', '.agda', 'Agda'),
    ('x-pygments/aheui', '.aheui', 'Aheui'),
    ('text/x-alloy', '.als', 'Alloy'),
    ('text/x-ambienttalk', '.at', 'AmbientTalk'),
    ('x-pygments/ampl', '.run', 'Ampl'),
    ('x-pygments/ng2', '', 'Angular2'),
    ('x-pygments/antlr-actionscript', '.G', 'ANTLR With ActionScript Target'),
    ('x-pygments/antlr-csharp', '.G', 'ANTLR With C# Target'),
    ('x-pygments/antlr-cpp', '.G', 'ANTLR With CPP Target'),
    ('x-pygments/antlr-java', '.G', 'ANTLR With Java Target'),
    ('x-pygments/antlr', '', 'ANTLR'),
    ('x-pygments/antlr-objc', '.G', 'ANTLR With ObjectiveC Target'),
    ('x-pygments/antlr-perl', '.G', 'ANTLR With Perl Target'),
    ('x-pygments/antlr-python', '.G', 'ANTLR With Python Target'),
    ('x-pygments/antlr-ruby', '.G', 'ANTLR With Ruby Target'),
    ('x-pygments/arrow', '.arw', 'Arrow'),
    ('x-pygments/arturo', '.art', 'Arturo'),
    ('application/pgp-keys', '.asc', 'ASCII armored'),
    ('x-pygments/asn1', '.asn1', 'ASN.1'),
    ('text/x-aspectj', '.aj', 'AspectJ'),
    ('text/x-asymptote', '.asy', 'Asymptote'),
    ('x-pygments/augeas', '.aug', 'Augeas'),
    ('x-pygments/bbcbasic', '.bbc', 'BBC Basic'),
    ('x-pygments/bc', '.bc', 'BC'),
    ('x-pygments/bqn', '.bqn', 'BQN'),
    ('x-pygments/bst', '.bst', 'BST'),
    ('x-pygments/bare', '.bare', 'BARE'),
    ('x-pygments/basemake', '', 'Base Makefile'),
    ('application/x-shell-session', '.sh-session', 'Bash Session'),
    ('text/x-bdd', '.feature', 'Bdd'),
    ('text/x-berry', '.be', 'Berry'),
    ('text/x-bb', '.bb', 'BlitzBasic'),
    ('text/x-bmx', '.bmx', 'BlitzMax'),
    ('text/x-blueprint', '.blp', 'Blueprint'),
    ('x-pygments/boa', '.boa', 'Boa'),
    ('x-pygments/boogie', '.bpl', 'Boogie'),
    ('x-pygments/bugs', '.bug', 'BUGS'),
    ('x-pygments/camkes', '.camkes', 'CAmkES'),
    ('text/x-c-objdump', '.c-objdump', 'c-objdump'),
    ('x-pygments/cpsa', '.cpsa', 'CPSA'),
    ('x-pygments/css+ul4', '.cssul4', 'CSS+UL4'),
    ('x-pygments/aspx-cs', '.aspx', 'aspx-cs'),
    ('x-pygments/ca65', '.s', 'ca65 assembler'),
    ('x-pygments/cadl', '.cadl', 'cADL'),
    ('x-pygments/capdl', '.cdl', 'CapDL'),
    ('x-pygments/capnp', '.capnp', "Cap'n Proto"),
    ('text/x-carbon', '.carbon', 'Carbon'),
    ('x-pygments/cbmbas', '.bas', 'CBM BASIC V2'),
    ('text/x-cddl', '.cddl', 'CDDL'),
    ('text/x-ceylon', '.ceylon', 'Ceylon'),
    ('x-pygments/cfengine3', '.cf', 'CFEngine3'),
    ('text/x-chaiscript', '.chai', 'ChaiScript'),
    ('x-pygments/chapel', '.chpl', 'Chapel'),
    ('x-pygments/charmci', '.ci', 'Charmci'),
    ('text/html+cheetah', '', 'HTML+Cheetah'),
    ('application/x-javascript+cheetah', '', 'JavaScript+Cheetah'),
    ('application/x-cheetah', '.tmpl', 'Cheetah'),
    ('application/xml+cheetah', '', 'XML+Cheetah'),
    ('text/x-cirru', '.cirru', 'Cirru'),
    ('text/x-clay', '.clay', 'Clay'),
    ('x-pygments/clean', '.icl', 'Clean'),
    ('text/x-clojure', '.clj', 'Clojure'),
    ('text/x-clojurescript', '.cljs', 'ClojureScript'),
    ('x-pygments/cobolfree', '.cbl', 'COBOLFree'),
    ('text/x-cobol', '.cob', 'COBOL'),
    ('x-pygments/cfc', '.cfc', 'Coldfusion CFC'),
    ('application/x-coldfusion', '.cfm', 'Coldfusion HTML'),
    ('x-pygments/cfs', '', 'cfstatement'),
    ('x-pygments/comal', '.cml', 'COMAL-80'),
    ('text/x-component-pascal', '.cp', 'Component Pascal'),
    ('text/x-coq', '.v', 'Coq'),
    ('text/x-cplint', '.ecl', 'cplint'),
    ('text/x-cpp-objdump', '.cpp-objdump', 'cpp-objdump'),
    ('x-pygments/crmsh', '.crmsh', 'Crmsh'),
    ('text/x-crocsrc', '.croc', 'Croc'),
    ('text/x-cryptol', '.cry', 'Cryptol'),
    ('x-pygments/csound-document', '.csd', 'Csound Document'),
    ('x-pygments/csound', '.orc', 'Csound Orchestra'),
    ('x-pygments/csound-score', '.sco', 'Csound Score'),
    ('text/css+django', '.css.j2', 'CSS+Django/Jinja'),
    ('text/css+ruby', '', 'CSS+Ruby'),
    ('text/css+genshi', '', 'CSS+Genshi Text'),
    ('text/css+php', '', 'CSS+PHP'),
    ('text/css+smarty', '', 'CSS+Smarty'),
    ('x-pygments/cypher', '.cyp', 'Cypher'),
    ('text/x-cython', '.pyx', 'Cython'),
    ('text/x-d-objdump', '.d-objdump', 'd-objdump'),
    ('x-pygments/dpatch', '.dpatch', 'Darcs Patch'),
    ('text/x-dasm16', '.dasm16', 'DASM16'),
    ('x-pygments/dax', '.dax', 'Dax'),
    ('x-pygments/desktop', '.desktop', 'Desktop file'),
    ('text/x-c', '.dts', 'Devicetree'),
    ('text/x-dg', '.dg', 'dg'),
    ('application/x-django-templating', '', 'Django/Jinja'),
    ('text/dns', '.zone', 'Zone'),
    ('text/x-duel', '.duel', 'Duel'),
    ('text/x-dylan-console', '.dylan-console', 'Dylan session'),
    ('text/x-dylan', '.dylan', 'Dylan'),
    ('text/x-dylan-lid', '.lid', 'DylanLID'),
    ('application/x-ecl', '.ecl', 'ECL'),
    ('text/x-echdr', '.ec', 'eC'),
    ('text/x-earl-grey', '.eg', 'Earl Grey'),
    ('text/x-easytrieve', '.ezt', 'Easytrieve'),
    ('text/x-eiffel', '.e', 'Eiffel'),
    ('text/x-elixir-shellsession', '', 'Elixir iex session'),
    ('text/x-elixir', '.ex', 'Elixir'),
    ('text/x-elm', '.elm', 'Elm'),
    ('text/x-elpi', '.elpi', 'Elpi'),
    ('text/x-erl-shellsession', '.erl-sh', 'Erlang erl session'),
    ('text/html+evoque', '.html', 'HTML+Evoque'),
    ('application/x-evoque', '.evoque', 'Evoque'),
    ('application/xml+evoque', '.xml', 'XML+Evoque'),
    ('x-pygments/execline', '.exec', 'execline'),
    ('text/x-ezhil', '.n', 'Ezhil'),
    ('text/x-fsharp', '.fs', 'F#'),
    ('text/x-fstar', '.fst', 'FStar'),
    ('text/x-factor', '.factor', 'Factor'),
    ('text/x-fancysrc', '.fy', 'Fancy'),
    ('application/x-fantom', '.fan', 'Fantom'),
    ('text/x-felix', '.flx', 'Felix'),
    ('x-pygments/fennel', '.fnl', 'Fennel'),
    ('x-pygments/fift', '.fif', 'Fift'),
    ('text/x-flatline', '', 'Flatline'),
    ('x-pygments/floscript', '.flo', 'FloScript'),
    ('application/x-forth', '.frt', 'Forth'),
    ('x-pygments/fortranfixed', '.f', 'FortranFixed'),
    ('x-pygments/foxpro', '.PRG', 'FoxPro'),
    ('text/x-freefem', '.edp', 'Freefem'),
    ('x-pygments/func', '.fc', 'FunC'),
    ('text/x-futhark', '.fut', 'Futhark'),
    ('x-pygments/gap-console', '.tst', 'GAP session'),
    ('x-pygments/gap', '.g', 'GAP'),
    ('text/x-gdscript', '.gd', 'GDScript'),
    ('x-pygments/gsql', '.gsql', 'GSQL'),
    ('x-pygments/gcode', '.gcode', 'g-code'),
    ('application/x-genshi', '.kid', 'Genshi'),
    ('application/x-genshi-text', '', 'Genshi Text'),
    ('application/x-gettext', '.pot', 'Gettext Catalog'),
    ('text/x-gherkin', '.feature', 'Gherkin'),
    ('x-pygments/golo', '.golo', 'Golo'),
    ('text/x-gooddata-cl', '.gdc', 'GoodData-CL'),
    ('text/x-gosu', '.gs', 'Gosu'),
    ('text/x-gosu-template', '.gst', 'Gosu Template'),
    ('x-pygments/graphql', '.graphql', 'GraphQL'),
    ('text/x-graphviz', '.gv', 'Graphviz'),
    ('text/x-groovy', '.groovy', 'Groovy'),
    ('text/x-hlsl', '.hlsl', 'HLSL'),
    ('x-pygments/html+ul4', '.htmlul4', 'HTML+UL4'),
    ('text/x-haml', '.haml', 'Haml'),
    ('x-pygments/handlebars', '', 'Handlebars'),
    ('text/haxe', '.hx', 'Haxe'),
    ('text/x-hsail', '.hsail', 'HSAIL'),
    ('x-pygments/hspec', '', 'Hspec'),
    ('text/html+genshi', '', 'HTML+Genshi'),
    ('text/html+smarty', '', 'HTML+Smarty'),
    ('x-pygments/haxeml', '.hxml', 'Hxml'),
    ('text/x-hy', '.hy', 'Hy'),
    ('text/x-hybris', '.hy', 'Hybris'),
    ('text/idl', '.pro', 'IDL'),
    ('x-pygments/icon', '.icon', 'Icon'),
    ('text/x-idris', '.idr', 'Idris'),
    ('text/ipf', '.ipf', 'Igor'),
    ('x-pygments/inform6', '.inf', 'Inform 6'),
    ('x-pygments/i6t', '.i6t', 'Inform 6 template'),
    ('x-pygments/inform7', '.ni', 'Inform 7'),
    ('text/x-iosrc', '.io', 'Io'),
    ('text/x-iokesrc', '.ik', 'Ioke'),
    ('text/x-isabelle', '.thy', 'Isabelle'),
    ('text/x-j', '.ijs', 'J'),
    ('x-pygments/jmespath', '.jp', 'JMESPath'),
    ('text/x-jslt', '.jslt', 'JSLT'),
    ('x-pygments/jags', '.jag', 'JAGS'),
    ('x-pygments/jasmin', '.j', 'Jasmin'),
    ('application/x-javascript+django', '.js.j2', 'JavaScript+Django/Jinja'),
    ('application/x-javascript+ruby', '', 'JavaScript+Ruby'),
    ('application/x-javascript+genshi', '', 'JavaScript+Genshi Text'),
    ('application/x-javascript+php', '', 'JavaScript+PHP'),
    ('application/x-javascript+smarty', '', 'JavaScript+Smarty'),
    ('x-pygments/js+ul4', '.jsul4', 'Javascript+UL4'),
    ('text/x-jcl', '.jcl', 'JCL'),
    ('application/jsgf', '.jsgf', 'JSGF'),
    ('x-pygments/jsonbareobject', '', 'JSONBareObject'),
    ('application/ld+json', '.jsonld', 'JSON-LD'),
    ('x-pygments/jsonnet', '.jsonnet', 'Jsonnet'),
    ('application/x-jsp', '.jsp', 'Java Server Page'),
    ('text/jsx', '.jsx', 'JSX'),
    ('x-pygments/jlcon', '', 'Julia console'),
    ('application/juttle', '.juttle', 'Juttle'),
    ('x-pygments/k', '.k', 'K'),
    ('text/kal', '.kal', 'Kal'),
    ('text/x-koka', '.kk', 'Koka'),
    ('x-pygments/kuin', '.kn', 'Kuin'),
    ('x-pygments/kql', '.kql', 'Kusto'),
    ('text/x-lsl', '.lsl', 'LSL'),
    ('text/css+lasso', '', 'CSS+Lasso'),
    ('text/html+lasso', '', 'HTML+Lasso'),
    ('application/x-javascript+lasso', '', 'JavaScript+Lasso'),
    ('text/x-lasso', '.lasso', 'Lasso'),
    ('application/xml+lasso', '', 'XML+Lasso'),
    ('text/x-ldapconf', '', 'LDAP configuration file'),
    ('text/x-ldif', '.ldif', 'LDIF'),
    ('text/x-lean', '.lean', 'Lean'),
    ('text/x-lighttpd-conf', '', 'Lighttpd configuration file'),
    ('text/limbo', '.b', 'Limbo'),
    ('x-pygments/liquid', '.liquid', 'liquid'),
    ('text/x-literate-agda', '.lagda', 'Literate Agda'),
    ('text/x-literate-cryptol', '.lcry', 'Literate Cryptol'),
    ('text/x-literate-haskell', '.lhs', 'Literate Haskell'),
    ('text/x-literate-idris', '.lidr', 'Literate Idris'),
    ('text/livescript', '.ls', 'LiveScript'),
    ('x-pygments/llvm-mir-body', '', 'LLVM-MIR Body'),
    ('x-pygments/llvm-mir', '.mir', 'LLVM-MIR'),
    ('text/x-logos', '.x', 'Logos'),
    ('text/x-logtalk', '.lgt', 'Logtalk'),
    ('text/mcfunction', '.mcfunction', 'MCFunction'),
    ('text/mcschema', '.mcschema', 'MCSchema'),
    ('x-pygments/mips', '.mips', 'MIPS'),
    ('text/x-moocode', '.moo', 'MOOCode'),
    ('x-pygments/doscon', '', 'MSDOS Session'),
    ('x-pygments/macaulay2', '.m2', 'Macaulay2'),
    ('text/css+mako', '', 'CSS+Mako'),
    ('text/html+mako', '', 'HTML+Mako'),
    ('application/x-javascript+mako', '', 'JavaScript+Mako'),
    ('application/x-mako', '.mao', 'Mako'),
    ('application/xml+mako', '', 'XML+Mako'),
    ('text/x-gooddata-maql', '.maql', 'MAQL'),
    ('text/x-mask', '.mask', 'Mask'),
    ('application/x-mason', '.m', 'Mason'),
    ('x-pygments/matlabsession', '', 'Matlab session'),
    ('x-pygments/maxima', '.mac', 'Maxima'),
    ('text/x-meson', '', 'Meson'),
    ('text/x-minidsrc', '', 'MiniD'),
    ('text/x-minicript', '.ms', 'MiniScript'),
    ('text/x-modelica', '.mo', 'Modelica'),
    ('text/x-modula2', '.def', 'Modula-2'),
    ('text/x-monkey', '.monkey', 'Monkey'),
    ('x-pygments/monte', '.mt', 'Monte'),
    ('text/x-moonscript', '.moon', 'MoonScript'),
    ('x-pygments/mosel', '.mos', 'Mosel'),
    ('x-pygments/css+mozpreproc', '.css.in', 'CSS+mozpreproc'),
    ('x-pygments/mozhashpreproc', '', 'mozhashpreproc'),
    ('x-pygments/javascript+mozpreproc', '.js.in', 'Javascript+mozpreproc'),
    ('x-pygments/mozpercentpreproc', '', 'mozpercentpreproc'),
    ('x-pygments/xul+mozpreproc', '.xul.in', 'XUL+mozpreproc'),
    ('text/x-mql', '.mq4', 'MQL'),
    ('x-pygments/mscgen', '.msc', 'Mscgen'),
    ('x-pygments/mupad', '.mu', 'MuPAD'),
    ('x-pygments/mxml', '.mxml', 'MXML'),
    ('text/css+myghty', '', 'CSS+Myghty'),
    ('text/html+myghty', '', 'HTML+Myghty'),
    ('application/x-javascript+myghty', '', 'JavaScript+Myghty'),
    ('application/x-myghty', '.myt', 'Myghty'),
    ('application/xml+myghty', '', 'XML+Myghty'),
    ('text/ncl', '.ncl', 'NCL'),
    ('text/x-nemerle', '.n', 'Nemerle'),
    ('text/x-nescsrc', '.nc', 'nesC'),
    ('x-pygments/nestedtext', '.nt', 'NestedText'),
    ('text/x-newlisp', '.lsp', 'NewLisp'),
    ('text/x-newspeak', '.ns2', 'Newspeak'),
    ('text/x-nim', '.nim', 'Nimrod'),
    ('x-pygments/nit', '.nit', 'Nit'),
    ('text/x-nodejsrepl', '', 'Node.js REPL console session'),
    ('x-pygments/notmuch', '', 'Notmuch'),
    ('x-pygments/nusmv', '.smv', 'NuSMV'),
    ('x-pygments/numpy', '', 'NumPy'),
    ('text/x-objdump', '.objdump', 'objdump'),
    ('text/x-objective-c++', '.mm', 'Objective-C++'),
    ('text/x-objective-j', '.j', 'Objective-J'),
    ('text/octave', '.m', 'Octave'),
    ('text/odin', '.odin', 'ODIN'),
    ('x-pygments/omg-idl', '.idl', 'OMG Interface Definition Language'),
    ('text/x-ooc', '.ooc', 'Ooc'),
    ('text/x-opa', '.opa', 'Opa'),
    ('text/x-openedge', '.p', 'OpenEdge ABL'),
    ('application/x-openscad', '.scad', 'OpenSCAD'),
    ('x-pygments/output', '', 'Text output'),
    ('x-pygments/pacmanconf', '', 'PacmanConf'),
    ('x-pygments/pan', '.pan', 'Pan'),
    ('text/x-parasail', '.psi', 'ParaSail'),
    ('text/x-pawn', '.p', 'Pawn'),
    ('text/x-peg', '.peg', 'PEG'),
    ('text/x-perl6', '.pl', 'Perl6'),
    ('text/x-phix', '.exw', 'Phix'),
    ('text/x-php', '.php', 'PHP'),
    ('text/x-pig', '.pig', 'Pig'),
    ('text/x-pike', '.pike', 'Pike'),
    ('text/x-plpgsql', '', 'PL/pgSQL'),
    ('x-pygments/pointless', '.ptls', 'Pointless'),
    ('x-pygments/pony', '.pony', 'Pony'),
    ('x-pygments/portugol', '.alg', 'Portugol'),
    ('text/x-postgresql-psql', '', 'PostgreSQL console (psql)'),
    ('text/x-postgresql-explain', '.explain', 'PostgreSQL EXPLAIN dialect'),
    ('text/x-povray', '.pov', 'POVRay'),
    ('x-pygments/pwsh-session', '', 'PowerShell Session'),
    ('x-pygments/praat', '.praat', 'Praat'),
    ('x-pygments/procfile', '', 'Procfile'),
    ('x-pygments/promql', '.promql', 'PromQL'),
    ('application/prql', '.prql', 'PRQL'),
    ('x-pygments/psysh', '', 'PsySH console session for PHP'),
    ('text/x-ptx', '.ptx', 'PTX'),
    ('text/x-pug', '.pug', 'Pug'),
    ('application/x-pypylog', '.pypylog', 'PyPy Log'),
    ('text/x-python2', '', 'Python 2.x'),
    ('text/x-python2-traceback', '.py2tb', 'Python 2.x Traceback'),
    ('text/x-python-doctest', '', 'Python console session'),
    ('text/x-python-traceback', '.pytb', 'Python Traceback'),
    ('x-pygments/py+ul4', '.pyul4', 'Python+UL4'),
    ('x-pygments/q', '.q', 'Q'),
    ('x-pygments/qvto', '.qvto', 'QVTO'),
    ('x-pygments/qlik', '.qvs', 'Qlik'),
    ('x-pygments/rconsole', '.Rout', 'RConsole'),
    ('x-pygments/rng-compact', '.rnc', 'Relax-NG Compact'),
    ('text/x-racket', '.rkt', 'Racket'),
    ('x-pygments/ragel-c', '.rl', 'Ragel in C Host'),
    ('x-pygments/ragel-cpp', '.rl', 'Ragel in CPP Host'),
    ('x-pygments/ragel-d', '.rl', 'Ragel in D Host'),
    ('x-pygments/ragel-em', '.rl', 'Embedded Ragel'),
    ('x-pygments/ragel-java', '.rl', 'Ragel in Java Host'),
    ('x-pygments/ragel', '', 'Ragel'),
    ('x-pygments/ragel-objc', '.rl', 'Ragel in Objective C Host'),
    ('x-pygments/ragel-ruby', '.rl', 'Ragel in Ruby Host'),
    ('application/x-pygments-tokens', '', 'Raw token data'),
    ('text/x-r-doc', '.Rd', 'Rd'),
    ('text/x-reasonml', '.re', 'ReasonML'),
    ('text/x-rebol', '.r', 'REBOL'),
    ('text/x-red', '.red', 'Red'),
    ('x-pygments/redcode', '.cw', 'Redcode'),
    ('x-pygments/resourcebundle', '', 'ResourceBundle'),
    ('text/x-rexx', '.rexx', 'Rexx'),
    ('text/html+ruby', '.rhtml', 'RHTML'),
    ('text/x-ride', '.ride', 'Ride'),
    ('text/rita', '.rita', 'Rita'),
    ('x-pygments/roboconf-graph', '.graph', 'Roboconf Graph'),
    ('x-pygments/roboconf-instances', '.instances', 'Roboconf Instances'),
    ('text/x-robotframework', '.robot', 'RobotFramework'),
    ('text/x-rql', '.rql', 'RQL'),
    ('text/rsl', '.rsl', 'RSL'),
    ('x-pygments/trafficscript', '.rts', 'TrafficScript'),
    ('text/x-ruby-shellsession', '', 'Ruby irb session'),
    ('text/x-sas', '.SAS', 'SAS'),
    ('text/S-plus', '.S', 'S'),
    ('text/x-standardml', '.sml', 'Standard ML'),
    ('text/snbt', '.snbt', 'SNBT'),
    ('text/x-sarl', '.sarl', 'SARL'),
    ('x-pygments/savi', '.savi', 'Savi'),
    ('text/x-scaml', '.scaml', 'Scaml'),
    ('text/scilab', '.sci', 'Scilab'),
    ('text/x-sed', '.sed', 'Sed'),
    ('text/shex', '.shex', 'ShExC'),
    ('text/x-shen', '.shen', 'Shen'),
    ('x-pygments/sieve', '.siv', 'Sieve'),
    ('x-pygments/silver', '.sil', 'Silver'),
    ('x-pygments/singularity', '.def', 'Singularity'),
    ('x-pygments/slash', '.sla', 'Slash'),
    ('text/x-slim', '.slim', 'Slim'),
    ('x-pygments/slurm', '.sl', 'Slurm'),
    ('text/smali', '.smali', 'Smali'),
    ('text/x-smalltalk', '.st', 'Smalltalk'),
    ('x-pygments/sgf', '.sgf', 'SmartGameFormat'),
    ('application/x-smarty', '.tpl', 'Smarty'),
    ('x-pygments/smithy', '.smithy', 'Smithy'),
    ('text/x-snobol', '.snobol', 'Snobol'),
    ('x-pygments/snowball', '.sbl', 'Snowball'),
    ('x-pygments/solidity', '.sol', 'Solidity'),
    ('x-pygments/sophia', '.aes', 'Sophia'),
    ('text/x-sourcepawn', '.sp', 'SourcePawn'),
    ('x-pygments/debsources', '', 'Debian Sourcelist'),
    ('application/sparql-query', '.rq', 'SPARQL'),
    ('text/x-spice', '.spice', 'Spice'),
    ('x-pygments/sql+jinja', '.sql', 'SQL+Jinja'),
    ('text/x-sql', '.sql', 'SQL'),
    ('text/x-sqlite3-console', '.sqlite3-console', 'sqlite3con'),
    ('text/x-squidconf', '', 'SquidConf'),
    ('x-pygments/srcinfo', '', 'Srcinfo'),
    ('application/x-ssp', '.ssp', 'Scalate Server Page'),
    ('x-pygments/stan', '.stan', 'Stan'),
    ('text/x-stata', '.do', 'Stata'),
    ('application/supercollider', '.sc', 'SuperCollider'),
    ('text/x-systemverilog', '.sv', 'systemverilog'),
    ('x-pygments/systemd', '.service', 'Systemd'),
    ('x-pygments/tap', '.tap', 'TAP'),
    ('x-pygments/tnt', '.tnt', 'Typographic Number Theory'),
    ('x-pygments/tads3', '.t', 'TADS 3'),
    ('text/x-uxntal', '.tal', 'Tal'),
    ('text/x-tasm', '.asm', 'TASM'),
    ('text/x-tcl', '.tcl', 'Tcl'),
    ('x-pygments/tcshcon', '', 'Tcsh Session'),
    ('text/x-tea', '.tea', 'Tea'),
    ('x-pygments/teal', '.teal', 'teal'),
    ('text/x-teratermmacro', '.ttl', 'Tera Term macro'),
    ('x-pygments/termcap', '', 'Termcap'),
    ('x-pygments/terminfo', '', 'Terminfo'),
    ('application/x-tf', '.tf', 'Terraform'),
    ('x-pygments/ti', '.ti', 'ThingsDB'),
    ('application/x-thrift', '.thrift', 'Thrift'),
    ('text/vnd.tiddlywiki', '.tid', 'tiddler'),
    ('x-pygments/tlb', '.tlb', 'Tl-b'),
    ('x-pygments/tls', '', 'TLS Presentation Language'),
    ('text/x-todo', '.todotxt', 'Todotxt'),
    ('text/x-tsql', '.sql', 'Transact-SQL'),
    ('x-pygments/treetop', '.treetop', 'Treetop'),
    ('text/turtle', '.ttl', 'Turtle'),
    ('text/html+twig', '.twig', 'HTML+Twig'),
    ('application/x-twig', '', 'Twig'),
    ('x-pygments/typoscriptcssdata', '', 'TypoScriptCssData'),
    ('x-pygments/typoscripthtmldata', '', 'TypoScriptHtmlData'),
    ('text/x-typoscript', '.typoscript', 'TypoScript'),
    ('x-pygments/ul4', '.ul4', 'UL4'),
    ('x-pygments/ucode', '.u', 'ucode'),
    ('text/unicon', '.icn', 'Unicon'),
    ('x-pygments/unixconfig', '', 'Unix/Linux config files'),
    ('application/x-urbiscript', '.u', 'UrbiScript'),
    ('application/x-www-form-urlencoded', '', 'urlencoded'),
    ('x-pygments/usd', '.usd', 'USD'),
    ('x-pygments/vbscript', '.vbs', 'VBScript'),
    ('text/x-vclsrc', '.vcl', 'VCL'),
    ('text/x-vclsnippet', '', 'VCLSnippets'),
    ('x-pygments/vctreestatus', '', 'VCTreeStatus'),
    ('x-pygments/vgl', '.rpf', 'VGL'),
    ('x-pygments/aspx-vb', '.aspx', 'aspx-vb'),
    ('text/html+velocity', '', 'HTML+Velocity'),
    ('x-pygments/velocity', '.vm', 'Velocity'),
    ('application/xml+velocity', '', 'XML+Velocity'),
    ('text/x-verifpal', '.vp', 'Verifpal'),
    ('x-pygments/visualprologgrammar', '.vipgrm', 'Visual Prolog Grammar'),
    ('x-pygments/visualprolog', '.pro', 'Visual Prolog'),
    ('x-pygments/vyper', '.vy', 'Vyper'),
    ('x-pygments/wdiff', '.wdiff', 'WDiff'),
    ('x-pygments/wast', '.wat', 'WebAssembly'),
    ('x-pygments/webidl', '.webidl', 'Web IDL'),
    ('text/wgsl', '.wgsl', 'WebGPU Shading Language'),
    ('text/x-whiley', '.whiley', 'Whiley'),
    ('text/x-wiki', '', 'Wikitext'),
    ('x-pygments/wowtoc', '.toc', 'World of Warcraft TOC'),
    ('x-pygments/wren', '.wren', 'Wren'),
    ('text/x-x10', '.x10', 'X10'),
    ('x-pygments/xml+ul4', '.xmlul4', 'XML+UL4'),
    ('text/xquery', '.xqy', 'XQuery'),
    ('application/xml+django', '.xml.j2', 'XML+Django/Jinja'),
    ('application/xml+ruby', '', 'XML+Ruby'),
    ('application/xml+php', '', 'XML+PHP'),
    ('application/xml+smarty', '', 'XML+Smarty'),
    ('x-pygments/xorg.conf', '', 'Xorg'),
    ('x-pygments/xpp', '.xpp', 'X++'),
    ('application/xsl+xml', '.xsl', 'XSLT'),
    ('text/x-xtend', '.xtend', 'Xtend'),
    ('x-pygments/extempore', '.xtm', 'xtlang'),
    ('text/x-yaml+jinja', '.sls', 'YAML+Jinja'),
    ('application/yang', '.yang', 'YANG'),
    ('text/x-yara', '.yar', 'YARA'),
    ('x-pygments/zephir', '.zep', 'Zephir'),
    ('text/zig', '.zig', 'Zig'),
    ('x-pygments/ansys', '.ans', 'ANSYS parametric design language'),
]

types = {entry[0]: entry[2] for entry in supported if entry[0] != 'heading'}
extensions = {entry[0]: entry[1] for entry in supported if entry[0] != 'heading'}

extmap = {}
for mime, ext in extensions.items():
    if not ext:
        continue

    try:
        extmap[ext].add(mime)
    except KeyError:
        extmap[ext] = {mime}

languages = '\n'.join('<option value="{}">{}</option>'.format(entry[0], html.escape(entry[2])) if entry[0] != 'heading' else '<option disabled>──────────</option>\n<option disabled>{}</option>'.format(html.escape(entry[2])) for entry in supported)
