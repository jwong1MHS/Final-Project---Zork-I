from msvcrt import getch
from random import randint
import os
import sys

#commands = [look; examine; talk, close, exit, pull, move, take, kill, open, enter, push, lift, tie]
#direction = [north, south, east, west, northeast, northwest, southeast, southwest, up, down]

location = []
inventory = []

conditions = {"open_mailbox": False, "open window": False}

def West_of_House():    #game always starts off here
    name = "West of House"
    print(f"{name}")    #prints the name of the location. Formatted because spacing of text can change
    if name not in location:    #check if the location is called already
        location.append(name)   #if not, add it to a list indicating that the game has already mentioned it once
        print("You are standing in an open field west of a white house, with a boarded front \ndoor.\nThere is a small mailbox here.")
    
    option = input("\n>").lower()   #fancy > for users to know where the input is
    
    if option == "open":    #bloacked path
        print("The door cannot be opened.")
        West_of_House()
    elif option == "open mailbox":  #first thing to do
        print("Opening the mailbox reveals a small leaflet.")
        conditions["open_mailbox"] = True   #mark that the mailbox that was originally closed to be open
        West_of_House()
    elif (option == "take leaflet") and (conditions["open_mailbox"] == True):   #only if the mailbox is open
        print("Taken.\n")
        inventory.append("leaflet") #then can you take the leaflet
        West_of_House()
    elif (option == "drop leaflet") and ("leaflet" in inventory):   #only if there is a leaflet in the inventory
        print("Dropped.\n")
        inventory.remove("leaflet") #then can you drop the leaflet
        West_of_House()
    elif option == "inventory": #spills the contents in your inventory
        print("You are carrying:")  
        print(inventory[0])    #prints the contents
        West_of_House()
    elif option == "north":
        North_of_House()
    else:
        print(f"I do not know what {option} is.")   #used for any unknown commands
        West_of_House()


def North_of_House():
    name = "North of House"
    print(f"{name}")    #prints the name of the location. Formatted because spacing of text can change
    if name not in location:    #check if the location is called already
        location.append(name)   #if not, add it to a list indicating that the game has already mentioned it once
        print("You are facing the north side of a white house. There is no door here, and all \nthe windows are boarded up. To the north a narrow path winds through the trees.")
    
    option = input("\n>").lower()   #fancy > for users to know where the input is

    if option == "north":
        Forest_Path()
    elif option == "east":
        Behind_House()
    else:
        print(f"I do not know what {option} is.")   #used for any unknown commands
        North_of_House()


def Forest_Path():
    name = "Forest Path"
    print(f"{name}")    #prints the name of the location. Formatted because spacing of text can change
    if name not in location:    #check if the location is called already
        location.append(name)   #if not, add it to a list indicating that the game has already mentioned it once
        print("This is a path winding through a dimly lit forest. The path heads north-south \nhere. One particularly large tree with some low branches stands at the edge \nof the path.")
    Forest_Chirp()

    option = input("\n>").lower()   #fancy > for users to know where the input is

    if option == "south":
        North_of_House()
    elif (option == "climb up") or (option == "up"):
        Up_a_Tree()
    elif (option == "open egg") and ("egg" in inventory):   #checks if egg is in the inventory
        print("You have neither the tools nor the expertise.")
        Forest_Path()
    else:
        print(f"I do not know what {option} is.")   #used for any unknown commands
        Forest_Path()


def Up_a_Tree():
    name = "Up a Tree"
    print(f"{name}")    #prints the name of the location. Formatted because spacing of text can change
    if name not in location:    #check if the location is called already
        location.append(name)   #if not, add it to a list indicating that the game has already mentioned it once
        print("You are about 10 feet bove the ground nestled among some large branches. The \nnearest branch above you is above your reach. \nBeside you on the branch is a small bird's nest. \nIn the bird's nest is a large egg encrusted with precious jewels, apparently \nscavenged by a childless songbird. The egg is covered with fine gold inlay, \nand ornamented in lapis lazuli and mother-of-pearl. Unlike most eggs, this one \nis hinged and closed with a delicate looking clasp. The egg appears extremely \nfragile.")
    Forest_Chirp()
    
    option = input("\n>").lower()   #fancy > for users to know where the input is

    if (option == "climb down") or (option == "down"):
        Forest_Path()
    elif option == "get egg":
        print("Taken.")
        Up_a_Tree()
    else:
        print(f"I do not know what {option} is.")   #used for any unknown commands
        Up_a_Tree()


def Forest_Chirp(): #random line sometimes called when in the forest
    random = randint(1,6)
    if random == 5:
        print("You hear in the distance the chirping of a song bird.")


def Behind_House():
    name = "Behind House"
    print(f"{name}")    #prints the name of the location. Formatted because spacing of text can change
    if name not in location:    #check if the location is called already
        location.append(name)   #if not, add it to a list indicating that the game has already mentioned it once
        print("You are behind the white house. A path leads into the forest to the east. In \none corner of the house there is a small window which is slightly ajar.")

    option = input("\n>").lower()   #fancy > for users to know where the input is

    if option == "open window":
        print("With great effort, you open the window far enough to allow entry.")
        conditions["open_window"] = True
        Behind_House()
    elif (option == "enter house") and (conditions["open_window"] == True):     #checks if the window is open
        Kitchen()
    elif option == "enter house":
        print("The window is closed.")
        Behind_House()
    else:
        print(f"I do not know what {option} is.")   #used for any unknown commands
        Behind_House()


