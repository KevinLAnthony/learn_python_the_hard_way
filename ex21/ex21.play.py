def add(a, b):
	print(f"ADDING {a} + {b}")
	return a + b

def subtract(a, b):
	print(f"SUBTRACTING {a} - {b}")
	return a - b

def multiply(a, b):
	print(f"MULTIPLYING {a} * {b}")
	return a * b

def divide(a, b):
	print(f"DIVIDING {a} / {b}")
	return a / b


print("Let's do some math with just functions!")

"""age = add(30, 5)
height = subtract(78, 4)
weight = multiply(90, 2)"""
iq = divide(100, 2)
iq # does not print ***** see below
 
#print(f"Age: {age}, Height: {height}, Weight: {weight}, IQ: {iq}")


# A puzzle for the extra credit, type it in anyway.
#print("Here is a puzzle.")

# just typing "iq" doesn't print "DIVIDING 100 / 2 ". Have to use to provide the "divide" function by name. ***** see above
#what = add(age, subtract(height, multiply(weight, divide(iq, 2))))

#print("That becomes: ", what, "Can you do it by hand?")

what2 = add(age, subtract(height, multiply(weight, divide(iq2(200, 4), 2))))