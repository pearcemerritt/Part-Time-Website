import turtle

HORIZ_LINE_TOP = (-150,50)
HORIZ_LINE_BOTTOM = (-150,-50)
VERT_LINE_LEFT = (-50,-150)
VERT_LINE_RIGHT = (50,-150)

turtle.setup(500,500)	# set the window size to 500 by 500 pixels
wn = turtle.Screen()
rachel = turtle.Turtle()

rachel.pensize(3)
rachel.pencolor("#00bfff")

rachel.penup()
rachel.setposition(VERT_LINE_LEFT)


rachel.pendown()
rachel.left(90)
rachel.forward(300)
rachel.penup()

rachel.setposition(VERT_LINE_RIGHT)
rachel.pendown()
rachel.forward(300)
rachel.penup()

rachel.setposition(HORIZ_LINE_BOTTOM)
rachel.pendown()
rachel.right(90)
rachel.forward(300)
rachel.penup()

rachel.setposition(HORIZ_LINE_TOP)
rachel.pendown()
rachel.forward(300)
rachel.penup()

def draw_symbol(x,y):
	print "x:",x, "y:",y
	if(-150 <= x <= -50 and 50 <= y <= 150):	# Square 1
		draw_x(-150,150)
	elif(-50 <= x <= 50 and 50 <= y <= 150):	# Square 2
		pass
	elif(50 <= x <= 150 and 50 <= y <= 150):	# Square 3
		pass
	elif(-150 <= x <= -50 and -50 <= y <= 50):	# Square 4
		pass
	elif(-50 <= x <= 50 and -50 <= y <= 50):	# Square 5
		pass
	elif(50 <= x <= 150 and -50 <= y <= 50):	# Square 6
		pass
	elif(-150 <= x <= -50 and -150 <= y <= -50):	# Square 7
		pass
	elif(-50 <= x <= 50 and -150 <= y <= -50):	# Square 8
		pass
	elif(50 <= x <= 150 and -150 <= y <= -50):	# Square 9
		pass
	else:
		exit()

def draw_x(x,y):
	# TODO: Make sure turtle is facing right
	rachel.pencolor("red")
	rachel.penup()
	rachel.setpos(x+5,y-5)
	rachel.right(45)
	rachel.pendown()
	rachel.forward(100)
	rachel.penup()
	rachel.setposition(x+95,y-5)
	rachel.right(90)
	rachel.pendown()
	rachel.forward(100)



turtle.onscreenclick(draw_symbol)

turtle.mainloop()	# Wait for user to close window
# wn.exitonclick()	# Wait for user to click before closing window