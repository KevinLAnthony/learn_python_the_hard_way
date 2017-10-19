from sys import exit

def gold_room():
	print("This room is full of gold. How much do you take?")

	choice = input("> ")
	# so the choices of gold you can take include 0 or 1?
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
	bear_moved = False

	#While what's true, bear_moved? ANS: No, it's while true is true, so it's always true
	#and loop always running.
	while True:
		choice = input("> ")

		if choice == "take honey":
			#what does the "dead" function do? ANS: It's defined below, and the 
			#printed statement here is the parameter (the "why") for why you're dead.
			dead("The bear looks at you and then slaps your face off.")
		#I guess "not bear_moved" means bear_moved = True, since bear_moved = False
		elif choice == "taunt bear" and not bear_moved:
			print("The bear has moved from the door.")
			print("You can go through it now.")
			#why the need for bear_moved = True here?
			bear_moved = True
		elif choice == "taunt bear" and bear_moved:
			dead("The bear gets mad and chews your leg off.")
		elif choice == "open door" and bear_moved:
			gold_room()
		else:
			print("I have no idea what that means.")

	
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
	#what does exit(0) do? What happens if I edit it or delete it? ANS: Seems to have no effect.


def start():
	print("You are in a dark room.")
	print("There is a door to your right and left.")
	print("Which one do you take?")

	choice = input("> ")

	if choice == "left":
		bear_room()
	elif choice == "right":
		cthulhu_room()
	else:
		dead("You stumble around the room until you starve.")


start()