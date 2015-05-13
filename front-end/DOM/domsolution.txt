# Add div element to the DOM
var div_element = document.createElement("div")
document.body.appendChild(div_element)

# Create header element
var header_element = document.createElement("h1")

# Create text node (text for the header element)
var text = document.createTextNode("Calculate All the Things!")

# Append the text to the header
header_element.appendChild(text)

# Append the header to the div element
div_element.appendChild(header_element)

# Create a table element and give it the id of calculator
var calc_table_element = document.createElement("table")
calc_table_element.id = "calculator"

# Append table element to the DOM
div_element.appendChild(calc_table_element)

# Create three rows of the "calculator" table
var table_first_row = document.createElement("tr")
var table_second_row = document.createElement("tr")
var table_third_row = document.createElement("tr")

# Create 12 cells of the "calculator" table & add their text
var table_cell_1 = document.createElement("td")
table_cell_1.innerText = "1"

var table_cell_2 = document.createElement("td")
table_cell_2.innerText = "2"

var table_cell_3 = document.createElement("td")
table_cell_3.innerText = "3"

var table_cell_4 = document.createElement("td")
table_cell_4.innerText = "4"

var table_cell_5 = document.createElement("td")
table_cell_5.innerText = "5"

var table_cell_6 = document.createElement("td")
table_cell_6.innerText = "6"

var table_cell_7 = document.createElement("td")
table_cell_7.innerText = "7"

var table_cell_8 = document.createElement("td")
table_cell_8.innerText = "8"

var table_cell_9 = document.createElement("td")
table_cell_9.innerText = "9"

var table_cell_plus = document.createElement("td")
table_cell_plus.innerText = "+"

var table_cell_minus = document.createElement("td")
table_cell_minus.innerText = "-"

var table_cell_equals = document.createElement("td")
table_cell_equals.innerText = "="


# Append first table row to the "calculator" table
calc_table_element.appendChild(table_first_row)

# Append the first 4 cells to the "calculator" table's first row
calc_table_element.lastChild.appendChild(table_cell_1)
calc_table_element.lastChild.appendChild(table_cell_2)
calc_table_element.lastChild.appendChild(table_cell_3)
calc_table_element.lastChild.appendChild(table_cell_plus)

# Append the second table row to the "calculator" table
calc_table_element.appendChild(table_second_row)

# Append the next 4 cells to the "calculator" table's second row
calc_table_element.lastChild.appendChild(table_cell_4)
calc_table_element.lastChild.appendChild(table_cell_5)
calc_table_element.lastChild.appendChild(table_cell_6)
calc_table_element.lastChild.appendChild(table_cell_minus)

# Append the third table row to the "calculator" table
calc_table_element.appendChild(table_third_row)

# Append the last 4 cells to the "calculator" table's last row
calc_table_element.lastChild.appendChild(table_cell_7)
calc_table_element.lastChild.appendChild(table_cell_8)
calc_table_element.lastChild.appendChild(table_cell_9)
calc_table_element.lastChild.appendChild(table_cell_equals)

# Create the "solution_bar" table, it's table row, & it's table cell
var solution_table_element = document.createElement("table")
solution_table_element.id = "solution_bar"
var solutions_table_row = document.createElement("tr")
var solutions_table_cell = document.createElement("td")

# Append the "solution_bar" table to the div_element
div_element.appendChild(solution_table_element)

# Append the row to the "solution_bar" table
solution_table_element.appendChild(solutions_table_row)

# Append the cell to the "solution_bar" table's row
solution_table_element.lastChild.appendChild(solutions_table_cell)