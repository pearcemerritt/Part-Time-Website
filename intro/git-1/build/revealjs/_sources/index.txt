========================
Version Control with Git
========================

Version Control
===============

What Is Version Control?
------------------------

.. only:: not revealjs

  Version control lets use manage software development safely:
  
- Track changes
- Look at older revisions
- Revert to early revision
- Share code/collaborate easily
- :incremental-li:`Save your bacon when you break something`

.. newslide::

- Homemade version control with filenames:

  - ``resume-version-1.docx``
  - ``resume-version-2.docx``
  - ``plan-update-20120122.docx``
  - ``plan-update-20121012.docx``

- :incremental-li:`Git is like this but a million times better`

Multiple Files
--------------

Tracks entire project (could be many files in folders, even):

.. parsed-literal::
  :class: console

  $ `ls`:cmd:
  NOTES          app_setup.py      db_reset.py         search.py
  README         config.py         flask/              tests.db
  app/           db_create.py      requirements.txt    tests.py
  app.db         db_migrate.py     run.py              trials.py

Git Intro
=========

Git
---

.. container:: item-incremental

  - Most popular Open Source version control program

  - Runs on Linux, OSX, and Windows

  - Main concern: safety!
  
Terminology WTF?!
-----------------

Directory
  Folder of files (which can contain subdirectories)

Repository
  Project kept under version control; can
  contain subdirectories

Working Directory
  *Your* particular copy of a repository
  
.. newslide::

Until we turn a directory into a repository, git won't work (and isn't
tracking anything):

.. parsed-literal::
  :class: console

  $ `mkdir play`:cmd:
  $ `cd play`:cmd:

  $ `git status`:cmd:
  fatal: Not a git repository (or any of the parent directories): .git

Creating Repository
-------------------

Turn your directory into a repository with ``git init``. 

.. parsed-literal::
  :class: console

  $ `git init`:cmd:
  Initialized empty Git repository in /tmp/play/.git/

You only need to do this once.

You can do it when you create the project or at a later point.

.. only:: not revealjs

  This creates a subdirectory called ``.git`` but, because this starts with a leading
  dot, Unix and OSX computers won't list this directory for you. You can see all
  directories, including those that start with a leading dot, with ``ls -a``.

  In larger projects, you might have your own subdirectories. The entire 
  project--subdirectories and all--is one repository, and you only need to do 
  ``git init`` once.

Untracked Files
---------------


Let's create a file, `hello.py`, in our repository::

  print "Hello"

Git can tell we've created this file but it also knows we haven't told it
to "track" it.

.. newslide::

.. parsed-literal::
  :class: console

  $ `git status`:cmd:
  On branch master

  Initial commit

  Untracked files:
    (use "git add <file>..." to include in what will be committed)

          `hello.py`:red:

  nothing added to commit but untracked files present (use "git add" 
  to track)

Tracking a File
---------------

For Git to manage files, "track" them with ``git add``:

.. parsed-literal::
  :class: console

  $ `git add hello.py`:cmd:

.. newslide::

Once we do that, we can see that Git is tracking our file:

.. parsed-literal::
  :class: console

  $ `git status`:cmd:
  On branch master

  Initial commit

  Changes to be committed:
    (use "git rm --cached <file>..." to unstage)

          `new file:   hello.py`:green:

First Check-In!
---------------

Our program is working! Let's "commit" it:

.. parsed-literal::
  :class: console

  $ `git commit -a -m "Say hello"`:cmd:
  [master (root-commit) 6f267125] Say hello
   1 file changed, 1 insertion(+)
   create mode 100644 hello.py

-a    Commit all *tracked* files

-m    Check-in message (record of what you did)

.. only:: not revealjs

  Instead of using ``-a``, you can specify individual files/directories to
  commit, like ``git commit -m "Message" file1.py file2.py`` -- but this is less common,
  since you'll typically want to check in the entire repository at a time.

  If you leave off the ``-m``, Git will open up an editor for you to enter a commit
  message there. 

  Here at the lab, it will open up "nano", a small and simple Unix editor. To save your
  work, type ``Control-X``, "Y" to confirm saving, and ``Enter`` to accept the filename.
  
  On many other computers, it will open up "Vim", a powerful (and slightly cryptic)
  Unix editor. This may happen on your personal laptop or other machines you use in the 
  future. If it opens up Vim and you don't know how to use it, type ``:q<return>``
  (colon, q, return) to quit. You can then re-type your commit command with the ``-m`` switch.

Did it Work?
------------

``git status`` shows us the state of our repository:

.. parsed-literal::
  :class: console

  $ `git status`:cmd:
  On branch master
  nothing to commit, working directory clean

.. newslide:: No, Really, Did It Work?

``git log`` shows us a log of our revision history:

