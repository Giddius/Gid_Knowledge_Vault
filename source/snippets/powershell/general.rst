General Powershell Snippets
===============================

Get all local Git Repo Paths
-------------------------------

.. code:: powershell

   foreach ($i in (gdr -PSProvider 'FileSystem')){
      Set-Location -Path $i.Root;
      Get-ChildItem . -Attributes Directory+Hidden -ErrorAction SilentlyContinue -Filter ".git" -Recurse | % { Write-Host $_.parent.FullName }
   }


Folder of Script itself
------------------------

.. code:: powershell

   $PSScriptRoot


Requires Admin
-----------------

.. code:: powershell

   #Requires -RunAsAdministrator


Get all Hard-Drives
----------------------

.. code:: powershell

   gdr -PSProvider 'FileSystem'