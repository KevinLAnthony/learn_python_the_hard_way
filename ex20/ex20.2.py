#import the argv module / library
from sys import argv

#hold arguments in argv module. Also, consider that script and filename are being declared as
#variables and are each being set to the argv module
script, input_file = argv

#create function and add parameter(s). 
def print_all(f):
#run print() function using value from parameter from overall containing function 
#and run read() function on parameter
	print(f.read())

#create function and add parameter(s). 
def rewind(f):
#run seek() function on parameter from overall containing function. Add a parameter to seek() function.
	f.seek(0)

#create function and add parameter(s). 
def print_a_line(line_count, f):
#run print() function using values from both parameters from overall containing function 
#and run readline() function on one of those parameters
	print(line_count, f.readline())

#declare object and set it equal to open() function containing variable set to argv module
current_file = open(input_file)

#print message
print("First let's print the whole file:\n")

#print value contained in object
print_all(current_file)

#print message
print("Now let's rewind, kind of like a tape.")

#run rewind function using valued contained within object
rewind(current_file)

#print message
print("Let's print three lines:")

#declare variable and give it a value
current_line = 1
#run print_a_line function using value contained within current_line variable and current_file object
print_a_line(current_line, current_file) # current_line = 1

#increment current_line variable by one
current_line = current_line + 1
#run print_a_line function using value contained within current_line variable and current_file object
print_a_line(current_line, current_file) # current_line = 2

#increment current_line variable by one
current_line = current_line + 1
#run print_a_line function using value contained within current_line variable and current_file object
print_a_line(current_line, current_file) # current_line = 3