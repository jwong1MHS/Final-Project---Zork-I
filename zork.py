from msvcrt import getch
import os
import sys

def intro():
    inventory = []
    os.system('cls||clear') #https://stackoverflow.com/questions/2084508/clear-terminal-in-python
    print("--------------------------------------------------")
    one = input("West of House\nYou are standing in an open field west of a white house, with a boarded front door.\nThere is a small mailbox here.\n\n>").lower()
    if one == "open mailbox" or "open" or "open it":
        os.system('cls||clear') #https://stackoverflow.com/questions/2084508/clear-terminal-in-python
        print("You open the mailbox and find a bear in it. The bear eats you.")
        dead()

"""---------------------------------------------------------------------------------------------------------------"""

def opening():
    os.system('cls||clear') #https://stackoverflow.com/questions/2084508/clear-terminal-in-python
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
        intro()
    else:
        confirm = input("Are you sure you know the password?\n\n>").lower()
        if (confirm == "no"):
            start() #don't know keycode go straight to game
        else:
            request(confirm, 0)   #repeats until you put in a keycode

def start():    #start of the game
    print("Press the Enter key to start:")
    if ord(getch()) == 13:  #Enter key
        intro() #Starts game
    else:
        start()

def dead():
    print("--------------------------------------------------")
    resurrect = input("You are dead.\nContinue?\n\n>").lower()
    if resurrect == "yes":
        request(0, resurrect)
    elif resurrect == "no":
        print("You are now dead. Your password at this stage is: \n1\nKeep it. The game will now close. Press Enter to exit the game.")
        if ord(getch()) == 13:  #Enter key
            sys.exit(0)
    else:
        dead()

opening()

