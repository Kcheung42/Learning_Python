from sys import exit

def gold_room():
	print "This room is full of gold. How much do you take?"
	next = raw_input("> ")
	try:
		assert int(next) > 10, "you took too little gold"
		how_much = int(next)
	except ValueError:
		dead("Man, learn to tpe a number.")
	if how_much < 50:
		print "Nice you win!"
		exit(0)

def bear_room():
	print "There is a bear here."
	print "There is a bear here."
	print "There is a bear here."
	print "How are you going to move the bear?"
	bear_moved = False

	while True:
		next = raw_input("> ")
		if next == "take honey":
			dead("Bear looks at you and slaps your face o")
		elif next == "taunt bear" and  not bear_moved:
			print "The bear moved from the door you can go through it"
			bear_moved = True
		elif next == "taunt bear" and bear_moved:
			dead("The bear is pissed and chews your leg off.")
		elif next == "open door" and bear_moved:
			gold_room()
		else:
			print "I got no idea what that means."

def cthulu_room():
	print "here you see the great evil Cthulu."
	print "He, it, whatever stares at you and you go insane"
	print "Do you flee for your life or eat your head"

	next = raw_input("> ")
	if "flee" in next:
		start()
	elif "head" in next:
		dead("Well that was tastey")
	else:
		cthulu_room()


def dead(why):
	print why, "Good Job!" , " idiot"
	exit(0)

def start():
	print "You are in a dark room."
	print "There is a door to your right and left."
	print "Which one do you take?"

	next = raw_input("> ")
	if next == "left":
		bear_room()
	if next == "right":
		cthulu_room()
	else:
		dead("you stumble around the room until you starved")


if __name__ == "__main__":
	gold_room()
	start()
