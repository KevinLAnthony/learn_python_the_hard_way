from sys import exit

def die(cause_of_death):
	print(cause_of_death)
	print("RIP")
	exit(0)


def begin():
	print("You want to reach the castle, which is many miles away to the north over very rough terrain.")
	print("You are at a fork on a trail in the woods with paths leading to the left and right.")
	print("Both trails lead north in the direction of the castle.")
	print("Which path do you take?")
	print("Answer \"l\" for \"left\" or \"r\" for \"right\".")

	while True:

		decision = input("> ")

		if decision == "l":
			river_south_1()
		elif decision == "r":
			mountain_south()
		else:
			print("That wasn't one of the choices. Let's try this again...")
			begin()


def river_south_1():
	print("You come to an old, high, rickety bridge with a raging river far below it.")
	print("Which path do you take?")
	print("Answer \"1\" to cross the high, rickety bridge.")
	print("Answer \"2\" to swim across the strong, swirling, wide river.")
	print("Answer \"3\" to turn and go back the way you came.")

	while True: 

		decision = input("> ")

		if decision == "1":
			print("You start to make your way across the rickety bridge when about half-way across, the" + 
		  		" ropes break, plunging you into the river below.")
			bridge()
		elif decision == "2":
			print("You decide to take on the river instead of contend with a questionable bridge " +
				"and manage to make it to the other side wet but uninjured.")
			river_north()
		elif decision == "3":
			begin()
		else:
			print("That wasn't one of the choices. Let's try this again...")
			river_south_1()


def bridge():
	#I realize that when one leaves the river area and comes back, the bridge
	#will again be intact, but this type of thing is not unusual for video games
	#, and I haven't figured out how to compensate for it yet, anyway.
	
	print("Do you...")
	print("\"1\" swim upstream against the current?")
	print("\"2\" swim downstream with the current?")
	print("\"3\" swim forward toward the side of the river you were trying to reach?")
	print("\"4\" swim back toward the side of the river from which you came?")

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
			print("You're wet, but you made it across.")
			river_north()
		elif decision == "4":
			print("You're wet, but you made it.")
			river_south_2()
		else: 
			print("Please answer \"1\" to swim against the current, \"2\" to swim with the current," +
				  " \"3\" to swim forward, or \"4\" to swim back.")


def river_south_2():
	print("The bridge is out, so you're again faced with swimming north across the river " +
		  "or south on the trail through the woods.")
	print("Do you...")
	print("\"1\" swim north across the strong, swirling, wide river?")
	print("\"2\" go back south on the trail in the woods " + 
		  "and in the wrong direction of the castle?")

	decision = None

	while decision not in ("1", "2"): 

		decision = input("> ")

		if decision == "1":
			print("You make your way across the river wet and cold but unscathed.")
			river_north()
		elif decision == "2":
			begin()
		else: 
			print("Please answer \"1\" to swim across the river or \"2\" to go back through the woods " + 
				  "and away from the castle.")


def river_north():
	print("Do you...")
	print("\"1\" keep north going along the trail into woods?")
	print("\"2\" swim back south across the river?")

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
	print("You continue into the woods on the trail toward the castle " +
		  "and encounter a swarm of killer bees right in your path.")
	print("Do you...")
	print("\"1\" run back south toward the river?")
	print("\"2\" take a route around the bees in the woods but off trail a little bit?")
	print("\"3\" run through the bees?")

	decision = None

	while decision not in ("1", "2", "3"): 

		decision = input("> ")

		if decision == "1":
			print("You make your way back to the north side of the river.")
			print("Where to now?")
			river_north()
		elif decision == "2":
			print("You've got some cuts and bruises from the heavy brush, " +
				"but congratulations, you've reached the castle! You made it!")
			exit(0)
		elif decision == "3":
			print("You really ran through a swarm of killer bees?")
			print("Well, you can imagine what happens next...")
			die("You got killT!")
		else: 
			print("Please answer \"1\" to keep moving or \"2\" to swim back across the river.")


