from msvcrt import getch

def intro():
    inventory = []
    print("--------------------------------------------------")
    one = input("West of House\nYou are standing in an open field west of a white house, with a boarded front door.\nThere is a small mailbox here.\n>")
    if one == "open mailbox":
        print("Open mailbox")