.. parsed-literal::
  :class: console

  $ `git log`:cmd:
  commit `faa215bd9dd82ce8dca58f3ab3d0ece49d6fb351`:tan:
  Author: Jessica Developer <jess@gmail.com>
  Date:   Wed Sep 17 21:13:02 2014 -0700

    Say hello

Keep Working
------------

Make a change to `hello.py`:

::

  print "Hello"
  print "World"

Git knows we've modified the file since we committed it:

.. parsed-literal::
  :class: console

  $ `git status`:cmd:
  On branch master
  Changes not staged for commit:
    (use "git add <file>..." to update what will be committed)
    (use "git checkout -- <file>..." to discard changes in working 
    directory)

          `modified:   hello.py`:red:

  no changes added to commit (use "git add" and/or "git commit -a")

.. newslide::

Let's check in our changed version:

.. parsed-literal::
  :class: console

  $ `git commit -a -m "Add world"`:cmd:
  [master 411455e8] Add world
   1 file changed, 1 insertion(+)

And So On
---------

Keep editing and committing every so often.

Logs
====

Git Log
-------

``git log`` shows us all history, from most-recent to oldest:

.. parsed-literal::
  :class: console

  $ git log
  commit `d9808883c4432ee61c56a1df7d0c5330a5a2df7c`:tan:
  Author: Jessica Developer <jess@gmail.com>
  Date:   Wed Sep 17 21:17:18 2014 -0700

      Add world

  commit `faa215bd9dd82ce8dca58f3ab3d0ece49d6fb351`:tan:
  Author: Jessica Developer <jess@gmail.com>
  Date:   Wed Sep 17 21:13:02 2014 -0700

      Say hello

.. only:: not revealjs

  As your needs get more sophisticated, ``git log`` has many options, such as 
  only showing recent history, work by one person, work on a single file or directory
  of your project, etc.



.. move to future?

        Revision IDs
        ------------

        Git shows "revision IDs" in ``git log`` output:

        .. parsed-literal::
          :class: console

          commit `faa215bd9dd82ce8dca58f3ab3d0ece49d6fb351`:tan:

        - 40-character long hexidecimal strings

        - Uniquely refer to each version (even across world!)

        - But a bit of a pain to type/remember

        Tagging
        -------

        - A "tag" is a nickname for a particular revision.

          .. only:: not revealjs
         
            You might tag this when you come to a milestone (version 1.0!), or when you
            finish working through our instructions but want to continue on and play on your
            own, or when you show your code to an instructor.

        - Tag names should look like variables:

          - ``version_1``
          - ``finished_exercise``
          - ``showed_to_nick``

        .. newslide::

        To create a tag:

        .. parsed-literal::
          :class: console

          $ `git tag -m "Finished last step in exercise" finished_exercise`:cmd:

        Can list all tags:

        .. parsed-literal::
          :class: console

          $ `git tag -l`:cmd:
          finished_exercise

        .. newslide::

        Can see log with tags with ``--decorate`` option:

        .. parsed-literal::
          :class: console

          $ `git log --decorate`:cmd:
          commit `0fac84fc1ce68fce033ae82528ce7447962639a3`:tan:
            (`HEAD`:cyan:, `tag: finished_exercise,`:tan: `master`:green:)
          Author: Jessica Developer <jess@gmail.com>
          Date:   Thu Sep 18 06:47:31 2014 -0700

              Add world

          commit `14125014ee07f4fe76f048836246690afe6856d4`:tan:
          Author: Jessica Developer <jess@gmail.com>
          Date:   Thu Sep 18 06:47:31 2014 -0700

              Say hello

Reviewing & Reverting
=====================

ARGH!
-----   

We've changed `hello.py`::

  print "Hello"
  print "World"
  Yuck
  
And now we've broken our code:

.. parsed-literal::
  :class: console

  $ `python hello.py`:cmd:
  Hello
  World
  Traceback (most recent call last):
    File "hello.py", line 3, in <module>
      Yuck
  NameError: name 'Yuck' is not defined

What Changed?
-------------

``git diff`` can tell us what's different:

.. parsed-literal::
  :class: console

  $ `git diff`:cmd:
  diff --git a/hello.py b/hello.py
  index 3808fc1..8ef9f2d 100644
  --- a/hello.py
  +++ b/hello.py
  `@@ -1,2 +1,3 @@`:cyan:
   print "Hello"
   print "World"
  `+Yuck`:green:

New lines in `+green`:green:, deleted lines in `-red`:red:.

Just Take Me Back
-----------------

To return to our last revision, use ``git reset``:

.. parsed-literal::
  :class: console

  $ `git reset`:cmd:
  Unstaged changes after reset:
  M	hello.py

... except it won't; we'd lose change to `hello.py`.

``--hard`` options means do this, even if we lose our change:

.. parsed-literal::
  :class: console

  $ `git reset --hard`:cmd:
  HEAD is now at 411455e8 Add world.

