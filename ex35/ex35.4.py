from sys import exit

def gold_room():
	print("This room is full of gold. How much do you take?")

	choice = input("> ")
	if "0" in choice or "1" in choice:
		how_much = int(choice)
	else:
		dead("Man, learn to type a number.")

	if how_much < 50:
		print("Nice, you're not greedy. You win!")
		exit(0)
	else:
		dead("You greedy bastard!")


def bear_room():
	print("There is a bear here.")
	print("The bear has a bunch of honey.")
	print("The fat bear is in front of another door.")
	print("How are you going to move the bear?")
	print("Type \"1\" for \"take honey,\" \"2\" for \"taunt bear,\" or \"3\" for \"open door.\"")

	choice = None

	#maybe it's best to think of this line as just a condition in general
	bear_moved = False

	while choice not in (1, 2, 3):
		choice = input("> ")

		if choice == "1":
			dead("The bear looks at you and then slaps your face off.")
		elif choice == "2" and not bear_moved:
			print("The bear has moved from the door.")
			print("You can go through it now.")
			bear_moved = True
		elif choice == "2" and bear_moved:
			dead("The bear gets mad and chews your leg off.")
		elif choice == "3" and not bear_moved:
			dead("The bear is in your way and kills you when you try to open the door.")
		elif choice == "3" and bear_moved:
			gold_room()
		else:
			print("I have no idea what that means.")
			print("Please type \"1\" for \"take honey,\" \"2\"" + 
				" for \"taunt bear,\" or \"3\" for \"open door.\"")

	
def cthulhu_room():
	print("Here you see the great evil Cthulhu.")
	print("He, it, whatever stares at you and you go insane.")
	print("Do you flee for your life or eat your head?")

	choice = input("> ")

	if "flee" in choice:
		start()
	elif "head" in choice:
		dead("Well that was tasty!")
	else:
		cthulhu_room()

def dead(why):
	print(why, "Good job!")
	exit(0)


def start():
	print("You are in a dark room.")
	print("There is a door to your right and left.")
	print("Which one do you take?")
	print("Answer \"l\" for \"left\" or \"r\" for \"right\".")

	choice = None

	while choice not in ("l", "r"):
		choice = input("> ")

		if choice == "l":
			bear_room()
		elif choice == "r":
			cthulhu_room()
		else:
			print("I have no idea what that means.")
			print("Please answer \"l\" for \"left\" or \"r\" for \"right\".")


start()