In [1]: my_string = "python"

In [2]: my_string1 = 'python'

In [3]: print type(my_string)
<type 'str'>

In [4]: print type(my_string1)
<type 'str'>

In [5]: my_num1 = 10

In [6]: print type(my_num1)
<type 'int'>

In [7]: my_num2 = 10.0

In [8]: print type(my_num2)
<type 'float'>

In [9]: my_num3 = "10.0"

In [10]: print type(my_num3)
<type 'str'>


In [12]: my_string.upper?
Docstring:
S.upper() -> string

Return a copy of the string S converted to uppercase.
Type:      builtin_function_or_method

In [13]: my_string.upper()
Out[13]: 'PYTHON'

In [14]: my_string.upper??
Type: builtin_function_or_method


# task1:

In [15]: my_string.
              my_string.capitalize my_string.isalnum    my_string.lstrip     my_string.splitlines 
              my_string.center     my_string.isalpha    my_string.partition  my_string.startswith 
              my_string.count      my_string.isdigit    my_string.replace    my_string.strip      
              my_string.decode     my_string.islower    my_string.rfind      my_string.swapcase   
              my_string.encode     my_string.isspace    my_string.rindex     my_string.title      
              my_string.endswith   my_string.istitle    my_string.rjust      my_string.translate  
              my_string.expandtabs my_string.isupper    my_string.rpartition my_string.upper      
              my_string.find       my_string.join       my_string.rsplit     my_string.zfill      
              my_string.format     my_string.ljust      my_string.rstrip                          
              my_string.index      my_string.lower      my_string.split                           



In [15]: print my_num1
10

In [16]: print my_num2
10.0

In [17]: my_num1.
                  my_num1.bit_length  my_num1.imag        
                  my_num1.conjugate   my_num1.numerator   
                  my_num1.denominator my_num1.real        


In [17]: my_num2.
                  my_num2.as_integer_ratio my_num2.hex              my_num2.real             
                  my_num2.conjugate        my_num2.imag                                      
                  my_num2.fromhex          my_num2.is_integer                                


tcloudost@tcloudost-VirtualBox ~/Documents/git_repositories/python-batches $ python
Python 2.7.6 (default, Jun 22 2015, 17:58:13) 
[GCC 4.8.2] on linux2
Type "help", "copyright", "credits" or "license" for more information.
>>> 
>>> help()

Welcome to Python 2.7!  This is the online help utility.

If this is your first time using Python, you should definitely check out
the tutorial on the Internet at http://docs.python.org/2.7/tutorial/.

Enter the name of any module, keyword, or topic to get help on writing
Python programs and using Python modules.  To quit this help utility and
return to the interpreter, just type "quit".

To get a list of available modules, keywords, or topics, type "modules",
"keywords", or "topics".  Each module also comes with a one-line summary
of what it does; to list the modules whose summaries contain a given word
such as "spam", type "modules spam".

help> keywords

Here is a list of the Python keywords.  Enter any keyword to get more help.

and                 elif                if                  print
as                  else                import              raise
assert              except              in                  return
break               exec                is                  try
class               finally             lambda              while
continue            for                 not                 with
def                 from                or                  yield
del                 global              pass                

help> topics

Here is a list of available topics.  Enter any topic name to get more help.

ASSERTION           DEBUGGING           LITERALS            SEQUENCEMETHODS2
ASSIGNMENT          DELETION            LOOPING             SEQUENCES
ATTRIBUTEMETHODS    DICTIONARIES        MAPPINGMETHODS      SHIFTING
ATTRIBUTES          DICTIONARYLITERALS  MAPPINGS            SLICINGS
AUGMENTEDASSIGNMENT DYNAMICFEATURES     METHODS             SPECIALATTRIBUTES
BACKQUOTES          ELLIPSIS            MODULES             SPECIALIDENTIFIERS
BASICMETHODS        EXCEPTIONS          NAMESPACES          SPECIALMETHODS
BINARY              EXECUTION           NONE                STRINGMETHODS
BITWISE             EXPRESSIONS         NUMBERMETHODS       STRINGS
BOOLEAN             FILES               NUMBERS             SUBSCRIPTS
CALLABLEMETHODS     FLOAT               OBJECTS             TRACEBACKS
CALLS               FORMATTING          OPERATORS           TRUTHVALUE
CLASSES             FRAMEOBJECTS        PACKAGES            TUPLELITERALS
CODEOBJECTS         FRAMES              POWER               TUPLES
COERCIONS           FUNCTIONS           PRECEDENCE          TYPEOBJECTS
COMPARISON          IDENTIFIERS         PRINTING            TYPES
COMPLEX             IMPORTING           PRIVATENAMES        UNARY
CONDITIONAL         INTEGER             RETURNING           UNICODE
CONTEXTMANAGERS     LISTLITERALS        SCOPING             
CONVERSIONS         LISTS               SEQUENCEMETHODS1    

