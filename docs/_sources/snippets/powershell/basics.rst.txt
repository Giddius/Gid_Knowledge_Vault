Basic Powershell Snippets
===========================

Variables
---------------

Assign variable
~~~~~~~~~~~~~~~~~~

.. code:: powershell

   $var_name = "this"



Environment
---------------

Set environment variable
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code:: powershell

   $env:VAR_NAME = 'variable'



Get all environment variables
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code:: powershell

   dir env:


Calling
---------

Call Operator
~~~~~~~~~~~~~~~

.. code:: powershell

   & 'c:\Path\To\target.exe'

Output to Variable
~~~~~~~~~~~~~~~~~~~~~

.. code:: powershell

   $outputVariable = (($callCommand) | Out-String).Trim()


Example
^^^^^^^^^^^^

.. container:: code_example

   .. code:: powershell

      $rawBasePythonDir = ((python -c "import sys;print(sys.base_prefix)") | Out-String).Trim()

Path Handling
---------------

String to Path-Object
~~~~~~~~~~~~~~~~~~~~~~~~

.. code:: powershell

   $pathObject = Resolve-Path $stringPath