def mountain_south():
	print("You're now at the bottom of a mountain with a trail going up and one going around.")
	print("You can tell that going up the mountain will be quicker but likely more treacherous.")
	print("Which path do you take?")
	print("Answer \"1\" to ascend the mountain.")
	print("Answer \"2\" to take the trail around the mountain.")
	print("Answer \"3\" to turn and go back the way you came.")

	while True: 

		decision = input("> ")

		if decision == "1":
			print("You ascend up the mountain, but the air gets increasingly thin and cold, and" + 
		  		" you're spent, anyway, given the steepness alone.")
			print("You're concerned you may be unable to keep going forward.")
			ascend_mountain()
		elif decision == "2":
			print("You decide to take the trail around the mountain even though it's likely longer.")
			print("It takes some time, and you're worn out for a while, " +
				"but you finally make it around the mountain.")
			wolf()
		elif decision == "3":
			begin()
		else:
			print("That wasn't one of the choices. Let's try this again...")
			mountain_south()


def ascend_mountain():
	print("Do you...")
	print("\"1\" keep going up the mountain?")
	print("\"2\" stop and rest before going anywhere else?")
	print("\"3\" go back down the mountain?")

	decision = None

	while decision not in ("1", "2", "3"): 

		decision = input("> ")

		if decision == "1":
			die("You tire yourself out, pass out, get hypothermia, and die.")
		elif decision == "2":
			print("You stop and rest before moving on. Smart move.")
			after_rest()
		elif decision == "3":
			die("You try to make your way back down the steep trail but are so exhausted " +
				"\nthat you lose your footing and tumble down the steep mountain at literally " +
				"\n\"break neck\" speed, breaking multiple bones until you are left lying there " +
				"\nwith no way to get up and no one to help you. ")
		else: 
			print("Please answer \"1\" to keep going up the mountain, " +
				"\"2\" to stop and rest, or \"3\" to go back down the mountain.")


def after_rest():
	print("Do you...")
	print("\"1\" keep going up the mountain?")
	print("\"2\" go back down the mountain?")

	decision = None

	while decision not in ("1", "2", "3"): 

		decision = input("> ")

		if decision == "1":
			print("After resting, you make it up the mountain and back down the other side.")
			mountain_north()
		elif decision == "2":
			print("You head back down toward the foot of the mountain.")
			mountain_south()
		else: 
			print("Please answer \"1\" to keep going up the mountain " +
				"or \"2\" to go back down the mountain.")


def mountain_north():
	print("You're now standing at the base of the north side of the mountain where trails " +
		"going over the mountain and around the mountain meet.")
	print("The trail also continues on north.")
	print("Do you...")
	print("\"1\" keep going north on the trail through the woods?")
	print("\"2\" ascend the mountain from its north side?")
	print("\"3\" go south around the mountain?")

	decision = None

	while decision not in ("1", "2", "3"): 

		decision = input("> ")

		if decision == "1":
			wolf()
		elif decision == "2":
			die("As you're going up the mountain, you're killed by an avalanche.")
		elif decision == "3":
			print("You go back around the mountain and again reach the mountain's south side.")
			mountain_south()
		else: 
			print("Please answer \"1\" to keep going north on the trail, " +
				"\"2\" to ascend the mountain from the north side, or \"3\" to go back around the mountain.")

def wolf():
	print("You continue on your way north to the castle and encounter a single, snarling wolf on the trail in the woods.")
	print("Still snarling and growling, the wolf starts walking toward you.")
	print("Do you...")
	print("\"1\" turn and run back south toward the north side of the mountain?")
	print("\"2\" take a route around the wolf in the woods but off trail a little bit?")
	print("\"3\" back away slowly while still facing the wolf?")
	print("\"4\" yell, make aggressive noises and walk toward the wolf?")

	decision = None

	while decision not in ("1", "2", "3", "4"): 

		decision = input("> ")

		if decision == "1":
			print("Growling and with sudden speed, the wolf catches up with you and attacks you.")
			die("You try to fight it off, but several more wolves are suddenly on you, too, and " +
				" at this point, there's nothing you can do.")
		elif decision == "2":
			print("You try to go around the wolf, but his pack-mates were lying in wait to attack you there.")
			die("Suddenly, the whole pack is on you, and you're done for.")
		elif decision == "3":
			print("The wolf keeps closing in on your position, snarling and growling the whole time.")
			print("At this point, the wolf looks really mean, big, and close.")
			wolf_close()
		elif decision == "4":
			print("The wolf keeps closing in on your position, snarling and growling the whole time.")
			print("At this point, the wolf looks really mean, big, and close.")
			wolf_close()
		else: 
			print("Please answer \"1\" to run back south, \"2\" to take a route around the wolf. " +
				"\"3\" to back away slowly, or \"4\" to be aggresive toward the wolf.")


