#import the argv module / library
from sys import argv

#hold arguments in argv module. Also, consider that script and filename are being declared as
#variables and are each being set to the argv module
script, filename = argv

#print message to user
print("Type the filename again:")
#declare variable and set to input function containing message to user
file_again = input("> ")

#declare variable and set it to open the value contained in file_again variable and return a stream
#Here, the value will be taken from a text file whose data will be taken from a text file referenced by 
#the user.
txt_again = open(file_again)

#print the results of reading the value in the txt_again variable via the read function
print(txt_again.read())