help> LISTS

Related help topics: LISTLITERALS

help> modules

Please wait a moment while I gather a list of all available modules...

/usr/local/lib/python2.7/dist-packages/IPython/kernel/__init__.py:13: ShimWarning: The `IPython.kernel` package has been deprecated. You should import from ipykernel or jupyter_client instead.
  "You should import from ipykernel or jupyter_client instead.", ShimWarning)
/usr/lib/python2.7/dist-packages/gobject/constants.py:24: Warning: g_boxed_type_register_static: assertion 'g_type_from_name (name) == 0' failed
  import gobject._gobject
No handlers could be found for logger "oneconf.distributor"
/usr/lib/python2.7/dist-packages/gtk-2.0/gtk/__init__.py:127: RuntimeWarning: PyOS_InputHook is not available for interactive use of PyGTK
  set_interactive(1)
ANSI                apt                 gtkunixprint        requests
AptUrl              apt_inst            gzip                resource
BaseHTTPServer      apt_pkg             hashlib             rexec
Bastion             aptdaemon           heapq               rfc822
BeautifulSoup       aptsources          hmac                rlcompleter
BeautifulSoupTests  argparse            hotshot             rmagic
CDROM               array               html5lib            robotparser
CGIHTTPServer       ast                 htmlentitydefs      runpy
Canvas              asynchat            htmllib             samba
CommandNotFound     asyncore            httplib             sched
ConfigParser        atexit              httplib2            screen
Cookie              atk                 idlelib             select
Crypto              audiodev            ihooks              serial
DLFCN               audioop             imaplib             sessioninstaller
Dialog              autoreload          imghdr              sets
DocXMLRPCServer     axi                 imp                 setuptools
Exscript            backports           importlib           sexy
Exscriptd           backports_abc       imputil             sgmllib
FSM                 base64              inspect             sha
FileDialog          bdb                 io                  shelve
FixTk               binascii            ipykernel           shlex
HTMLParser          binhex              ipython_genutils    shutil
IN                  bisect              ipywidgets          shutil_backports
IPython             bonobo              itertools           signal
Image               bpdb                jinja2              simplegeneric
ImageChops          bpython             json                singledispatch
ImageColor          bsddb               jsonschema          singledispatch_helpers
ImageCrackCode      bz2                 jupyter             sip
ImageDraw           cPickle             jupyter_client      sipconfig
ImageEnhance        cProfile            jupyter_console     sipconfig_nd
ImageFile           cStringIO           jupyter_core        site
ImageFileIO         cairo               keyword             sitecustomize
ImageFilter         calendar            ldb                 six
ImageFont           caribou             lib2to3             smbc
ImageGL             certifi             libxml2             smtpd
ImageGrab           cgi                 libxml2mod          smtplib
ImageMath           cgitb               linecache           sndhdr
ImageOps            chardet             linuxaudiodev       socket
ImagePalette        chunk               locale              spwd
ImagePath           cmath               lockfile            spyderlib
ImageQt             cmd                 logging             spyderplugins
ImageSequence       code                lsb_release         sqlite3
ImageStat           codecs              lxml                sre
ImageTk             codeop              macpath             sre_compile
ImageWin            collections         macurl2path         sre_constants
MimeWriter          colorama            mailbox             sre_parse
MySQLdb             colorsys            mailcap             ssl
ORBit               commands            mako                stat
OpenSSL             compileall          markupbase          statvfs
PAM                 compiler            markupsafe          storemagic
PIL                 configglue          marshal             string
PSDraw              configobj           math                stringold
PngImagePlugin      configparser        md5                 stringprep
PyQt4               contextlib          mhlib               strop
Queue               cookielib           mimetools           struct
ScrolledText        copy                mimetypes           subprocess
SimpleDialog        copy_reg            mimify              sunau
SimpleHTTPServer    crypt               mistune             sunaudio
SimpleXMLRPCServer  csv                 mmap                symbol
SocketServer        ctypes              modulefinder        sympyprinting
StringIO            cups                multifile           symtable
TYPES               cupshelpers         multiprocessing     sys
Tix                 curl                mutex               sysconfig
TkExscript          curses              mysql               syslog
Tkconstants         cv                  nbconvert           tabnanny
Tkdnd               cv2                 nbformat            talloc
Tkinter             cythonmagic         netrc               tarfile
UbuntuSystemService datetime            new                 tdb
UserDict            dbhash              nis                 telnetlib
UserList            dbm                 nntplib             tempfile
UserString          dbus                notebook            terminado
_LWPCookieJar       deb822              ntdb                termios
_MozillaCookieJar   debconf             ntpath              test
__builtin__         debian              nturl2path          tests
__future__          debian_bundle       numbers             textwrap
_abcoll             debtagshw           numpy               this
_ast                decimal             oauthlib            thread
_bisect             decorator           oneconf             threading
_bsddb              defer               opcode              tidy
_codecs             difflib             operator            time
_codecs_cn          dircache            optparse            timeit
_codecs_hk          dirspec             os                  tkColorChooser
_codecs_iso2022     dis                 os2emxpath          tkCommonDialog
_codecs_jp          distlib             ossaudiodev         tkFileDialog
_codecs_kr          distutils           pango               tkFont
_codecs_tw          django              pangocairo          tkMessageBox
_collections        dns                 paramiko            tkSimpleDialog
_csv                doctest             parser              toaiff
_ctypes             drv_libxml2         parted              token
_ctypes_test        dsextras            pathlib2            tokenize
_curses             dumbdbm             pdb                 tornado
_curses_panel       dummy_thread        pexpect             trace
_dbus_bindings      dummy_threading     pickle              traceback
_dbus_glib_bindings duplicity           pickleshare         traitlets
_elementtree        easy_install        pickletools         ttk
_functools          email               pip                 tty
_hashlib            encodings           pipes               turtle
_heapq              entrypoints         piston_mini_client  twisted
_hotshot            errno               pkg_resources       types
_io                 exceptions          pkgutil             ubuntu_sso
_json               fabfile             platform            unicodedata
_locale             fabric              plistlib            unittest
_lsprof             fcntl               popen2              urllib
_markerlib          fdpexpect           poplib              urllib2
_md5                feedparser          posix               urllib3
_multibytecodec     filecmp             posixfile           urlparse
_multiprocessing    fileinput           posixpath           user
_mysql              fnmatch             pprint              uu
_mysql_exceptions   formatter           profile             uuid
_osx_support        fpectl              prompt_toolkit      validate
_ped                fpformat            pstats              virtualenv
_pyio               fractions           pty                 vte
_random             ftplib              ptyprocess          warnings
_sha                functools           pwd                 wave
_sha256             functools32         pxssh               wcwidth
_sha512             future_builtins     py_compile          weakref
_smbc               gc                  pyatspi             webbrowser
_socket             gconf               pyclbr              webkit
_sqlite3            gdbm                pycurl              whichdb
_sre                genericpath         pydoc               widgetsnbextension
_ssl                getopt              pydoc_data          wsgiref
_strptime           getpass             pyexpat             xapian
_struct             gettext             pygments            xdg
_symtable           gi                  pygtk               xdrlib
_sysconfigdata      gio                 pygtkcompat         xml
_sysconfigdata_nd   glib                pyinotify           xmllib
_testcapi           glob                pynotify            xmlrpclib
_threading_local    gnome               pyodbc              xxsubtype
_tkinter            gnomecanvas         pysqlite2           zipfile
_warnings           gnomekeyring        qtconsole           zipimport
_weakref            gnomevfs            quopri              zlib
_weakrefset         gobject             random              zmq
abc                 google              re                  zope
aifc                grp                 readline            
antigravity         gtk                 reportlab           
anydbm              gtksourceview2      repr                

