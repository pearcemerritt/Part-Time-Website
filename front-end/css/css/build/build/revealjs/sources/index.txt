.. highlight:: css

===
CSS
===

.. TODO

  show off Chrome CSS debugging

Cascading Style Sheets
======================

Our Goals
---------

- Learn enough CSS to make things look rad
- Learn about the three parts of a CSS rule
- Learn about the flow of the document


Separating Content from Presentation
------------------------------------

.. only:: not revealjs

  Writing HTML was horrible before CSS because you couldn't separate your
  content from your presentation.

OLD SCHOOL:

.. code-block:: html

  <p>
    <font color="red">
      In the old days, this is how we made text in each paragraph red.
    </font>
  </p>

.. container:: one-incremental

  BUT NOW...

  .. code-block:: css

      p {
         color: red;
      }

  .. code-block:: html

      <p>
        all paragraphs are now red!
      </p>


Some Simple Syntax
------------------

CSS is made up of ``selectors``, ``properties``, and ``values``.

.. code-block:: css

    selector {
       property: value;
    }

.. container:: one-incremental

  In this example, we're *selecting* all ``<p>`` elements
  and styling them.

  .. code-block:: css

      p {
         color: red;
      }

.. only:: not revealjs

  In CSS, comments are delineated by ``/*`` and ``*/``, like this::

    p {
        color: red;   /* our brand color */
    }

Where Things Go
===============

Inline Style
------------

.. code-block:: html

  <p style="color:red;">
    this paragraph has inline styling applied to it.
  </p>


Internal Style Rules
--------------------

.. code-block:: html

  <html>
    <head>
        <style>

          /* CSS goes here */

        </style>
    </head>
    <body>

      <!-- HTML goes here -->
        
    </body>
  </html>


.. TODO

  Tip
  ---

  Dont mix <style> and <link>

.. TODO place this somewhere

  Styles on Styles
  ----------------

  .. code-block:: css

    p  { color: red }
    p.urgent { background-colro: blue; }

  .. code-block:: html

    <p class=urgent>i am red on blue</p>


External Style Rules
--------------------

If we make a css file called `style.css`:

.. code-block:: css

  /* style.css */

  selector {
       property: value;
    }

  selector {
       property: value;
       another-property: value;
    }

  ...


.. newslide:: 

We can then ``link`` to it in our ``html``...

.. code-block:: html

  <html>
    <head>

      <link rel="stylesheet" href="./style.css">

    </head>
    <body>

      ... 

    </body>
  </html>

Specificity
-----------

.. code-block:: css

  p { color: blue }
       .urgent { color: red }
       p#form-error-message { color: green; }

       p#form-error-message { color: green; }
  p { color: blue }
       .urgent { color: red }


Selectors
=========

Selectors
---------

.. parsed-literal::

    `selector`:red: {
       property: value;
    }

Elements as Selectors
---------------------

Use an ``element`` if you want to target all elements of a certain type.

.. code-block:: css

  h1 {
     font-family: sans-serif;
  }


Ids as Selectors
----------------

Use an ``#id`` if you want to selectively target one element.

.. code-block:: css

  #notice {
     font-family: monospace;
  }


Classes as Selectors
--------------------

Use a ``.class`` if you want to selectively target several elements.

.. code-block:: css

  .urgent {
     color: red;
     font-weight: bold;
  }


Block Elements
--------------

- start on a new line
- take up the whole width of their containing element

.. image:: block.png


Examples
--------

.. container:: nest-incremental

  - paragraphs (``<p>``)
  - headers (``h1``, ``h2``, etc.)
  - items in a list (``<li>``).
  - **[NEW]** the ``<div>`` element.



Inline Elements
---------------

- sit on a line together
- don't break the flow of your document

.. image:: inline.png


Examples
--------

.. container:: nest-incremental

  - hyperlinks (``<a>``)
  - emphasized text (``<em>``)
  - **[NEW]** the ``<span>`` element.


``div`` and ``span``
--------------------


.. container:: nest-incremental

  - ``div`` is a general purpose ``block`` element

  - ``span`` is a general purpose ``inline`` element

.. container:: one-incremental

  What do we mean by *general purpose*?

.. only:: not revealjs

  The ``div`` and ``span`` tags should be used to indicate ``block`` and ``inline`` elements that can't be described using the other HTML tags.

                
In Practice
-----------

.. code-block:: html

  <div id="notice"> How are you, gentlemen? 
    <span class="urgent"> All your base are belong to us.</span>
    You are on the way to destruction.
    You have no chance to survive 
    <span class="urgent"> make your time.</span>
    Ha Ha Ha Ha ...
  </div>

Combining Selectors
-------------------

.. container:: compare

    .. code-block:: html

      <div class="urgent">
        This is an urgent block of text!
      </div>

      <p>
        And this is a regular paragraph that has an
        <span class="urgent">urgent</span>
        section within it.
      </p>

    .. code-block:: css


      /* select divs that have the urgent class */

      div.urgent {
        color: white;
        background-color: red;
      }

      /* select all elements with the urgent class
         that are within a paragraph */

      p .urgent {
        color: red;
        font-weight: bold;
      }


