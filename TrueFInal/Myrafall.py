import time
import sys

# Figuring out how users might respond
answer_A = ["A", "a"]
answer_B = ["B", "b"]
answer_C = ["C", "c"]
yes = ["Y", "y", "yes"]
no = ["N", "n", "no"]


def myrafall_start():
    print("When you awaken you hear the sounds of rushing water.\n"
          "you look around and see a great river in front of you"
          "as your looking around you hear a small growl from beside you and you look over to see Crow.\n"
          "She looks at you then turns to look at an island in the middle of the river.\n"
          "On this island you see a small cabin, Crow starts to walk over to the river.\n"
          "You remember that Entiris said Crow would lead you to the pieces of "
          "captains ship, so you decide to follow her.\n"
          "Crow fly's across the river then turns and look at you.\n"
          "looking around you see a fallen log that is half submerged in the water and a bridge.\n"
          "Do you:\n"
          "A : Cross the bridge\n"
          "B: Cross the log\n"
          "C: Jump the river")
    time.sleep(1)
    choice = input(">>> ")
    if choice in answer_A:
        river_a()
    elif choice in answer_B:
        river_b()
    elif choice in answer_C:
        print("You turn around and walk away from the river a bit.\n"
              "You hear Crow make a confused noise from behind you.\n"
              "You take a deep breath and turn to face the river again.\n"
              "You pause for a couple seconds then start to run towards the river.\n"
              "as you hit the edge of the river you jump putting as much force into the jump as you can.\n"
              "You don't even make it halfway across the river when you hit "
              "the rapidly flowing water and are swept away.\n"
              "\n\nnote to self, check the distance before you jump")
        sys.exit()


def river_a():
    print("You walk over to the bridge and decide to walk across it.\n"
          "The walk across is easy enough and you run into no troubles crossing it.\n"
          "Once you are across the bridge Crow walks up to you and motions towards the cabin.\n"
          "You decide to follow her and head towards the cabin.\n"
          "Once you are at the cabin you see what looks to be some bee hives, gardens "
          "that the bees are flying around, and some drying racks.\n"
          "There also appears to be a black cloth spread out across a table.\n"
          "as you are looking around you see a shadow moving inside the cabin\n"
          "Do you knock on the door? Y/N")
    time.sleep(1)
    choice = input(">>> ")
    if choice in yes:
        knock_y()
    if choice in no:
        print("You decide not to knock.\n"
              "Eventually a rabbit human hybrid walks out of the cabin.\n"
              "they seem shocked to see you standing there, while you try to explain "
              "why you are there they draw a sword and get ready to fight.\n"
              "You realize that you don't have any weapons on you and due to that you decide to try and run away.\n"
              "but while you are running away you fail to realize you are running straight towards the river.\n"
              "you end out falling in the river and getting swept away\n"
              "\n\nshould never appear in a retired adventures home with out warning")
        sys.exit()


def river_b():
    print("As you start to cross the log you notice there is a slime"
          "like substance that cover the log making it slippery.\n"
          "half way across the river you almost slip off"
          "the log but are able to catch yourself and other than that you make it across the log safely"
          "if a little shaken from nearly falling into the river.\n"
          "While you are recovering from your scare Crow walks up to you and motions for you to follow her.\n"
          "You decide to follow her and head towards the cabin,\n"
          "Once you are at the cabin you see what looks to be some bee hives, "
          "gardens that the bees are flying around, and some drying racks.\n"
          "There also appears to be a black cloth spread out across a table.\n"
          "as you are looking around you see a shadow moving inside the cabin\n"
          "Do you knock on the door? Y/N")
    time.sleep(1)
    choice = input(">>> ")
    if choice in yes:
        knock_y()
    if choice in no:
        print("You decide not to knock \n"
              "Eventually a rabbit human hybrid walks out of the cabin.\n"
              "they seem shocked to see you standing there, while you try to explain "
              "why you are there they draw a sword and get ready to fight.\n"
              "You realize you don't have any weapons on you and due to that you decide to try and run away.\n"
              "but while you are running away you fail to realize you are running straight towards the river.\n"
              "you end out falling in the river and getting swept away.\n"
              "\n\nshould never appear in a retired adventures home with out warning")
        sys.exit()


def knock_y():
    print("You walk up to the door and knock.\n"
          "You hear some shuffling from inside and a quick 'coming!'\n"
          "When the door opens you see a human-rabbit hybrid.\n"
          "'Hello, what are you doing here? People don't often cross the river.'\n"
          "You introduce yourself, but hesitate and try to decide if you should explain why you are here when\n"
          "Crow makes a sound from behind you.\n"
          "Rabbitman looks at Crow 'ah, your traveling with a sudo dragon, "
          "someone I used to travel with also had one.'\n"
          "'Also, my name is Daedalus or you can call me Dae for short.'\n"
          "Crow continues to look at you then jumps up onto the table and paws at the cloth on it.\n"
          "'Does your dragon have something against my table cloth?'\n"
          "You try to remember the items you were sent to collect and remember that one of them was a mast cloth.\n"
          "The cloth on the table looks like it could be used for a mast cloth, though it is quite small.\n"
          "Do you ask Dae if you can have or trade for the cloth? Y/N")
    time.sleep(1)
    choice = input(">>> ")
    if choice in yes:
        cloth_y()
    if choice in no:
        print("Rather than asking Dae for the cloth you decide to take the cloth and run.\n"
              "You hear Dae shout behind you, you also hear him start ot pursue.\n"
              "What you failed to realize was, you are not close to any crossing points of the river.\n"
              "With out realizing how close to the river you had gotten"
              "you end out falling in and getting taken down river\n"
              "The current drags you further away and you realize you have failed your mission")
        sys.exit()


