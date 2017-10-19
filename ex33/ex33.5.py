#i = 0  --> has to be inside function. Won't work otherwise.
numbers = []

def looper(iteration_stop):
	i = 0
	#numbers = list(range(i, iteration_stop)) --> using this line instead of a for-loop creates a different
	# numbers list, which only exists inside the function. The numbers list created at the top of the script
	# is still empty and doesn't print any numbers when the for loop at the bottom of the script is run.

	for i in range(0, 6):
		print(f"Adding {i} to the list.")
		# append is a function that lists understand
		numbers.append(i)

	for i in numbers:
		print("Numbers now: ", numbers)
		print(f"At the bottom, i was: {i}")


looper(6)

print("The numbers: ")

for num in numbers:
	print(num)