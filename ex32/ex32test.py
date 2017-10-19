the_count = [1, 2, 3, 4, 5]
fruits = ['apples', 'oranges', 'pears', 'apricots']
change = [1, 'pennies', 2, 'dimes', 3, 'quarters']

# this first kind of for-loop goes through a list
# I changed the "number" variable to "i". Result is the same, b/c just another way of naming the variable.
for i in the_count:
	print(f"This is count {i}")

# same as above
for fruit in fruits:
	print(f"A fruit of type: {fruit}")

# also we can go through mixed lists too
# notice we have to use {} since we don't know what's left in it
for i in change:
	print(f"I got {i}")

# we can also build lists, first start with an empty one
elements = []

# then use the range function to do 0 to 5 counts
for i in range(0, 6):
	print(f"Adding {i} to the list.")
	# append is a function that lists understand
	elements.append(i)

# now we can print them out too
for i in elements:
	print(f"Element was: {i}")