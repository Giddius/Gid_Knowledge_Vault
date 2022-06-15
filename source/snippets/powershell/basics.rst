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

