HTML: Forms
===========

Make a simple order form using tables and forms and submit it to a server.

Your goal is to make something that looks like the screenshot below.
An example can also be viewed here: `Ubermelon Order Form`_

.. _`Ubermelon Order Form`: https://ubermelon-order-form.herokuapp.com/

You can open a file in Chrome by using `File > Open` and navigating to your `form.html`,
which you should put in ~/src/html-forms/.

Specifications
--------------

Header
++++++

The header should have a title: "Ubermelon Order Form"

Body
++++

h1 element
^^^^^^^^^^

The command "Order!" is in an h1 tag.

Table
^^^^^

-  The table has two header columns, "Melon Name" and "Price per lb".
-  The names and prices of the melons are in the screenshot

Text
^^^^

The "Place your orders here! You know you want to." is in a paragraph.

Form
^^^^

-  First Name is a text input, with a name of "firstname"
-  Last Name is a text input, with a name of "lastname"
-  Use the correct accessibility syntax for the text inputs, with a
   "label for" and "id" (or enclose the input in the label, which is
   equally good for accessibility)
-  Melon Type is a dropdown with name "melontype"
-  The types of melons are: watermelon, honeydew, canteloupe, crenshaw,
   canary
-  Quantity is a text input with name of "quantity"
-  Delivery Time is a radio button with name "time"
-  Delivery Time has values of "am", "pm", and "wat"
-  Returning Customer is a radio button and values of "yes" and "no"
-  Statistics is a checkbox with name "stats" and values of "Dog",
   "Cat", "Hedgehog", "Balloonicorn", and "Yak"
-  The submit button is of type "submit"
-  The form action should go to:
   `https://ubermelon-order-form.herokuapp.com/process`
-  You can use either a `GET` or `POST` request. Try them both!

Footer
^^^^^^

The disclaimer about the quantities is in a footer tag.

Screenshot
----------

.. image:: form.png

**STOP. Please ask for a code review.**

If you finish this and there is time, please see `Further Study <further-study.html>`_.