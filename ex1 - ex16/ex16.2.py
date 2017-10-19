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

txt.close()