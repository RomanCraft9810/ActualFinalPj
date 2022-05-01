import time
import sys

# Figuring out how users might respond
answer_A = ["A", "a"]
answer_B = ["B", "b"]
answer_C = ["C", "c"]
yes = ["Y", "y", "yes"]
no = ["N", "n", "no"]


def glaceo_start():
    print("It takes you another three days before you reach the mountain, you look around "
          "to see if you can spot something that will lead you to where you need to be, but see nothing.\n"
          "You turn to Crow and see her looking at the top of the "
          "mountain and realize that you are gonna have to climb that thing.\n"
          "As you are climbing the mountain you hear a rumble.\n"
          "You look up and see an avalanche heading you way.\n"
          "Do you:\n"
          "A - try to out run it\n"
          "b - look for cover\n"
          "c - stand still")
    time.sleep(1)
    choice = input(">>> ")
    if choice in answer_A:
        ava_a()
    elif choice in answer_B:
        ava_b()
    elif choice in answer_C:
        ava_c()


def ava_a():
    print("You turn and try to outrun the avalanche, but before you know it the avalanche is on you \n"
          "You are buried alive with no way to escape\n"
          "\n\nYou should try to find cover")
    sys.exit()


def ava_b():
    print("You look for cover and spot a cave near you.\n"
          "You quickly run into the cave and Crow follows you.\n"
          "The avalanche goes past the cave, but now you have a new problem.\n"
          "The cave entrance is blocked.\n"
          "While you are sitting there trying to think of what to do you hear a meowing from outside\n"
          "Crow starts to dig at the snow, do you help? Y/N")
    time.sleep(1)
    choice = input(">>> ")
    if choice in yes:
        help_y()
    if choice in no:
        help_n()


def ava_c():
    print("You stand there not being able to believe your bad luck.\n"
          "In the time you were standing there the avalanche covered you\n"
          "\n\nThink about your life decisions later, yah know when theres not immediate death coming for you.")
    sys.exit()


def help_y():
    print("You start to help Crow dig through the snow.\n"
          "You quickly realize the snow was not as thick as you originally thought.\n"
          "Finally you break through the surface of the snow, "
          "once you are out and help Crow out you see a black cat waiting for you.\n"
          "Once the cat sees it has your attention it turns around and starts to walk away.\n"
          "Do you follow it? Y/N")
    time.sleep(1)
    choice = input(">>> ")
    if choice in yes:
        follow_y()
    if choice in no:
        follow_n()


def help_n():
    print("You decide not to help Crow dig, eventually Crow grows tired and stops digging.\n"
          "There is barley any progress on the hole and with your stubbornness you still don't help dig\n"
          "Eventually you hear a roar of a creature in the distance\n"
          "\n\nShould've helped")
    sys.exit()


def follow_y():
    print("You decide to follow the cat and ascend higher up the mountain.\n"
          "Thankfully nothing else happens on your way up.\n"
          "Once you reach teh top of the mountain there appears to be someone there.\n"
          ">que dramatic lightning\n"
          "someone sitting in what appears to be a ... shopping cart? Slowly turns to face you,\n"
          "they are petting a cat in that way someone does when they are being evil, like in the movies.\n"
          "The cat appears to be the same one that lead you up the mountain.\n"
          "'I have been expecting you' They say.\n"
          "'You are looking for the hull of Captains ship correct?' they ask.\n"
          "You nod your head, looking at them in concern, have they blinked this while time?\n"
          "'Well, look no further, cause it's right here!' They shout.\n"
          "'But you can only get it by gaining my trust, but that will be a hard task' They say.\n"
          "What do you do?\n"
          "A - try giving them something\n"
          "B - try to convince them\n"
          "C - take the cart by force")
    time.sleep(1)
    choice = input(">>> ")
    if choice in answer_A:
        cart_a()
    elif choice in answer_B:
        cart_b()
    elif choice in answer_C:
        cart_c()


def follow_n():
    print("You decide not to follow the cat.\n"
          "Instead you wander the mountain lost, and eventually freeze.\n"
          "\n\nShould have followed the cat")
    sys.exit()


def cart_a():
    print("You decide to look at what you have that you could give them.\n"
          "You have:\n"
          "A - a sandwich, quite old at this point\n"
          "B - An amethyst\n"
          "C - A the feather Phyrra gave you")
    time.sleep(1)
    choice = input(">>> ")
    if choice in answer_A:
        give_a()
    elif choice in answer_B:
        give_b()
    elif choice in answer_C:
        give_c()


def cart_b():
    print("You try to convince them to give you the cart.\n"
          "They keep refusing and eventually you hear a roar in the distance.\n"
          "'Looks like you are to late' They say, in a sing song voice\n"
          "\n\nShould have tried a gift")
    sys.exit()


def cart_c():
    print("You try to take the cart by force, but they move out of the way and you fall off the mountain instead.\n"
          "\n\nVesper died to fall damage")
    sys.exit()


def give_a():
    print("You hold out the sandwich, but the person looks at it in disgust.\n"
          "'Are you trying to give me food poising, like I know Im dead already but that's kinda rude.'\n"
          "'BUt, it doesn't matter cause your to late' They say as a rumbling can be heard in the distance."
          "\n\nWhy did you try to give them an old sandwich?")
    sys.exit()


def give_b():
    print("You hold the Amethyst out to the person.\n"
          "When they see it their eyes go wide, they look at you questioningly, "
          "but eventually the scoot the cart closer and take the gem.\n"
          "'I suppose this gem will make a good peace offering, my name is Maeick.'\n"
          "'I was given this cart to guard, but I suppose you could have it' Maeick says.\n"
          "He pushes the cart towards you, and you stop it from rolling down the hill.\n"
          "You look at the three items you have managed to"
          "gather and try to figure out how they are supposed to make a boat.\n"
          "You look at Maeick for help.\n"
          "'Im not sure how it works, try putting all the part on top of each other.' Maeick says.\n"
          "Do you do what Maeick suggested? Y/N")
    time.sleep(1)
    choice = input(">>> ")
    if choice in yes:
        sug_y()
    if choice in no:
        sug_n()


def give_c():
    print("You hold out the feather, but...\n"
          "With the winds on the top of the mountain it gets blown out of your hand\n"
          "welp, that didn't work out to well\n"
          ">Type y and hit enter to try again.")
    time.sleep(1)
    choice = input(">>> ")
    if choice in yes:
        follow_y()


def sug_y():
    print("You decide to set all the parts on top of each other.\n"
          "The parts seem to react to each other, and next thing you know the mast and mast cloth "
          "are perfectly together with the mast fixed into one of the holes on the shopping cart.\n"
          "You decide to climb into the shopping cart to see what would happen and the next "
          "thing you know the shopping cart is flying thorough the air.\n"
          "Its heading towards a small island in the middle of the ocean\n"
          "Time to figure out what this quest was for.")


def sug_n():
    print("You decide to try and figure out how the cart works yourself.\n"
          "You spend almost two days trying to figure it out, when you hear a roar from close by.\n"
          "\n\nGuess you should have listened to Maeick")
    sys.exit()


glaceo_start()
