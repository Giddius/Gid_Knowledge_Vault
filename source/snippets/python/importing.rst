Importing
============


Import Module From a Path
---------------------------

.. code:: python

   from pathlib import Path
   import importlib.util
   from types import ModuleType

   def import_module_from_path(module_name: str, module_path: Path) -> ModuleType:
      if module_path.is_dir:
         module_path = module_path.joinpath("__init__.py")
      spec = importlib.util.spec_from_file_location(module_name, module_path)
      module = importlib.util.module_from_spec(spec)
      sys.modules[module_name] = module
      spec.loader.exec_module(module)
      return module