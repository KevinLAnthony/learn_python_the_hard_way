# declare and instantiate integer variable
types_of_people = 10
# declare and instantiate string variable that contains integer variable in it
x = f"There are {types_of_people} types of people."

# declare and instantiate string variable
binary = "binary"
# declare and instantiate string variable
do_not = "don't"
# declare and instantiate string variables containing string variables in it
y = f"Those who know {binary} and those who {do_not}." ### HERE 1,2

# print string variable containing integer variable
print(x)
# print string variable containing string variables
print(y)

# print string variable containing integer variable along with additional text
print(f"I said: {x}") ### HERE 3
# print string variable containing string variables along with additional text. Show original string variable in single quotes.
print(f"I also said '{y}'") ### HERE 4

# declare and instantiate boolean variable
hilarious = False
# declare and instantiate string variable containing boolean variable
joke_evaluation = "Isn't that joke so funny?! {}"

# print string variable containing boolean variable. Use format() method to print boolean variable.
print(joke_evaluation.format(hilarious))

# declare and instantiate string variable
w = "This is the left side of..."
# declare and instantiate string variable
e = "a string with a right side."

# print string variables
print(w + e)