.. only:: not revealjs

  You can even go back to earlier versions with ``git reset`` by specifying an earlier
  revision ID or tag--but be warned, you're **losing** history this way! This is useful
  only if you're certain you never want the changes you made after a certain revision.

  To revert to an earlier revision:

  .. parsed-literal::
    :class: console

    $ `git reset --hard finished_exercise`:cmd:

  You can either provide a tag name or a revision ID to return to. **Be careful.**

.. Too advanced?

  Looking Further Back
  --------------------

  We can "checkout" an earlier revision to look at it.

  You must have a "clean" working directory (commit or reset).

  .. newslide::

  Let's change our file::

    print "Hello"
    print "World"
    print "Ok"

  and commit our change:

  .. parsed-literal::
    :class: console

    $ `git commit -a -m "Add Ok"`:cmd:
     [master 411455e8] Add Ok
    1 file changed, 1 insertion(+)

  .. newslide::

  .. jdigraph:: rating
      :revealjs: -Grankdir=LR -Gsize=7,5!
      :jlatex: -Grankdir=LR -Gsize=2.5,2.5

      revision_1
      revision_2 [label="revision_2\nfinished_exercise"]
      revision_3 [label="revision_3\nYOU ARE HERE"]
      revision_1 -> revision_2
      revision_2 -> revision_3

  .. newslide:: The Time Machine

  And now let's look at our code in an earlier revision:

  .. parsed-literal::
    :class: console

    $ `git checkout finished_exercise`:cmd:
    Note: checking out 'b53d1a57'.

    You are in 'detached HEAD' state. You can look around, make 
    experimental changes and commit them, and you can discard any commits 
    you make in this state without impacting any branches by performing 
    another checkout.

    If you want to create a new branch to retain commits you create, you 
    may do so (now or later) by using -b with the checkout command again. 
    Example:

      git checkout -b new_branch_name

    HEAD is now at b53d1a57... Add world.

  .. newslide::

  Where are we?

  .. parsed-literal::
    :class: console

    $ `git status`:cmd:
    `HEAD detached at`:red: finished_exercise
    nothing to commit, working directory clean

  Our file is the earlier version::

    print "Hello"
    print "World"

  .. newslide::

  .. jdigraph:: rating
      :revealjs: -Grankdir=LR -Gsize=7,5!
      :jlatex: -Grankdir=LR -Gsize=2.5,2.5

      revision_1
      revision_2 [label="revision_2\nfinished_exercise\nYOU ARE HERE"]
      revision_3 [label="revision_3"]
      revision_1 -> revision_2
      revision_2 -> revision_3

  .. newslide:: Time Travel

  .. only:: revealjs

    .. image:: back-to-the-future-02.jpg

  .. newslide:: The Space-Time Continuum

  **Don't make any changes**. Just look around.


  If there's stuff you want, copy to clipboard/other folder.

  .. newslide::

  To get back to the future:

  .. parsed-literal::
    :class: console

    $ `git checkout master`:cmd:
    Switched to branch 'master'

  And now we're back::

    print "Hello"
    print "World"
    print "Ok"
  
Recap
=====

What Did We Learn?
------------------

.. container:: item-incremental

  - Git tracks files in "repository"

  - Must initialize with ``git init`` once

  - Add files you want to track with ``git add``

  - When things work or you've done a lot of work, commit

    - Don't be a jerk to your future self!

.. newslide::

.. container:: item-incremental

  - ``git status`` shows status of working directory

  - ``git log`` shows what you've committed

  - ``git diff`` shows changes since you committed

  - You can compare to/revert back to last revision


.. only:: not revealjs

  Commands
  --------

  You can try this out, from top to bottom, with these commands::

    # Make a directory and go into it
    cd /tmp
    mkdir play
    cd play

    # Turn into a git repository
    git init

    # Add a file with one line
    echo 'print "Hello"' > hello.py

    # See that git knows it's untracked
    git status

    # Tell git to track it
    git add hello.py

    # Commit our change and see that it's committed
    git commit -a -m "Say hello"
    git status
    git log

    # Add a second line to it
    echo 'print "World"' >> hello.py

    # See that git knows it changed
    git status

    # Commit change and see that git tracked that
    git commit -a -m "Add world"
    git log

    # Add a third, bad line to our program; see that it breaks things
    echo 'Yuck' >> hello.py
    python hello.py

    # What changed?
    git diff

    # Try to reset
    git reset

    # Add the "--hard" option to say it's ok to lose our "Yuck" line
    git reset --hard

.. too-advanced

  # Add a tag nicknaming this revision
  git tag -m "Finished instructions" finished_exercise

  # List all tags
  git tag -l

  # Show the log with tags
  git log --decorate

  # Add a new, good line to our file and commit it
  echo 'print "Ok"' >> hello.py
  git commit -a -m "Add ok"

  # Go back in our time machine and look at an earlier revision
  git checkout finished_exercise
  git status

  # Come back to the future
  git checkout master