Properties
==========

Properties
----------

.. parsed-literal::

  selector {
     `property`:red: : value;
  }

General Properties
------------------

- margin
- padding
- border


Block Properties
----------------

- width
- height
- float


Inline/Text Properties
----------------------

- text-align
- text-decoration
- text-transformation
- line-height
- vertical-align


Font Properties
---------------

- color
- font-family
- font-size
- font-style
- font-weight


Background Properties
---------------------

- background-color
- background-image
- background-repeat
- background-position


List and Link Properties
------------------------

- list-style-type (lists)
- text-decoration (links)


Values
======

Values
------

.. parsed-literal::

    selector {
       property: `value`:red:;
    }


Keyword Values
--------------

.. only:: not revealjs

  Many CSS properties take one or more of a fixed set of keywords. For example,
  ``text-align`` takes a keyword of `left`, `right`, or `center` (the default):

.. code-block:: css

  p {
    text-align: left;
    text-align: right;
    text-align: center;
  }



Notes about Numeric Units
-------------------------

Zero values shouldn't have a unit:

.. code-block:: css

  body {
    margin: 0px;       /* bad!  */
    margin: 0;         /* good! */
  }

Decimal values should have a leading zero:

.. code-block:: css

  footer {
    font-size: .75em;   /* bad!  */
    font-size: 0.75em;  /* good! */
  }

.. only:: not revealjs

  This isn't required by the specification, but is considered very
  good style, as it's easy to misread ``.75em`` as ``75em``, and
  the leading zero makes it much harder to misread.

Functional Values
-----------------

.. code-block:: css

    body {
       background-image: url("static/img/bg-image.jpg");
    }


Color Values
------------

Referencing colors can be done in three primary ways: color name,
hex value, and red-green-blue value.

.. code-block:: css

    p {
       color: red;            /* or */
       color: #ff0000;        /* or */
       color: rgb(255, 0, 0);
    }

.. only:: not revealjs

  Hex values are typically 6 hex (``0-9``, ``a-f``) digits.
  There first 2 digits say how much red is in a color; the second
  how much green; the third, how much blue.

  Hex values can also be given with only three digits, like ``#abc``,
  which always means the same things as ``#aabbcc``.

.. note:: **Transparency**

  You can also learn about the ``rgba()`` method of specifying a color,
  where you can provide an "alpha" channel value that shows how
  opaque or transparent the color is.

The Anatomy of a Block Element
------------------------------

Block elements have some attributes that are applied to all four sides:

- margin
- padding
- border

.. image:: box.png

.. newslide:: 

.. code-block:: css

  div {

    margin: 20px;               /* all have 20px margin */

    margin: 75px 50px;          /* top/bottom=75px, right/left=50px */

    margin: 5px 3em 20% 23pt;   /* top -> right -> bottom -> left  */

    margin-left: 30px;          /* the left margin is 30px  */

  }

.. only:: not revealjs

  A good mneumonic for the order of top |rarr| right |rarr| bottom |rarr| left in
  things like this is "trouble" for TRBL. Others may find it easy to remember as
  "start at the top and go clockwise."

Displays: Block and Inline
--------------------------

display: block
  the default display value for block elements

display: inline
  the default display value for inline elements

display: inline-block
  display as a block element that will flow with the surrounding content


These properties can be used to manipulate the display of a webpage.

.. TODO
  some kind of graphic showing difference between different displays

.. DEMO

      

Centering Things
----------------

There are two helpful ways of centering objects.

.. code-block:: css

    h1 {
       text-align: center;
    }

.. only:: not revealjs

  This centers the text within the ``h1`` element.

::

    div {
       margin: 0 auto;
       width: 600px;
    }              

.. only:: not revealjs

  This center the ``div`` itself; text within that it would still
  be left-justified within the ``div``.

                   
**Centering block elements requires that you specify their width.**


Floating
--------

the ``float`` property and text wrapping:

.. code-block:: css

    img {
       float: left;
    }

.. only:: not revealjs

  "The float CSS property specifies that an element should be taken from the normal flow and placed along the left or right side of its container, where text and inline elements will wrap around it." -- Mozilla Developer Network
     
.. DEMO         

Separate CSS Files
==================

Linking
-------

We have a lot of css in our ``<style>`` element.

Let's move it to a dedicated css file & link to it instead.

.. DEMO

Looking Ahead
=============

Coming Up
---------

DOM Manipulation.

Resources!
----------

-  `Head First HTML and CSS
   [book] <http://shop.oreilly.com/product/9780596159924.do>`__
-  `Delightful CSS selectors game [fun] <https://flukeout.github.io/>`__
-  `The 30 CSS Selectors You Must Memorize
   [article] <http://code.tutsplus.com/tutorials/the-30-css-selectors-you-must-memorize--net-16048>`__

