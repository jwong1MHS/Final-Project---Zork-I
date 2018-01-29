from msvcrt import getch
import os
import sys

commands = [look, examine, talk, close, exit, pull, move, take, kill, open, enter, push, lift, tie]
direction = [north, south, east, west, northeast, northwest, southeast, southwest, up, down]

location = {}

def West_of_House():
    option = input("West of House\nYou are standing in an open field west of a white house, with a boarded front door.\nThere is a small mailbox here.\n\n>").lower()
    if option == "west":
        Forest(-1, 0)
    elif option == "north":
        North_of_House()
    elif option == "south":
        South_of_House()
    elif option == "open":
        print("The door cannot be opened.")
        location 



def Forest(latitude, longitude):
    option = input("Forest\nThis is a forest, with trees in all directions. To the east, there appears to be sunlight.\n\n>")
    
    if option == "west":
        latitude -= 1
    elif option == "east":
        latitude += 1
    elif option == "south":
        longitude -= 1
    elif option == "north":
        longitude += 1

    if latitude == 0 and longitude == 1:
        Forest_Path()
    elif latitude == 0 and longitude == 2:
        Clearing()
    elif longitude > 2:
        print("The forest becoems impenetrable to the north.\n")
        Forest(latitude, 2)
    elif longitude < -1:
        print("Storm tossed trees block your way.\n")
        FOrest(latitude, -1))
    elif latitude < -1:
        print("You would need a machete to go further west.\n")
        Forest(-1, longitude)
    else:
        Forest(latitude, longitude)

def Forest_Path():
    option = input("Forest Path\nThis is a path winding through a dimly lit forest. The path heads north-south here. One particularly large tree with some low branches stands at the edge of the path.\n\n>").lower()
    if option == "north":
        Clearing()
    elif option == "south":
        North_of_House()
    elif option == "east":
        Forest(1,0)
    elif option == "west":
        Forest(-1.0)
    
def North_of_House():
    option = input("North of House\nYou are facing the north side of a white house. There is no door here, and all the windows are boarded up. To the north a narrow path winds through the trees.\n\n>").lower()
    if option == "north":
        Forest_Path()
    if option == "south":
        print("The windows are all boarded.\n")
        North_of_House()
    if option == "west":
        West_of_House()
    if option == "east":
        Behind_House()

def South_of_House()
    option = input("South of House\nYou are facng the south side of a white house. There is no door here, and the windows are all boarded.\n\n>").lower()
    if option == "south":
        Forest(0, -1)

def Clearing():
    option = input("Clearing\nYou are in a clearing, with a forest surrounding you on all sides. A path leads south. On the ground is a pile of leaves.\n\n")
    if option == "pick up":
        option = input("(up the pile of leaves)In disturbing the pile of leaves, a grating is revealed.\nTaken.\n\n>")
    if option == "north":
        print("The forest becomes impenetrable to the north.\n")
        Clearing()

def Behind_House():
    option = input("You are behind the white house. A path leads into the forest to the east, In one corner of the house there is a small window which is slightly ajar.")
    if option == "west":
        print("The kitchen window is closed\n")
    if option == "east":
        Clearing()

def Canyon_View():
    option("Canyon View\nYou are at the top of the Grand Canyon on its west wall. From here there is a marvelous view of the canyon and parts of the Frigid River upstream. Across the canyon, the walls of the White CLiffs join the mighty ramparts of the FLathead Mountains to the east. Following the Canyon upstream to the north, Aragain Falls may be seen, complete with rainbow. The mighty Frigid River flows out from a great dark cavern. To the west and south can be seen an immense forest, stretching for miles around. A path leads northwest. It is possible to climb down into the canyon from here.\n\n>")
    if option == "east":
        Rocky_Ledge()

def Rocky_Ledge():
    option("Rocky Leedge\nYou are on a ledge about halfway up the wall of the river canyon. You can see from here that the main flow from Aragain Falls twist along a passage which is impossible for you to enter. Below you is the cnayon bottom. Above you is more cliff, which appears climbable.\n\n>")
    if option == "down":
        Canyon_Bottom()
    elif option == "up":
        Rocky_Ledge()
    elif option == "east" or "west" or "north" or "south":
        print("You can't go that way.\n")

def Canyon_Bottom():
    option("Canyon Bottom\nYou are beneath the walls of the river which may be climbable here. The lesser part of the runoff of Aragain Falls flows by below. To the north is a narrow path.\n\n>")
    if option == "up":
        Rocky_Ledge()
    elif option == "north":
        End_of_Rainbow()
    elif option == "down":
        print("You can't go that way.\n")
        Canyon_Bottom()
    
def End_of_Rainbow():
    option = input("End of Rainbow\nYou are on a small, rocky beach on the continuation of the Frigid River past the Falls. The beach is narrow due to the presence of the White Cliffs. The river canyon opens here and sinlight shines in from above. A ranbow crosses over the falls to the east and a narrow path continues to the southwest.\n\n>")
    if option == "north" or "south" or "east" or "west" or "down" or "up" or "in" or "out":
        print("You can't go that way.")
        End_of_Rainbow()


"""---------------------------------------------------------------------------------------------------------------"""

def opening():
    os.system('cls||clear')     #https://stackoverflow.com/questions/2084508/clear-terminal-in-python
    password = input("Do you know the secret password?\n\n>").lower()
    if (password == "yes"):
        request(password, 0)
    elif (password == "no"):
        start()
    else:
        opening()

def request(x, y):
    keycode = input("What is the password?\n\n>")
    if (keycode == "1"):
        if (y == "yes"):
            print("You have been resurrected successfully.")
        start()
    else:
        confirm = input("Are you sure you know the password?\n\n>").lower()
        if (confirm == "no"):
            start()     #don't know keycode go straight to game
        else:
            request(confirm, 0)     #repeats until you put in a keycode

def start(): #start of the game
    print("Press the Enter key to start:")
    if ord(getch()) == 13:      #Enter key
        os.system('cls||clear')
        West_of_House()     #Starts game
    else:
        start()

def dead():
    print("--------------------------------------------------")
    resurrect = input("You are dead.\nContinue?\n\n>").lower()
    if resurrect == "yes":
        request(0, resurrect)
    elif resurrect == "no":
        print("You are now dead. Your password at this stage is: \n1\nKeep it. The game will now close. Press Enter to exit the game.")
        if ord(getch()) == 13:      #Enter key
            sys.exit(0)
    else:
        dead()

opening()
#i don't know
