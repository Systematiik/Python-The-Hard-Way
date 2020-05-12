print("""You enter a dark room with two doors.
Do you go through door #1 or door #2?""")
door = input("> ")
if door == "1":
    print("There's a giant bear here eating a cheese cake.",
    "\nWhat do you do?",
    "\n1. Take the cake.",
    "\n2. Scream at the bear.")
    bear = input("> ")
    if bear == "1":
        print("The bear eats your face off. Good job!")
    elif bear == "2":
        print("The bear eats your leg off. Good job!")
    else:
        print(f"Well, doing {bear} is probably better.")
        print("Bear runs away.")
elif door == "2":
    print("You stare into the endless abyss at Cthulu's retina.",
    "\n1. Blueberries.",
    "\n2. Yellow jacket clothespins.",
    "\n3. Understanding revolvers yelling melodies.")
    insanity = input("> ")
    if insanity == "1" or insanity == "2":
        print("Your body survives powered by a mind of jello.\nGood job!!!")
    else:
        print("The insanity rots your eyes into a pool of muck.\nGood job!!!")
elif door == "69":
    print(f"You found the special door {door}.",
    "\nYou have earned $1000000.")
elif door == "420":
    print("Smoke weed everyday.")
elif door == "door":
    print("That's not a valid door number however. Awesome thinking!\n Congrats!")
else:
    print("You stumble around and fall on a knife and die.\nGood job!!!")