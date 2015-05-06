================================
Introduction to the Command Line
================================

The Terminal
============

The Terminal...A.K.A.
---------------------

- The Shell

- The Command Line

- Console

- A way to talk to your computer

- :incremental:`Your portal to the file system`

Opening the Terminal
--------------------

- Mac

  - Command-Space to open spotlight, type `term`

  - Finder |rarr| Applications |rarr| Utilities |rarr| Terminal

  - Pin it to the dock

- Linux

  - Click on icon in upper left, type `term`

  - Find it on the launchbar on the lab machines

Okay, It's Open. Now What?
--------------------------

- Inside the terminal, you'll be running a "shell"

  - The shell is a special type of program

  - Allows you to talk directly to the file system

  - The default shell is called "bash"

  - It's waiting for you to type at the "prompt"

The Prompt
----------

- Lots of information in the prompt

- It's waiting for you to give it a job to do

- Every command is a program

- Most commands:

  - Have a mnemonic of some sort

  - Are two or three letters long

  - Take arguments, many similar to other commands

Example: Where am I?
--------------------

- It's very handy to know where you are

- Print Working Directory

.. parsed-literal::
  :class: console

  $ `pwd`:cmd:
  /Users/rachel

.. newslide::

Wait. That was gibberish. What on earth does `/Users/rachel` mean?

The File System
===============

The File System
---------------

- Visualize it as an upside down tree

- :incremental:`It has a root`

- :incremental:`And branches`

- :incremental:`And leaves`

Exploring the File System
-------------------------

- Where was I?

- :incremental:`pwd`

ls: List Files in a Directory
=============================

ls
--

List files in a directory

.. parsed-literal::
  :class: console

  $ `ls`:cmd:
  Desktop/     Documents/      Downloads/
  Pictures/    part-time/      notes.txt      

ls -a
-----

List all files in a directory, including hidden files

.. parsed-literal::
  :class: console

  $ `ls - a`:cmd:
  ./           Desktop/     Documents/      Downloads/
  ../          Pictures/    part-time/      notes.txt 
  .bashrc      .vimrc               


ls -l
-----

.. parsed-literal::
  :class: console

  $ `ls -l`:cmd:
  -rw-r--r--   1 rachel  staff  142 Oct 27 22:13 notes.txt
  -rw-r--r--   1 rachel  staff  142 Oct 28 22:15 Desktop/
  drwxr-xr-x  15 rachel  staff  510 Oct 30 12:13 part-time/
  etc.

ls -al
------

.. parsed-literal::
  :class: console

  $ `ls -al`:cmd:
  -rw-r--r--   1 rachel  staff  142 Oct 27 20:13 .bashrc
  -rw-r--r--   1 rachel  staff  142 Oct 27 22:13 notes.txt
  drwx------   1 rachel  staff  142 Oct 28 22:15 Desktop/
  drwxr-xr-x   6 rachel  staff  510 Oct 30 12:13 part-time/

You can also do them separately, as in 'ls -a -l'

cd: Change Directory
====================

cd: Change Directory
--------------------

Used to change into a new working directory

.. parsed-literal::
  :class: console

  $ `pwd`:cmd:
  /Users/rachel
  $ `cd part-time`:cmd:
  $ `pwd`:cmd:
  /Users/rachel/part-time

Move and Copy
=============

mv: Move and Rename
-------------------

.. parsed-literal::
  :class: console

  $ `ls`:cmd:
  file          file1        file2       file3

  $ `mv file file.txt`:cmd:

  $ `ls`:cmd:
  file.txt      file1        file2       file3

cp: Copy
--------

.. parsed-literal::
  :class: console

  $ `ls`:cmd:
  file       file1          file2        file3

  $ `cp file file.txt`:cmd:

  $ `ls`:cmd:
  file       file.txt       file1        file2       file3

Tab Complete All the Things!!
=============================

rm: Remove File(s)
==================

rm: Remove File(s)
------------------

.. parsed-literal::
  :class: console

  $ `ls`:cmd:
  file       file.txt       file1        file2       file3

  $ `rm file.txt`:cmd:
  file       file1        file2       file3

Making and Removing Directories
===============================

mkdir: Make Directory
---------------------

.. parsed-literal::
  :class: console

  $ `mkdir ubermelon`:cmd:

rmdir: Remove Directory
-----------------------

.. parsed-literal::
  :class: console

  $ `rmdir ubermelon`:cmd:


Things the Shell Knows
======================

If You're Lost, You Can Always Go $HOME
---------------------------------------

Where home is is one of the many things that the shell knows.

.. parsed-literal::
  :class: console

  $ `cd`:cmd:
  $ `cd /Users/rachel`:cmd:
  $ `cd $HOME`:cmd:

And Introducing...the ~
-----------------------

The tilde (``~``) is another way the shell refers to `$HOME`

.. parsed-literal::
  :class: console

  $ `cd ~`:cmd:
  $ `cd ~/`:cmd:

The Environment
---------------

.. parsed-literal::
  :class: console

  $ `env`:cmd:
  SHELL=/bin/bash
  USER=rachel
  HOME=/Users/rachel
  PATH=/usr/local/bin:/usr/bin:/bin:/usr/sbin:/sbin
  etc.

The Shell Knows What You've Done
--------------------------------

.. parsed-literal::
  :class: console

  $ `history`:cmd:
  534  ls
  535  ls bob
  536  ls sally
  537  ls ubermelon
  538  history
  $

Use Arrow Keys to Traverse History
----------------------------------

Or: How to type even less

- Up arrow goes backwards through history list

- Down arrow goes forwards until it hits most recent

Three Special Commands
======================

Make it Stahp
-------------

- `<Ctrl-C>` is called a "Keyboard Interrupt"

- This stops a runaway process (i.e. an infinite loop)

Get Me Out of Here
------------------

- `<Ctrl-D>` is "Exit"

- This will exit a shell, including python shells

.. only:: not revealjs

  Except on Windows, where `<Ctrl-Z>` is used to exit shells, includign
  the Python shell.

Suspend Me
----------

- `<Ctrl-Z>` is "Suspend"

- Just. No. For now.

.. only:: not revealjs

  Except on Windows, where `<Ctrl-Z>` is used to exit shells. There is
  no "suspend" keyboard equivalent on Windows.

