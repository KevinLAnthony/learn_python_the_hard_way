#declare and instantiate string variable
formatter = "{} {} {} {}"

#print integers by passing them as arguments to the format function of the formatter variable
print(formatter.format(1, 2, 3, 4))
#print strings by passing them as arguments to the format function of the formatter variable
print(formatter.format("one", "two", "three", "four"))
#print booleans by them as arguments to the format function of the formatter variable
print(formatter.format(True, False, False, True))
#print the formatter string variable by passing it as arguments to the format function of the formatter variable
print(formatter.format(formatter, formatter, formatter, formatter))
#print strings by passing them as arguments to the format function of the formatter variable
print(formatter.format(
	"Try your",
	"Own text here",
	"Maybe a poem",
	"Or a song about fear"
))