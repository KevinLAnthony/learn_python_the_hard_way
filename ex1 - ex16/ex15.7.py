#import the argv module / library
from sys import argv

#hold arguments in argv module. Also, consider that script and filename are being declared as
#variables and are each being set to the argv module
script, filename = argv

#declare txt variable and set it to an open function that opens file (either a text or bytestring)
#Here, the filename variable represents a parameter. According to what we see when we run pydoc -m open, the open
#function does this: "Open file and return a stream"
txt = open(filename)

#print message with formatting via the f character. Also, include the filename variable (parameter) so that the
#name of the text file we're referencing in the "script, filename = argv" statement is printed.
print(f"Here's your file {filename}:")
#print the results of reading the txt file via the read function
print(txt.read())

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

txt.close()
txt_again.close()