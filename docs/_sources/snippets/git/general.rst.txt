General Git Snippets
========================


Unsorted
------------

Find Base Folder
~~~~~~~~~~~~~~~~~~

.. code:: console

   git rev-parse --show-toplevel


Branch names
~~~~~~~~~~~~~~~~~~

.. code:: console

   git branch


.. admonition:: options

   :-r: to only get remote branches
   :-a: to get remote and local branches

Delete Branch
~~~~~~~~~~~~~~~~~~

locally
+++++++++

.. code:: console

   git branch -d [branch_name]


.. admonition:: options

   :-D: replace `-d` with `-D` to force deletion. `-d` fails if the branch has not been pushed.

remote
+++++++++


.. code:: console

   git push -d [origin] [branch_name]


Branch info
~~~~~~~~~~~~~~~~~~


.. code:: console

   git show [OPTIONAL: branch_name]


ASCII Tree
~~~~~~~~~~~~~~~~~~

.. code:: console

   git log --graph --oneline


.. admonition:: options

   :--all: add `--all` to get the tree of all branches



Backup
~~~~~~~~~~~~~~~~~~

.. code:: console

   git bundle create <file_name or file_path>.bundle --all

