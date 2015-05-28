def find_average(num1, num2, num3):
	if(type(num1)==str or type(num2)==str or type(num3)==str):
		return "Sorry, the input(s) are invalid."
	else:
		return (num1+num2+num3)/3.0

print find_average(3,4,4)
print find_average(1,2,3)
print find_average("6", 8, 7)
print find_average(2, 9, "hi")