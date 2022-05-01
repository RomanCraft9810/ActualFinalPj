import time

# Figuring out how users might respond
answer_A = ["A", "a"]
answer_B = ["B", "b"]
answer_C = ["C", "c"]
yes = ["Y", "y", "yes"]
no = ["N", "n", "no"]


def final_start():
    print("The cart finally comes to a landing behind a rock on the small island.\n"
          "You get out of the cart and peak around the rock and see...\n"
          "The dude you ran into at the town a few day ago?\n"
          "Hes still wearing that pirate uniform, but he appears to be doing something.\n"
          "As you watch you see the captain drawing symbols on the ground.\n"
          "Eventually the man stops to admire his work\n"
          "He looks up at the sky as the storm starts to worsen\n"
          "'It has been a long time since we fought' the man says.\n"
          "You watch in confusion as the man pulls a book out of his pocket, "
          "on the cover appears to be a creature of some kind.\n"
          "'I will summon thee Cthulhu once more' The man states.\n"
          "Then it clicks, this is Captain, the one from the prophesy\n"
          "He not only protects his crew from danger, but he also causes the danger himself.\n"
          "What do you do:\n"
          "A - Shout and tell him to stop\n"
          "B - Ram the cart into his ankles\n"
          "C - Join him")
    time.sleep(1)
    choice = input(">>> ")
    if choice in answer_A:
        end_a()
    elif choice in answer_B:
        end_b()
    elif choice in answer_C:
        end_c()


def end_a():
    print("You try to shout at Captain to stop\n"
          "'Why would I stop, There is not enough danger anymore I have to spice up peoples lives\n"
          "It appears that your please are not enough to stop Captain\n"
          "Cthulhu emerges from the circle\n"
          "Captain is able to stop him, but just barley.\n"
          "Many lives are lost and many homes are destroyed, and no matter what "
          "you say no one believes that Captain summoned Cthulhu.\n"
          "\n\nEnding: That's a lot of damage")


def end_b():
    print("You decide to hop back into the cart and ram it into captain.\n"
          "As you are coming around the rock, the cart starts to pick up speed despite the fact the land is flat.\n"
          "Captain realises you are coming at the last second, but its not enough time to get out of the way.\n"
          "You ram the cart right into captains ankles and he falls to the ground.\n"
          "In the process many of the runes that were drawn on the ground are destroyed.\n"
          "'Why would you do that, don't ye think the world could use a little spicing up' Captain questions.\n"
          "You reply with no, if Captain goes through with this it will cause damage to many innocent people.\n"
          "Captain seems to think this over, but the next thing you know your eyes are full of salt water.\n"
          "When your vision clears Captain is gone, he escaped but for the time being the world is safe.\n"
          "\n\nEnding: I'll be back!")


def end_c():
    print("You decide to join Captain in summoning Cthulhu.\n"
          "'What are you doing here?' Captain questions.\n"
          "You tell Captain that you want to help him.\n"
          "'Ah, another who wants to bring a little chaos to the world' he responds.\n"
          "He tells you what to do and where to put the runes, and eventually the summoning is ready\n"
          "Together you are able to fight and defeat Cthulhu, and both of you enjoy the glory.\n"
          "\n\nEnding:Glory for all")


final_start()
