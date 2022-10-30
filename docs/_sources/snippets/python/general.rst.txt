General Python Snippets
=========================

Meta-Programming
-----------------

Meta-Classes
~~~~~~~~~~~~~~

Singleton
++++++++++++

.. code:: python

   class SingletonMeta(type):
      _instance = {}
      def __call__(cls, *args, **kwargs):
         if cls not in cls._instance:
               cls._instance[cls] = super(SingletonMeta, cls).__call__(*args, **kwargs)
         return cls._instance[cls]


Prohibitive Singleton
+++++++++++++++++++++++

.. code:: python

   class ProhibitiveSingletonMeta(type):
      _instance = None
      def __call__(cls, *args, **kwargs):
         if cls._instance is not None:
               raise RuntimeError(f"There can only be one instance of {cls.__name__}")
         cls._instance = super(ProhibitiveSingletonMeta, cls).__call__(*args, **kwargs)
         return cls._instance


custom-Builtins
-----------------

Dict
~~~~~~~~

ChangeAwareDict
+++++++++++++++++++

.. code:: python

   class ChangeAwareDict(dict):

      def __init__(self, *args, **kwargs):
         self.changed_listeners: set = set()
         super().__init__(*args, **kwargs)

      def connect_to_change_signal(self, target: Callable):
         self.changed_listeners.add(target)

      def emit_changed(self, key, value):
         for target in self.changed_listeners:
               target(key, value)

      def __setitem__(self, k, v) -> None:
         super().__setitem__(k, v)
         self.emit_changed(key=k, value=v)


Unsorted
-----------

Function name from inside function
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code:: python

   sys._getframe().f_code.co_name


Get Current Python Interpreter Path
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code:: python

   sys.executable


Get Venv Folder - or Python Folder if not in Venv
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code:: python

   sys.exec_prefix


Get Venv Scripts Folder - or Python Scripts Folder if not in Venv
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code:: python

   sysconfig.get_path


Get Venv site-packages Folder - or Python site-packages Folder if not in Venv
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code:: python

   sysconfig.get_path('purelib')


Get windows PATH as list
~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code:: python

   os.get_exec_path()


all loaded modules as dict
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code:: python

   sys.modules


all stdlib module names
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code:: python

   sys.stdlib_module_names



get python version
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code:: python

   major, minor, micro, _, _ = sys.version_info
   version_string = f"{major}.{minor}.{micro}"


get name and author from package
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code:: python

   from importlib.metadata import metadata

   APP_NAME = metadata(__name__).get('name')
   AUTHOR_NAME = metadata(__name__).get('author')

get package info
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code:: python

   def get_package_info(package_name):
      url = f"https://pypi.python.org/pypi/{package_name}/json"
      response = requests.get(url=url)
      if response.status_code == 404:
         # TODO: Custom ERROR
         raise RuntimeError(f"unable to get package info for package '{package_name}'")

      return response.json()


find all print statements
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. admonition:: required packages

   * `attrs <https://pypi.org/project/attrs/>`_


.. code:: python

    import attr
    from functools import cached_property
    from itertools import cycle
    from pathlib import Path
    import re


    @attr.s(auto_attribs=True, auto_detect=True, kw_only=True, frozen=True)
    class FoundPrintStmt:
        file_path: Path = attr.ib(converter=Path)
        line_number: int = attr.ib()
        line: str = attr.ib(converter=lambda x: x.rstrip('\n'))
        match: re.Match = attr.ib()

        @cached_property
        def matched_text(self):
            return self.match.group('stmt')

        @cached_property
        def pretty_line(self):
            mod_line = f"{self.line_number}|| {self.line}"
            offset = len(mod_line) - (len(self.line) + len(str(self.line_number)))

            indicator_chars = (cycle("╳~"), cycle("╳~"))
            indicator_string_top = ''.join(next(indicator_chars[0]) for _ in range(len(self.matched_text)))
            indicator_string_bottom = ''.join(next(indicator_chars[1]) for _ in range(len(self.matched_text)))
            top_line = ' ' * (self.match.start('stmt') + len(str(self.line_number)) + offset) + indicator_string_top
            bottom_line = ' ' * (self.match.start('stmt') + len(str(self.line_number)) + offset) + indicator_string_bottom

            return '\n'.join([top_line, mod_line, bottom_line])

        def as_dict(self):
            return attr.asdict(self) | {'matched_text': self.matched_text, 'pretty_line': self.pretty_line}


    def find_print_stmts(in_path):
        print_regex = re.compile(r'(?:\s|^)(?P<stmt>(print|pprint|ic)\(.*\))')

        def _find_print_stmts_in_file(in_file: Path):
            line_no = 0
            with in_file.open('r', encoding='utf-8') as f:
                for line in f:
                    line_no += 1
                    line = line.strip('\n')
                    if line.strip() == '':
                        continue
                    match = print_regex.search(line)
                    if not match:
                        continue
                    yield FoundPrintStmt(file_path=in_file, line_number=line_no, line=line, match=match)

        in_path = Path(in_path)

        if in_path.is_file():
            if in_path.suffix != '.py':
                raise TypeError(f'can only be used with ".py" files, not {in_path.suffix!r}')
            yield from _find_print_stmts_in_file(in_path)

        else:
            for dirname, folderlist, filelist in os.walk(in_path):
                for file in (Path(dirname, _file) for _file in filelist if _file.endswith('.py')):
                    if file.stat().st_size >= 10_485_760:
                        continue
                    yield from _find_print_stmts_in_file(file)
