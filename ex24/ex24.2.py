print("Let's practice everything.")
#the \ character is ignored, and you can use apostrophes and quotation marks as part of the quote
#without confusing the machine
print('You\'d need to know \'bout escapes with \\ that do:')
print('\n newlines and \t tabs.')

poem = """
\tThe lovely world
with logic so firmly planted
cannot discern \n the needs of love
nor comprehend passion from intuition
and requires an explanation
\n\t\twhere there is none.
"""

print("------------")
print(poem)
print("------------")


five = 10 - 2 + 3 - 6
print(f"This should be five: {five}")

def secret_formula(started):
	jelly_beans = started * 500
	jars = jelly_beans / 1000
	crates = jars / 100
	return jelly_beans, jars, crates


start_point = 10000
#the three global variables "beans," "jars," and "crates" correspond to the return values 
#of the three local variables "jelly_beans," "jars," and "crates" within the secret_formula function
#they correspond because of their placement, not their names.
beans, jars, crates = secret_formula(start_point)

# AUTHOR'S NOTE: remember that this is another way to format a string
#I guess you have to put the ".format()" part to use the variable along with the string.
#Also, removing the "{}" causes the number not to show up in the result.
print("With a starting point of: ".format(start_point))
# AUTHOR'S NOTE: it's just like with an f"" string
print(f"We'd have {beans} beans, {jars} jars, and {crates} crates.")

start_point = start_point / 10

print("We can also do that this way:")
formula = secret_formula(start_point)
# AUTHOR'S NOTE: this is an easy way to apply a list to a format string
#Here, removing the first set of brackets will cause the 5000000.0 figure
#to show up next to jars instead of beans. The number of crates will be incorrect, too.
#This happens because of the placement of the elements. The first element still gets printed but in the wrong place.
print("We'd have  beans, {} jars, and {} crates.".format(*formula))