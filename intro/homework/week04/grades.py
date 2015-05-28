# GOAL: Use the number grades from class_grades.txt to calculate a letter grade for each person in the class.
a = []
b = []
c = []
d = []
f = []

# open the class_grades.txt file
grade_file = open("class_grades.txt")

# read the file (assign to variables)
grade_list = grade_file.readlines()

# close the file
grade_file.close()

# GOAL: assign letter grades

# go through the list item by item
for grade in grade_list:
	
	# Convert the grade from a string to an integer
	grade = int(grade)

	# based on the grade percentage, add the grade to the associated letter list
	if(grade >= 90):
		a.append(grade)
	elif(grade >= 80):
		b.append(grade)
	elif(grade >= 70):
		c.append(grade)
	elif(grade >= 60):
		d.append(grade)
	else:
		f.append(grade)

print "The A(s) are", a
print "The B(s) are", b
print "The C(s) are", c
print "The D(s) are", d
print "The F(s) are", f

