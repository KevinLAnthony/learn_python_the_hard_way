# create a mapping of state to abbreviation
states = {
	'Oregon': 'OR',
	'Florida': 'FL',
	'California': 'CA',
	'New York': 'NY',
	'Michigan': 'MI'
}

# create a basic set of states and some cities in them
cities = {
	'CA': 'San Fransisco',
	'MI': 'Detroit',
	'FL': 'Jacksonville'
}

# add some more cities
cities['NY'] = 'New York'
cities['OR'] = 'Portland'

# print out some cities
print('-' * 10)
print("NY State has: ", cities['NY'])
print("OR State has: ", cities['OR'])

# print some states
print('-' * 10)
print("Michigan's abbreviation is: ", states['Michigan']) #states['Michigan'] --> 'MI'
print("Florida's abbreviation is: ", states['Florida'])

# do it by using the state then cities dict
print('-' * 10)
print("Michigan has: ", cities[states['Michigan']]) #cities[states['Michigan']] --> cities['MI'] --> 'Detroit'
print("Florida has: ", cities[states['Florida']])

# print every state abbreviation
print('-' * 10)
for state, abbrev in list(states.items()): #local variables created here and correspond to items in list due to positioning
	print(f"{state} is abbreviated {abbrev}") #{local variable} {local variable}

# print every city in state
print('-' * 10)
for abbrev, city in list(cities.items()): 
	print(f"{abbrev} has the city {city}")

# now do both at the same time
print('-' * 10)
for state, abbrev in list(states.items()): #same as line 38
	print(f"{state} state is abbreviated {abbrev}") #same as line 39 
	print(f"and has city {cities[abbrev]}") #{global variable[local variable]} --> e.g.: cities['OR']

print('-' * 10)
# safely get an abbreviation by state that might not be there
state = states.get('Texas')

if not state:
	print("Sorry, no Texas.")

# get a city with a default value
city = cities.get('TX', 'Does Not Exist') #passing the two parameters in in the order they would appear in the cities list if they existed. Does Not Exist is essentially the name of the city due to positioning.
print(f"The city for the state 'TX' is: {city}") 
