#declare and instantiate variable
cars = 100
#declare and instantiate variable
space_in_a_car = 4.0
#declare and instantiate variable
drivers = 30
#declare and instantiate variable
passengers = 90
#declare and instantiate variable
cars_not_driven = cars - drivers
#declare and instantiate variable
cars_driven = drivers
#declare and instantiate variable
carpool_capacity = cars_driven * space_in_a_car
#declare and instantiate variable
average_passengers_per_car = passengers / cars_driven


#print a string, a variable, and another string
print("There are", cars, "cars available.")
#print a string, a variable, and another string
print("There are only", drivers, "drivers available.")
#print a string, a variable, and another string
print("There will be", cars_not_driven, "empty cars today.")
#print a string, a variable, and another string
print("We can transport", carpool_capacity, "people today.")
#print a string, a variable, and another string
print("We have", passengers, "to carpool today.")
#print a string, a variable, and another string
print("We need to put about", average_passengers_per_car, "in each car.")
