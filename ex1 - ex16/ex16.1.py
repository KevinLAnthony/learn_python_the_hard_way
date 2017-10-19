from sys import argv

#declare script and filename variables and assign the value of argv
script, filename = argv

#print filename variable
print(f"We're going to erase {filename}.")
#print choices for user
print("If you don't want that, hit CTRL-C (^C).")
print("If you do want that, hit RETURN.")

#print message to user, and allow user to respond by typing
input("?")

#print message to user 
print("Opening the file...")
#declare file object called target and open the filename variable within it. Write to the file with 'w'
target = open(filename, 'w')

#print message to user
print("Truncating the file.  Goodbye!")
#use truncate function on target object
target.truncate()

#print message to user
print("Now I'm going to ask you for three lines.")

#print message to user, and allow user to respond by typing
line1 = input("line 1: ")
line2 = input("line 2: ")
line3 = input("line 3: ")

#print message
print("I'm goinng to write these to the file.")

#write user input to target object for that line and go to next line
target.write(line1)
target.write("\n")
#write user input to target object for that line and go to next line
target.write(line2)
target.write("\n")
#write user input to target object for that line and go to next line
target.write(line3)
target.write("\n")

#print message
print("And finally, we close it.")
#close target object
target.close()