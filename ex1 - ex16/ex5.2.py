name = 'Zed A. Shaw'
age = 35 # not a lie
height = 74 # inches
weight = 180 # lbs
eyes = 'Blue'
teeth = 'White'
hair = 'Brown'

height_centimeters = height * 2.54
weight_kg = weight / 2.2

print(f"Let's talk about {name}.")
print(f"He's {height} inches tall.")
print(f"He's {weight} pounds heavy.")
print("Actually, that's not too heavy.")
print(f"He's got {eyes} eyes and {hair} hair.")
print(f"His teeth are usually {teeth} depending on the coffee.")

# this line is tricky, try to get it right
total = age + height + weight
print(f"If I add {age}, {height}, and {weight}, I get {total}.")

print(f"The height in centimeters is {height_centimeters}.")
print(f"The weight in kilograms is {weight_kg}.")