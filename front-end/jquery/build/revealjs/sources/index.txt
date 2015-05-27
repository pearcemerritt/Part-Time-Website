.. highlight:: javascript

======
JQuery
======

Simplifying Interactive Web Pages
=================================

Learning Objectives
-------------------

.. container:: item-incremental

  -  I can tell someone what jQuery *is*.

  -  With the help of docs, I can hide an element using jQuery.

  -  With the help of docs, I can schedule an "on click" event using
     jQuery.


What is jQuery?
---------------

.. container:: item-incremental

  - A *set of alternatives* to the built-in JavaScript methods for
    manipulating the DOM in a web page.

  - A library that is extremely popular due to the simplicity it provides.


Review
======

What is a *specific use case* for JavaScript?
---------------------------------------------

Change a CSS class when a user clicks something.

.. container:: one-incremental

  ::

    var myElement = document.getElementById('#my-special-paragraph');

    myElement.addEventListener('click', changeTextColor);


What is a *generalized use case* for JavaScript?
------------------------------------------------

.. container:: one-incremental

  To provide a set of rules that guide the behavior of a webpage.

|
|

.. container:: one-incremental

  - My navigation links should change a color when the user mouses over them.

  - If the user tries to submit an empty form, they should be prompted to fill
    the form correctly.

  - Clicking on an ``<img>`` tag should make the image larger.


New: What is a *specific use case* for jQuery?
----------------------------------------------

.. container:: one-incremental

  Change a CSS class when a user clicks something.


New: What is the *generalized use case* for jQuery?
---------------------------------------------------
.. container:: one-incremental

  To provide a set of rules that guide the behavior of a webpage.

Why JQuery?
===========

JQuery is here to stay
----------------------

.. container:: item-incremental

  - cross-platform

  - lovely syntax

  - it's a marketable skill

  -  58% of the top 10,000 websites use jQuery

  -  source: http://trends.builtwith.com/javascript/jQuery


Something like this in JavaScript...
------------------------------------

Get all links in books and add the class `important`::


    var books = document.getElementsByClass("book");
    for (var i = 0; i < books.length; i++) {
      var links = books[i].getElementsByTagName("a");
      for (var j = 0; j < links.length; j++) {
          links[j].classList.add("important");
      }
    }                            
                            

\...Is much simpler in jQuery
-----------------------------

.. container:: one-incremental
  
  This is also JavaScript
  

::

    $(".book a").addClass("important");


Direct Comparison
-----------------

.. container:: compare
  
  .. code-block:: javascript

    // Plain Javascript

    var books = document.getElementsByClass("book");
    for (var i = 0; i < books.length; i++) {
      var links = books[i].getElementsByTagName("a");
      for (var j = 0; j < links.length; j++) {
          links[j].classList.add("important");
      }
    }

  .. code-block:: javascript

    // JQuery (still JavaScript)

    $(".book a").addClass("important");
                            



Basic jQuery Syntax
===================

Getting an element 
------------------

jQuery element(s) = dollar sign + selector string in parentheses

::

    var allImages = $('img');

    var myBio = $('#bio');


Basic Anatomy of a JQuery expression
------------------------------------

.. image:: anatomy.png

Basic Anatomy of JQuery, cont.
------------------------------

::

  $('#bio').addClass('gray-background');

.. container:: nest-incremental

  - The dollar sign is a shortcut for the function ``jQuery()``.

  - Is there a space after the dollar sign?

    - No!

  - Are there quotes around the selector?

    - Yes! It is a selector *string*.

  - As you learn more CSS selectors, you will also be improving your jQuery
    selector syntax. Woot!


Prevent Confusion Later: Learn the Important Selectors
------------------------------------------------------

.. container:: nest-incremental

  - ``$('.urgent')``

    - select all elements that have the class "urgent"

  - ``$('#bio')``

    - select the *single* element with the id "bio"

  - ``$('div')``

    - select all the divs

  - ``$('div.urgent')``

    - select the div with the class urgent

  - ``$('footer a.fancy')``

    - select all links with the class fancy that are *inside* the footer



An Acronym to Remember JQuery Expressions
-----------------------------------------
**D**\ octor **S**\ mith **D**\ oesn't **M**\ ake **P**\ retty **S**\ nowmen

.. container:: item-incremental

  - Dollar sign

  - Selector

  - Dot

  - Method

  - Parameter

  - Semicolon


.. container:: one-incremental

  .. image:: snowmen.png


jQuery Setup
============

Where does jQuery come from?
----------------------------

.. code-block:: html

    <script src="https://code.jquery.com/jquery.js"></script>

- Always include this line *before* any jQuery code needs to be evaluated

- At Hackbright, please put this inside the ``<head>`` tag

Where does *my* jQuery code go?
-------------------------------

-  Save jQuery code that you write with a ``.js`` file extension.

-  Include another script tag for *your* ``.js``
   file **after** the jQuery script tag

An HTML Doc
-----------

