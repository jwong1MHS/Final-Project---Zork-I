from msvcrt import getch

def password():
    password = input("Do you know the secret password? ").lower()
    if (password == "yes"):
        request()
    elif (password == "no"):
        print("start")
    else:
        password()

def request():
    keycode = input("What is the password? ")
    if (keycode == "1"):
        #intro()
        print("intro")
    else:
        confirm = input("Are you sure you know the password? ").lower()
        if (confirm == "no"):
            start() #don't know keycode go straight to game
        else:
            request()   #repeats until you put in a keycode

def start():    #start of the game
    print("Press the Enter key to start: ")
    if ord(getch()) == 13:  #Enter
        #intro() #Starts game
        print("intro")
    else:
        start()

password()