def wolf_close():
	print("Do you...")
	print("\"1\" turn and run back south toward the north side of the mountain?")
	print("\"2\" take a route around the wolf in the woods but off trail a little bit?")
	print("\"3\" start throwing rocks and sticks at the wolf?")

	decision = None

	while decision not in ("1", "2", "3"): 

		decision = input("> ")

		if decision == "1":
			print("Growling and with sudden speed, the wolf catches up with you and attacks you.")
			die("You try to fight it off, but several more wolves are suddenly on you, too, and " +
				" at this point, there's nothing you can do.")
		elif decision == "2":
			print("You try to go around the wolf, but its pack-mates were lying in wait to attack you there.")
			die("Suddenly, the whole pack is on you, and you're done for.")
		elif decision == "3":
			print("Initially, the wolf winces at the debris you're throwing at it then and lunges for you.")
			wolf_fight()
		else: 
			print("Please answer \"1\" to run back south, \"2\" to take a route around the wolf. " +
				"\"3\" to throw rocks and sticks at the wolf.")


def wolf_fight():
	print("Do you attempt to...")
	print("\"1\" move out of the way and grab a big stick lying closeby?")
	print("\"2\" punch the wolf?")
	print("\"3\" kick the wolf?")

	decision = None

	while decision not in ("1", "2", "3"): 

		decision = input("> ")

		if decision == "1":
			print("You successfully dodge the wolf as it lunges at you and manage to swipe the stick " +
				"from where it lies.")
			print("You are now standing where the wolf originally was when it was blocking your " +
				"path to the castle.")
			print("The wolf starts running toward you again.")
			grab_stick()
		elif decision == "2":
			print("You try to go punch the wolf, but your fist misses, and the wolf sinks his teeth " +
				"into your arm, knocking you to the ground and puncturing an artery in your arm.")
			die("Suddenly, the whole pack is on you, and you're done for.")
		elif decision == "3":
			print("You try to go kick the wolf, but your foot misses, and the wolf sinks his teeth " +
				"into your calf, causing you trip and fall.")
			die("Suddenly, the whole pack is on you, and you're done for.")
		else:
			print("Please answer \"1\" to move and grab the stick, \"2\" to punch the wolf, " +
				"or \"3\" to kick the wolf.")


def grab_stick():
	print("Do you attempt to...")
	print("\"1\" make a break for it toward the castle?")
	print("\"2\" swing the stick at the wolf when it's within range again?")
	print("\"3\" drop the stick and hold your hands up showing the wolf you're not its enemy?")

	stick_swung = False

	while True:

		decision = input("> ")

		if decision == "1" and stick_swung == False:
			print("Growling and with sudden speed, the wolf catches up with you and attacks you. " +
				"from behind.")
			die("You try to fight it off, but several more wolves are suddenly on you, too, and " +
				" at this point, there's nothing you can do.")
		elif decision == "1" and stick_swung == True:
			print("You make a break for it and manage to get away from the wolf while " + 
				"it's temporarily stunned.")
			print(" If the remainder of the pack is hiding closeby, then " +
				"you must have managed to outrun it, because you soon find yourself all alone on the trail " +
				"and on your way to the castle.")
			print("Tired and feeling lucky to be alive, you finally reach the castle. Congratulations!")
			print("You hope next time, though, that you'll remember to bring your sword.")
			exit(0)
		elif decision == "2" and stick_swung == False:
			print("The wolf lunges at you again, and you manage to whack it squarely in the nose " +
				"with a hard impact.")
			print("The wolf whimpers and scampers away slightly while looking dazed for a few seconds " +
				"but isn't necessarily out of the fight yet.")
			print("Do you now attempt to run north toward the castle or take another swing " +
				"at the wolf? Surrender is also still an option.")
			print("Answer \"1\" to run, \"2\" to swing again, or \"3\" to hold up your hands.")
			stick_swung = True
		elif decision == "2" and stick_swung == True:
			print("After staggering around for a few seconds, the wolf again lunges at you, and " +
				"once again, you manage to hit the wolf right in the face.")
			die("However, you no longer have only one wolf to worry about, as five more emerge from the woods " +
				"and all jump on you at once.")
		elif decision == "3":
			die("Really?")
		else:
			print("That wasn't one of the choices.")
			begin()			


begin()