.. code-block:: html

  <!doctype html>
  <html>

    <head>













    </head>

    <body>



    </body>
  </html>

.. newslide::

.. only:: not revealjs

  So that becomes:

.. code-block:: html
  :emphasize-lines: 9, 13, 22

  <!doctype html>
  <html>

    <head>




      <!-- CSS HERE -->



      <!-- JAVASCRIPT HERE -->




    </head>

    <body>

      <!-- HTML HERE -->

    </body>
  </html>


.. newslide::

.. code-block:: html
  :emphasize-lines: 5-16, 22

  <!doctype html>
  <html>

    <head>

      <link rel="stylesheet" href="stylesheet.css">

      <style>
        .fancy { color: pink; display: none; }
       </style>

      <script src="http://code.jquery.com/jquery.js"></script>

    </head>

    <body>

      <div class="fancy">I'm fancy!</div>

      <script>
        $(".fancy").show();
      </script>

    </body>
  </html>


Methods for Changing the DOM
============================

Changing CSS Classes
--------------------

::

    $("section").addClass("important");      // no error if already there

    $("section").hasClass("important");      // returns true or false

    $("section").removeClass("important");   // no error if not there

    $("section").toggleClass("important");


Changing HTML Attributes
------------------------

::

    $("img#cat").attr("src");              // returns src attribute

    $("img#cat").attr("src", "cat.jpg"); // add or change

Inserting HTML Elements
-----------------------


.. code-block:: html

  <div>
    <p>Existing Text.</p>
  </div>


-  the prepend() method adds to the top of the content of the element;
-  the append() method adds to the bottom of the content of the element.


.. code-block:: javascript

    $("p").prepend("Hello ");

    $("p").append(" The End!");
                            

.. newslide::

.. code-block:: html

  <div>
    <p>Existing Text. The End!</p>
  </div>

                            

Changing Contents of Existing HTML Elements
-------------------------------------------

::

    $("section").html();         // returns HTML

    $("section").html("Hi");     // sets HTML


Removing HTML Elements
----------------------

::

    $("section").empty();    // remove children

    $("section").remove();   // remove this element + children
                            

Showing/Hiding Elements
-----------------------

::

    $("img").hide();

    $("img").show();

    $("img").toggle();
                            

Animation Methods
=================

Shrinking and Growing Elements
------------------------------
::

    $("img").slideUp();       // shrink into nothing in position

    $("img").slideDown();     // grow into itself in position

    $("img").slideToggle();   // toggles via sliding
                            

Other Animations
----------------

-  ``fadeIn()``
-  ``fadeOut()``
-  ``fadeToggle()``

.. container:: one-incremental

  -  many many more

Speed of Animation
------------------

::

    $("img").slideUp(3000);      // milliseconds (3 secs)
                            

- The first param is the amount of time the animation should take to
  complete

  -  If you omit, slideUp and slideDown default to 400ms

A note on chaining methods
--------------------------

Is the following jQuery code allowed?

.. code-block:: javascript

  $("img#cat").attr("src", "cat.jpg").attr("height", 500);

                            

Event Listeners
===============

What is an event listener?
--------------------------

.. container:: nest-incremental

  - A list of what will happen when a user interacts with an HTML element 
    (or a group of HTML elements)
  - We as programmers need to specify 

    - the catalyst element
    - the type of event being handled
    - what will happen.


Two Ways to Schedule an On Click Event 
--------------------------------------

.. container:: compare
  
  .. code-block:: javascript

    // click event in Plain JavaScript

    var myBtn = document.getElementById('special-btn');

    myBtn.addEventListener('click', alertMe);

  .. code-block:: javascript

    // click event in JavaScript using JQuery

    $('#special-btn').on('click', alertMe);

.. container:: one-incremental

  My helper function (no JQuery here)::

    function alertMe(evt) {
      alert("Don't click that, please.");
    }


Other event types
-----------------

.. container:: one-incremental

  Just like in JavaScript!

-  mouseover ``$('#special-btn').on('mouseover', alertMe);``
-  change  ``$('input').on('change', alertMe);``
-  submit  ``$('form').on('submit', alertMe);``
-  keypress  ``$('input').on('keypress', alertMe);``

Practice
========

Practice 1
----------

.. code-block:: html

   <img id="cat" src="cat.jpg" alt="A cute kitten">

.. code-block:: css

    .special-border {
        border-color: green;
        border-radius: 4px;
        border-style: solid;
    }

::

    $("#cat").on("mouseover", showBorderOnKitten);

Helper function (there is JQuery here)::
  
  function showBorderOnKitten(evt) {

    $("img#cat").addClass("special-border");
  }
  


Practice 2
----------

::

    $(".trigger-alert").on("change", function (evt) {
        alert("Don't do that, please."); 
      }
    );


In Conclusion
=============

How to debug jQuery
-------------------

-  Check the order of your script tags

-  Check your syntax

-  Read the jQuery docs on the thing you're trying to do

Coming Up
---------

-exercise time!


FIN
===


