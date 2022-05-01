import time
import sys

# Figuring out how users might respond
answer_A = ["A", "a"]
answer_B = ["B", "b"]
answer_C = ["C", "c"]
yes = ["Y", "y", "yes"]
no = ["N", "n", "no"]


def ortus_start():
    print("Once its bright enough to travel, you say good bye to Dae and head towards the location he gave you.\n"
          "You have been traveling for three days, nothing has really happened.\n"
          "You see a break in the trees and head towards it.\n"
          "it leads into a clearing, other than a few feathers there is not really much in the clearing.\n"
          "You decide to set up camp for the night, you light a fire "
          "and eat a sandwich Dae gave to you before you left.\n"
          "After you finish eating you hear Crow start to growling.\n"
          "Do you investigate? Y/N")
    time.sleep(1)
    choice = input(">>> ")
    if choice in yes:
        crow_y()
    elif choice in no:
        crow_n()


def crow_y():
    print("You decide to go and check up on what Crow is doing.\n"
          "When you find Crow you see her looking at another Sudo-Dragon.\n"
          "This one is green with orange on its spikes and horns.\n"
          "It doesnt seem aggressive, but more confused than anything.\n"
          "You call Crow back and try to figure out to do with the other "
          "Sudo-Dragon when you hear something approaching.\n"
          "Someone walks through the trees and the other Sudo-Dragon runs up to them and climbs onto their shoulder.\n"
          "The new person looks like a bird human hybrid, "
          "they have large wings on their back that are mostly black with hints of blue on the covert feathers.\n"
          "'Who are you!? What are you doing here!' "
          "They shout, they place their hand on what looks like the sheath of a weapon.\n"
          "What do you do?\n"
          "A : explain why your there\n"
          "B : stay silent\n"
          "C : Run")
    time.sleep(1)
    choice = input(">>> ")
    if choice in answer_A:
        bird_a()
    elif choice in answer_B:
        bird_b()
    elif choice in answer_C:
        bird_c()


def crow_n():
    print("You decide not to investigate why Crow is growling.\n"
          "Eventually Crow comes running into the clearing and hot on her tail is another Sudo-Dragon.\n"
          "This one is green with orange on its spikes and horns.\n"
          "While you are trying ot figure out what to do Crow runs over to you and hides behind your legs.\n"
          "You hear something else approaching and see someone come out of the trees,"
          " the other sudo-Dragon runs up onto their shoulder.\n"
          "The new person looks like a bird-human hybrid, they have large wings on their back "
          "that are mostly black with hints of blue on the covert feathers.\n"
          "'Who are you!? What are you doing here!' They shout, they place their hand on "
          "what looks like the sheath of a weapon.\n"
          "What do you do?\n"
          "A : explain why your there\n"
          "B : stay silent\n"
          "C : Run")
    time.sleep(1)
    choice = input(">>> ")
    if choice in answer_A:
        bird_a()
    elif choice in answer_B:
        bird_b()
    elif choice in answer_C:
        bird_c()


def bird_a():
    print("You raise your hands in surrender and start to explain the quest you were sent on and "
          "how Dae pointed you in this direction looking for someone.\n"
          "The person seems to recognize Dae's name, they drop some of their defensive posture.\n"
          "'Dae, as in a rabbit person?' They ask.\n"
          "You reply yes to that and they seem to look more relieved.\n"
          "'Well if Dae sent you this way then you must be trust worthy. My name is Phyrra "
          "and this is Cinder.' Phyrra says motioning to themself and the sudo-dragon.\n"
          "'Whats your name?' Phyrra asks.\n"
          "You tell Phyrra your name and Crows name.\n"
          "'Lets head over to my home, better under cover than out in the open like this.'\n"
          "Phyrra motions for you to follow them. Do you? Y/N")
    time.sleep(1)
    choice = input(">>> ")
    if choice in yes:
        follow_y()
    elif choice in no:
        follow_n()


def bird_b():
    print("You freeze up and cant think of a response.\n"
          "The bird person draws their sword and before you have a change to move its over\n"
          "\n\nThat didn't work out very well")
    sys.exit()


def bird_c():
    print("You decide to try and run, but you forgot to take into account that the person had wings\n"
          "Before your even half way across the clearing the person has taken flight and it was over\n"
          "\n\nMaybe don't run from the person that can fly.")
    sys.exit()


def follow_y():
    print("You decide to follow Phyrra to her house, which you quickly find "
          "out it is a cave in the side of the mountain.\n"
          "Once you are inside you see many things that range from cloths of different regions, "
          "photos, herbs, what looks like a bottle of space dust, and a pair of sunglasses.\n"
          "Both Crow and Cinder are on opposite sides of the cave, neither "
          "looking like they want to interact with the other. \n"
          "'So you are looking for items that belonged to a ship of someone named Captain right?' Phyrra asks.\n"
          "You say yes, and she seems to think for a few seconds, "
          "'I may have one thing that could be what you are looking for.'\n"
          "Phyrra heads to the back of the cave, once they come back "
          "they are carrying what looks like the mast of a small ship.\n"
          "'Its not very big, but it might be what your looking for.' Phyrra says.\n"
          "Crow seems to perk up at the sight of the item and turns to look at you nodding her head. \n"
          "'Ill give it to you on one condition, I want you to help me "
          "get more of Cinders favorite snack.' Phyrra says.\n"
          "Do you accept the mission? Y/N")
    time.sleep(1)
    choice = input(">>> ")
    if choice in yes:
        mission_y()
    elif choice in no:
        mission_n()