Enter any module name to get more help.  Or, type "modules spam" to search
for modules whose descriptions contain the word "spam".

help> 

help> quit

You are now leaving help and returning to the Python interpreter.
If you want to ask for help on a particular object directly from the
interpreter, you can type "help(object)".  Executing "help('string')"
has the same effect as typing a particular string at the help> prompt.
>>> 
>>> 
>>> my_string = "python"
>>> print dir(my_string)
['__add__', '__class__', '__contains__', '__delattr__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__', '__getitem__', '__getnewargs__', '__getslice__', '__gt__', '__hash__', '__init__', '__le__', '__len__', '__lt__', '__mod__', '__mul__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__rmod__', '__rmul__', '__setattr__', '__sizeof__', '__str__', '__subclasshook__', '_formatter_field_name_split', '_formatter_parser', 'capitalize', 'center', 'count', 'decode', 'encode', 'endswith', 'expandtabs', 'find', 'format', 'index', 'isalnum', 'isalpha', 'isdigit', 'islower', 'isspace', 'istitle', 'isupper', 'join', 'ljust', 'lower', 'lstrip', 'partition', 'replace', 'rfind', 'rindex', 'rjust', 'rpartition', 'rsplit', 'rstrip', 'split', 'splitlines', 'startswith', 'strip', 'swapcase', 'title', 'translate', 'upper', 'zfill']
>>> 
>>> print help(my_string.upper)

None
>>> 

