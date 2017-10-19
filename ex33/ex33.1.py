#i = 0  --> has to be inside function. Won't work otherwise.
numbers = []

def looper(iteration_stop):
	i = 0
	while i < iteration_stop:
		print(f"At the top, i is {i}")
		numbers.append(i)

		i = i + 1
		print("Numbers now: ", numbers)
		print(f"At the bottom, i is {i}")

looper(6)

print("The numbers: ")

for num in numbers:
	print(num)