def follow_n():
    print("You decide not to follow Phyrra, but as you stand watching Phyrra walk away you feel a nip at your ankle.\n"
          "You look down to see Crow nipping and pushing at your leg, "
          "when you look at her she motions her head towards where Phyrra left.\n"
          "You try to ignore Crow but Crow remains persistent and you eventually follow Phyrra.\n"
          "You eventually reach Phyrra's home and realize its not a house, but a cave in the side of a mountain.\n"
          "Once you're inside you see many things that range from cloths of "
          "different regions, photos, herbs, what looks like a bottle of space dust, and a pair of sunglasses.\n"
          "Both Crow and Cinder are on opposite sides of the cave, neither "
          "looking like they want to interact with the other. \n"
          "'So you are looking for items that belonged to a ship of someone named Captain right?' Phyrra asks.\n"
          "You say yes, and she seems to think for a few seconds, "
          "'I may have one thing that could be what you are looking for.'\n"
          "Phyrra heads to the back of the cave, once they come "
          "back they are carrying what looks like the mast of a small ship.\n"
          "'Its not very big, but it might be what your looking for.' Phyrra says.\n"
          "Crow seems to perk up at the sight of the item and turns to look at you nodding her head. \n"
          "'Ill give it to you on one condition,"
          " I want you to help me get more of Cinders favorite snack.' Phyrra says.\n"
          "Do you accept the mission? Y/N")
    time.sleep(1)
    choice = input(">>> ")
    if choice in yes:
        mission_y()
    elif choice in no:
        mission_n()


def mission_y():
    print("You decide to accept the quest, and ask Phyrra what Cinders favorite snack is.\n"
          "'Its and herb called Dragon nip, I let her have it in small amounts.' Phyrra responds.\n"
          "'It will be a plant that looks close to a clover, "
          "but the flower will be a deep blue color, there should be some not to far from the cave.'\n"
          "With this information you head out of the cave to look for the plant.\n"
          "As you are looking you see three plants that look similar to the description Phyrra gave you.\n"
          "Which plant do you pick?\n"
          "A - One has three leaves that look like mittens with a deep blue flower.\n"
          "B - A plant with three short round leaves and a deep blue flower\n"
          "C - A plant with three long rounded leaves and a deep blue flower.")
    time.sleep(1)
    choice = input(">>> ")
    if choice in answer_A:
        plant_a()
    elif choice in answer_B:
        plant_b()
    elif choice in answer_C:
        plant_c()


def mission_n():
    print("You don't accept the quest.\n"
          "'Well, the only way you're getting the mast is if you this for me.' Phyrra says\n"
          "At a stale mate you decide to leave, you are not going to go pick some "
          "flowers for some prophesy that may not be true.\n"
          "You leave and less than two weeks later the ground starts to shake "
          "and the roars of some creature can be heard.\n"
          "\n\nSometimes flower picking can save the world")
    sys.exit()


def plant_a():
    print("You gather the first plant you saw, but quickly after you touch the plant your hands start to itch.\n"
          "You quickly realize that the plant you went to pick must be some form of "
          "poison ivy, but what you didn't realize was it was a deadly ivy.\n"
          "Quickly the rash starts to spread from your hands to the "
          "rest of your body, and soon after your body shuts down\n"
          "Word of advice, unless you know what it is, if it has mittens leave it alone.")
    sys.exit()


def plant_b():
    print("You decide to pick the second plant.\n"
          "when you touch the plant, nothing happens, you continue "
          "gathering the plant and head back to Phyrra's house.\n"
          "Once you get back Phyrra seems happy to see you.\n"
          "'I see you got the right plant, I realized after you left that I "
          "forgot to tell you about dragon nips deadly look a-likes, but that's water under the bridge now.'\n"
          "You look at Phyrra in shock of the fact she forgot "
          "a detail that important, but hand the plants over quickly.\n"
          "'The mast is yours now, all I have left to do is dry these plants and then they will be ready for Cinder.'\n"
          "'Also, you are welcome to stay here over night since it is getting late.'\n"
          "You thank Phyrra and once she leads you to where you can sleep you start to get ready for bed.\n"
          "The next morning before you leave Phyrra approaches you again.\n"
          "'I wanted to give you a couple more things before you left.' \n"
          "Phyrra hands you a feather and an amethyst. \n"
          "You thank Phyrra for the items, and pull out the"
          " map Dae gave you out so you can figure out where to go next.\n"
          "Crow sets her nose on a spot labeled Glaceo, specifically near one of the mountains. \n"
          "'Off to the cold lands of Glaceo I see, good luck and be careful of avalanches.' Phyrra warns\n"
          "You thank her for the warning and head out to Glaceo\n")


def plant_c():
    print("You decide to grab the third plant.\n"
          "While you are gathering the plant you see it has berries on it.\n"
          "You decide to eat a couple, it isn't until you go to stand "
          "up that you realize you cant move your legs anymore.\n"
          "You quickly realize that your having more and more trouble moving "
          "your body, and before you know it the world fades out around you.\n"
          "\n\nDon't eat random berries kids.")
    sys.exit()


ortus_start()
