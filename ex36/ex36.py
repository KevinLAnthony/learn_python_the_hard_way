from sys import exit

def die(cause_of_death):
	print(cause_of_death)
	print("RIP")
	exit(0)


print("You are at a fork on a trail in the woods with paths leading to the left and right.")
print("You want to reach the castle, which is many miles away to the north over very rough terrain.")


def begin():
	print("Which path do you take?")
	print("Answer \"l\" for \"left\" or \"r\" for \"right\".")

	decision = None

	while decision not in ("l", "r"): 

		decision = input("> ")

		if decision == "l":
			river_south_1()
		elif decision == "r":
			mountain()
		else:
			print("Please answer \"l\" for \"left\" or \"r\" for \"right\".")


def river_south_1():
	print("You come to an old, high, rickety bridge with a raging river far below it.")
	print("Which path do you take?")
	print("Answer \"1\" to cross the high, rickety bridge.")
	print("Answer \"2\" to swim across the strong, swirling, wide river.")
	print("Answer \"3\" to turn and go back the way you came.")

	decision = None

	while decision not in ("1", "2", "3"): 

		decision = input("> ")

		if decision == "1":
			bridge()
		elif decision == "2":
			river_north()
		elif decision == "3":
			begin()
		else: 
			print("Please answer \"1\" to cross the bridge, \"2\" to swim across the river or " +
				 "\"3\" to turn back.")

def bridge():
	print("You start to make your way about half-way across the rickety bridge when the" + 
		  " ropes break, plunging you into the river below.")
	print("Do you...")
	print("\"1\" Swim against the current?")
	print("\"2\" Swim with the current?")
	print("\"3\" Swim forward toward the side of the river you were trying to reach?")
	print("\"4\" Swim back toward the side of the river from which you came?")

	#Could add a random variable and conditions here to determine if you make it across bridge
	#or not

	decision = None

	while decision not in ("1", "2", "3", "4"): 

		decision = input("> ")

		if decision == "1":
			die("You tire yourself out and drown.")
		elif decision == "2":
			die("You swim down river but can't stop in time before being swept up by the current" +
				", plummeting down a waterfall, and smashing against the giant boulders below.")
		elif decision == "3":
			river_north()
		elif decision == "4":
			river_south_2()
		else: 
			print("Please answer \"1\" to swim against the current, \"2\" to swim with the current," +
				  " \"3\" to swim forward, or \"4\" to swim back.")


def river_south_2():
	print("The bridge is out, so you're again faced with swimming north across the river " +
		  "south on the trail through the woods.")
	print("Do you...")
	print("\"1\" Swim north across the strong, swirling, wide river?")
	print("\"2\" Go back south on the trail in the woods " + 
		  " and in the wrong direction of the castle?")

	decision = None

	while decision not in ("1", "2"): 

		decision = input("> ")

		if decision == "1":
			river_north("You make your way across the river unscathed.")
		elif decision == "2":
			begin()
		else: 
			print("Please answer \"1\" to swim across the river or \"2\" to go back through the woods " + 
				  "and away from the castle.")


def river_north(status):
	print(status)
	print("Do you...")
	print("\"1\" Keep going along the trail?")
	print("\"2\" Swim back across the river?")

	decision = None

	while decision not in ("1", "2"): 

		decision = input("> ")

		if decision == "1":
			bees()
		elif decision == "2":
			river_south_2()
		else: 
			print("Please answer \"1\" to keep moving or \"2\" to swim back across the river.")


def bees():
	print("You continue into the woods on the trail toward the castle. " +
		  " and encounter a swarm of killer bees right in your path.")
	print("Do you...")
	print("\"1\" Run back south toward the river?")
	print("\"2\" Take a route around the bees in the woods but off trail a little bit?")
	print("\"2\" Run through the bees?")

	decision = None

	while decision not in ("1", "2", "3"): 

		decision = input("> ")

		if decision == "1":
			river_north()
		elif decision == "2":
			print("You've reached the castle. Congratulations! You made it!")
			exit(0)
		else: 
			print("Please answer \"1\" to keep moving or \"2\" to swim back across the river.")






begin()