def cloth_y():
    print("You ask Dae if you could offer him something for the cloth.\n"
          "He looks at you thoughtfully for a few seconds and says,\n"
          "'Why do you need my table cloth?'\n"
          "You tell him about the quest you have been sent on.\n"
          "He seems to think over the information you have just given him,\n"
          "'o you think my table cloth is a part of the ship you need to create, well if that the case\n"
          "Ill trade you a sandwich for the cloth.'\n"
          "You give look Dae a strange look for a few seconds.\n"
          "Do you accept the sandwich trade? Y/N")
    time.sleep(1)
    choice = input(">>> ")
    if choice in yes:
        sand_y()
    if choice in no:
        sand_n()


def sand_y():
    print("You agree to get Dae a sandwich.\n"
          "'Awesome! Let me write a list of ingredients.'\n"
          "He takes a few seconds to write the list then hands you a piece of paper\n"
          "On the paper it says :\n"
          "Tomato, lettuce, baloney(fight me on that spelling “bologna” "
          "is stupid spelling), coated in a sour vinaigrette.\n"
          "'I already have the lettuce and tomato you just have to get the bologna and vinaigrette\n"
          "theres a town just down river from here, take these couple pieces of gold and buy the ingredients.\n"
          "You say good bye to Dae and start heading towards the village\n"
          "Once you are at the village you see a couple of shops,"
          " one that looks like a book store and a grocery store\n"
          "Which one do you go into:\n"
          "A - Book store\n"
          "B - Grocery")
    time.sleep(1)
    choice = input(">>> ")
    if choice in answer_A:
        bookstore()
    if choice in answer_B:
        grocery_store()


def sand_n():
    print("you say no to the sandwich trade. \n"
          "'Well your not getting my table cloth without giving me a sandwich.'\n"
          "Dae will not move from his offer, you both end out in a stale mate.\n"
          "until you eventually give in and decide to help Dae make a sandwich.\n"
          "He hands you a piece of paper that says:\n"
          "Tomato, lettuce, baloney(fight me on that spelling “bologna” "
          "is stupid spelling), coated in a sour vinaigrette.\n"
          "'I already have the lettuce and tomato you just have to get the bologna and vinaigrette\n"
          "theres a town just down river from here, take these couple pieces of gold and buy the ingredients.\n"
          "You say good bye to Dae and start heading towards the village\n"
          "Once you are at the village you see a couple of shops, "
          "one that looks like a book store and a grocery store\n"
          "Which one do you go into:\n"
          "A - Book store\n"
          "B - Grocery")
    time.sleep(1)
    choice = input(">>> ")
    if choice in answer_A:
        bookstore()
    if choice in answer_B:
        grocery_store()


def bookstore():
    print("You walk towards the book store and realize it's closed.\n"
          "but while you are looking through the window"
          "you see a book that has a squid like creature on the front cover\n"
          "you decide to head to the Grocery Store\n"
          ">type y and hit enter")
    time.sleep(1)
    choice = input(">>> ")
    if choice in yes:
        grocery_store()


def grocery_store():
    print("On your way to the store you run into someone.\n"
          "He looks to be wearing a pirates uniform, and he says sorry and quickly moves on.\n"
          "Once you are at the store you find the ingredients Dae asked you to get.\n"
          "you grab them and pay with the gold Dae gave you.\n"
          "On your way out you see that a crowd has gathered in the middle of the town.\n"
          "Do you go and look at whats going on? Y/N")
    time.sleep(1)
    choice = input(">>> ")
    if choice in yes:
        look_y()
    if choice in no:
        look_n()


def look_y():
    print("As you walk over to the group of people you see the person who was dressed as a pirate from before.\n"
          "'Come everyone I have something to say!\n"
          "It is I, Captain Saltblood, and I have come to tell you that it appears an old foe of mine \n"
          "has started to reappear, but fear not for I will swiftly deal with this threat!'\n"
          "You look around the crowd and everyone seems confused as to what Captain is talking about.\n"
          "As you look back at Captain he seems to notice you in the crowd and he quickly says good by to the people,"
          "you try to talk to him but before you can hes gone.\n"
          ">enter y to continue")
    time.sleep(1)
    choice = input(">>> ")
    if choice in yes:
        look_n()


def look_n():
    print("You decide to head back to Dae's cabin.\n"
          "Once your there and Dae sees you he says,\n"
          "'Ah! Did you get the ingredients I asked you to get?'\n"
          "You hand Dae the ingredients\n"
          "'Goog good, time to make my sandwich.\n"
          "While Dae is making his sandwich you grab the cloth and pack it away for later. \n"
          "Dae comes back out of his cabin, 'Do you know where you are heading next?'\n"
          "You think for a couple seconds and realize you don't know where to go next, you tell Dae that\n"
          "'Would you like to look at a map?' Dae offers\n"
          "You accept and Dae leads you into the cabin\n"
          "When Dae rolls out his map Crow quickly jumps on the map and sets a talon on an area of the map\n"
          "'Looks like your friend here knows were your going' Dae comments.\n"
          "You smile at the small dragon and look at where they are pointing, Ortus, "
          "'I have a friend that lives in that area, I can point you towards where they live, "
          "they might be able to help you.' Dae says\n"
          "You agree to let Dae point you to his friend.\n"
          "'They live in a cave around here' Dae says pointing at the map.\n"
          "With the location in mind Dae lets you stay the night in his cabin and you head out to Ortus"
          "in the morning\n")


myrafall_start()
