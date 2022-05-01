import sys
import time

# Possible answers to questions.
answer_A = ["A", "a"]
answer_B = ["B", "b"]
answer_C = ["C", "c"]
yes = ["Y", "y", "yes"]
no = ["N", "n", "no"]


# Gives the story text, and the options for the user
def intro():
    print(" You awaken in a strange area, it look like nothing you've ever seen before.\n  "
          " You are surrounded by mushrooms that are taller than trees.\n "
          " Beyond that these mushrooms are many different colors. \n"
          " As you look around you see a stranger standing in a clearing ahead of you.\n"
          " Will you approach them? Y/N")
    time.sleep(1)
    choice = input(">>> ")  # Allows the user to input an option.
    if choice in yes:  # State User Options.
        approach_the_stranger()
    elif choice in no:
        print("\nYou choose not to approach the stranger. \n"
              "\n As you stand there looking around the world starts to fade out around you.\n"
              "\nYou awaken in your bed and think 'that was a strange dream' and decide to get ready for your day.\n"
              "\n You return to your normal life, at least until you hear a roar in the distance.\n"
              "\n\n you didn't even talk to the person, the world was destroyed")
        sys.exit()


def approach_the_stranger():
    print("You decide to approach the stranger, they don't seem to react to your presence. \n"
          "Will you:\n"
          "A. Stand still and wait for them to notice you\n"
          "B. Say something to get their attention\n"
          "C. walk up and tap them on the shoulder")
    time.sleep(1)
    choice = input(">>> ")
    if choice in answer_A:
        print("\nYou decide to stand still. The person never notices you and eventually the world around you fades out"
              "into nothingness and you awaken in your bed. \n You decide to move "
              "on with your day, that is until you hear a roaring in the distance\n"
              "The world was destroyed, you didn't even talk to the person")
        sys.exit()
    elif choice in answer_B:
        say_something()
    elif choice in answer_C:
        tap()


def say_something():
    print("\nYou you decide to try and get the persons attention by saying something to them\n"
          "They seem shocked to see you there.\n"
          "'Oh! I didn't notice you there. I'm Entris, may I ask who you are?\n"
          "Will you tell Entris your name? Y/N")
    time.sleep(1)
    choice = input(">>> ")
    if choice in yes:
        name_y()
    elif choice in no:
        name_n()


def tap():
    print("You walk up to the person and tap them on the shoulder."
          "They jump and seem surprised to see you there"
          "'Hello there, Its surprising to see someone else here. "
          "My name is Entris, may I ask who you are?'\n"
          "Tell Entris your name? Y/N")
    time.sleep(1)
    choice = input(">>> ")
    if choice in yes:
        name_y()
    elif choice in no:
        name_n()


def name_y():
    print("'My name is Vesper.' You say.\n"
          "'That is a lovely name' Entris responds\n"
          "'If I may ask, do you know why you are here?'\n"
          "You tell Entris you have no clue why you are here.\n"
          "'Well, it appears the ancient powers of this world have chosen you to"
          "complete a prophesy.\n"
          "'Do you want to hear the prophesy?' Y/N")
    time.sleep(1)
    choice = input(">>> ")
    if choice in yes:
        prophesy_y()
    elif choice in no:
        prophesy_n()


def name_n():
    print("you choose not to tell Entris your name. \n"
          "As you both stare at each other the world starts to fade out\n"
          "the last thing you see is Entris turn back to face the forest once more and you "
          "hear the roar of a far off creature\n"
          "you awake in a cold sweat and the only thought that runs through your head is,"
          "'what a strange nightmare'\n"
          "\n\nyou didn't want to give your name, well the world ended because of that")
    sys.exit()


def prophesy_y():
    print("'It is said that there was once a great pirate captain, who was known"
          "to sail all the seas and had the ability to keep his crew safe from all dangers,"
          "but an evil that he once stopped has started to reappear once more.\n"
          "The day of destruction is close, but that is why you are here\n"
          "It is said that there are three main parts of captains ship.\n"
          "Your goal is to gather all these parts and remake captains once great ship.\n"
          "so, will you accept the quest?' Y/N")
    time.sleep(1)
    choice = input(">>> ")
    if choice in yes:
        quest_y()
    elif choice in no:
        quest_n()


def prophesy_n():
    print("'are you sure?' Y/N")
    choice = input(">>> ")
    if choice in yes:
        print("'ok'")
        quest_y()
    elif choice in no:
        prophesy_y()


def quest_y():
    print("'One thing I do want to say is, I once meet this great captain.\n"
          "thought it was only for a short period of time, and when we"
          "parted ways he stole half the parties gold and left us, never to be seen"
          "again, so if you do run into him take anything he says with a grain of salt'\n"
          "'Also, I have someone who can help you on this quest'\n"
          "Entris whistles and you start to hear rustling behind you, do you investigate? Y/N")
    time.sleep(1)
    choice = input(">>> ")
    if choice in yes:
        investigate_rustling()
    elif choice in no:
        ignore_rustling()


def quest_n():
    print("Are you sure? Y/N")
    choice = input(">>> ")
    if choice in yes:
        print("'Then the ancients must have chosen wrong'\n"
              "Entris waves her hand at you and turns back to the forest\n"
              "The world starts to fade out and you awaken with no memory of the dream.\n"
              "\n\nThe world ended just because you didn't want to take the quest")
        sys.exit()
    elif choice in no:
        quest_y()


def investigate_rustling():
    print("You decide to look in the bushes and find a sudo-dragon.\n"
          "Its scales are similar to that of a ravens feather and they look slightly bigger than"
          "the average house cat\n"
          "'That is Crow, she traveled with me back when I was doing missions.\n"
          "She will now help you find all the parts of captains ship.'\n"
          "Do you start the quest? Y/N")
    time.sleep(1)
    choice = input(">>> ")
    if choice in yes:
        quest_start()
    elif choice in no:
        print("\nSeriously?"
              "\n\nThe world Ended")
        sys.exit()


def ignore_rustling():
    print("You choose to ignore the rustling, it eventually stops but you hear a hiss\n"
          "from behind you.\n"
          "You turn around to see whats hissing only to come face to face with a sudo-dragon.\n"
          "'That is Crow, she traveled with me back when I was doing missions.\n"
          "She will now help you find all the parts of captains ship.'\n"
          "Do you start the quest? Y/N")
    time.sleep(1)
    choice = input(">>> ")
    if choice in yes:
        quest_start()
    elif choice in no:
        print("\n\nSeriously?"
              "\n\nThe world Ended")
        sys.exit()


def quest_start():
    print("'You will find the first part of the ship in the land of Myrafall,"
          "good luck' Entris says.\n"
          "You are surrounded by light and the world fades from view")


intro()  # Allows the script to run, without it code doesn't run.