def Kitchen():
    name = "Kitchen"
    print(f"{name}")    #prints the name of the location. Formatted because spacing of text can change
    if name not in location:    #check if the location is called already
        location.append(name)   #if not, add it to a list indicating that the game has already mentioned it once
        print("You are in the kitchen of the white house. A table seems to habe been used \nrecently for the preparation of food. A passage leads to the west and a dark \nstaircase can be seen leading upward. A dark chimney leads down and to the east is a small window which is open.")

    option = input("On the table is an elongated brown sack, smelling of hot peppers. \nA bottle is sitting on the table. \nThe glass bottle contains: \n A quantity of water\n\n>").lower()
    
    if option == "grab bottle":
        print("Taken.")
        inventory.append("glass bottle with water")
        Kitchen()
    elif option == "grab sack":
        print("Taken.")
        inventory.append("brown sack of hot peppers")
        Kitchen()
    elif option == "inventory":
        print("You are carrying:")
        for p in inventory:
            print(p)
    elif option == "save":
        print("Saved. Your password is: \nb11cd6c377ce942048d66ce45c702d")
        Kitchen()
    elif option == "eat peppers":
        print("Eating the peppers causes your mouth to catch on fire, and slowly you turn to \nashes.")
        dead()
    elif option == "west":
        Living_Room()
    else:
        print(f"I do not know what {option} is.")   #used for any unknown commands
        Kitchen()


def Living_Room():
    name = "Living Room"
    print(f"{name}")    #prints the name of the location. Formatted because spacing of text can change
    if name not in location:    #check if the location is called already
        location.append(name)   #if not, add it to a list indicating that the game has already mentioned it once
        print("You are in the living room. There is a doorway to the east, a wooden door with \nstrange gothic lettering to the west, which appears to be nailed shut, a trophy case, and a large oriental rug in the center of the room.")
    
    option = input("Above the trophy case hangs an elvish sword of great antiquity. A battery-powered brass lantern is on the trophy case.\n\n>")
    
    if option == "grab sword":
        print("Taken.")
        inventory.append("sword")
        Living_Room()
    elif option == "grab lantern":
        print("Taken.")
        inventory.append("lantern")
        Living_Room()
    elif option == "move rug":
        print("With a great effort, the rug is moved to one side of the room, revealing the dusty cover of a closed trap door.")
        Living_Room()
    elif option == "open trapdoor":
        print("The door reluctantly opens to reveal a rickety staircase descending into darkness.")
        Living_Room()
    elif option == "turn on lamp":
        print("The brass lantern is now on")
        Living_Room()
    elif option == "down":
        Cellar()
    else:
        print(f"I do not know what {option} is.")   #used for any unknown commands
        Living_Room()


def Cellar():
    name = "Cellar"
    print(f"{name}")    #prints the name of the location. Formatted because spacing of text can change
    if name not in location:    #check if the location is called already
        location.append(name)   #if not, add it to a list indicating that the game has already mentioned it once
        print("You have moved into a dark place. \nThe trap door crashes shut, and you hear someone barring it.\n")
    
    option = input("It is pitch black. You are likely to be eaten by a grue\n\n>")
    
    if option == "down":
        print("Oh, no! You have walked into the slavering fangs of a lurking grue!\n")
        dead()
    else:
        print(f"I do not know what {option} is.")   #used for any unknown commands
        Cellar()



"""---------------------------------------------------------------------------------------------------------------"""

def opening():  #the very start of the game
    os.system('cls||clear')     #https://stackoverflow.com/questions/2084508/clear-terminal-in-python
    password = input("Do you know the secret password?\n\n>").lower()
    if (password == "yes"):
        request(password, False)    #user has not resurrected
    elif (password == "no"):
        start()     #jump straight into the game
    else:
        opening()

def request(x, resurrect):  #asks for the keycode to jump to a part of the game
    keycode = input("What is the password?\n\n>")
    if (keycode == "b11cd6c377ce942048d66ce45c702d"):
        if (resurrect == True):     #checks if user has been resurrected
            print("You have been resurrected successfully.")
        Kitchen()
    else:
        confirm = input("Are you sure you know the password?\n\n>").lower()
        if (confirm == "no"):
            start()     #don't know keycode go straight to game
        else:
            request(confirm, 0)     #repeats until you put in a keycode

def start(): #start of the game
    print("Press the Enter key to start:")
    if ord(getch()) == 13:      #Enter key
        os.system('cls||clear')     #clear screen
        West_of_House()     #Starts game
    else:
        start()

def dead(): #called when the user is dead
    print("--------------------------------------------------\n")
    resurrect = input("  ****  You have died  ****\nContinue?\n\n>").lower()
    if resurrect == "yes":
        request(0, True)    #user has resurrected
    elif resurrect == "no":
        print("You are now dead. Your password at this stage is: b11cd6c377ce942048d66ce45c702d\n1\nKeep it. The game will now close. Press Enter to exit the game.")
        if ord(getch()) == 13:      #Enter key
            sys.exit(0)
    else:
        dead()

opening()
