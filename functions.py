import subprocess
import os
import time
import gam

#User class
class User:
    def __init__(self, id, email, exists=False):
        self.id = id
        self.email = email
        self.exists = exists

#prompt for user function
def prompt_user():
    #prompt for username
    print()
    this_id = input("Enter User:")

    #remove any whitespace
    this_id = this_id.replace(" ","")

    #process username -> email
    this_email = this_id
    if "@" not in this_id:
        this_email+= "@adventures.org"

    return User(this_id,this_email)

#verify user
def get_user():
    user = User("","")
    while user.exists == False:
        user = prompt_user()
        time.sleep(.25)
        print()
        print("Checking to see if",user.id,"exists...")
        time.sleep(.25)

        gam_data = gam.run("info user " + user.id)

        if gam_data.returncode == 0:
            print()
            print("User",user.email,"exists.")
            user.exists = True
            time.sleep(.5)
        else:
            print()
            print("User doesn't exist, please try again")
            time.sleep(.2)
        
    return user

#get key 
import termios, sys , tty
def getch():
   fd = sys.stdin.fileno()
   old_settings = termios.tcgetattr(fd)
   try:
      tty.setraw(fd)
      ch = sys.stdin.read(1)     #This number represents the length
   finally:
      termios.tcsetattr(fd, termios.TCSADRAIN, old_settings)
   return ch

def ask_abort():
    key = ""
    print("Abort process? y/n ",end='',flush=True)
    while key != "y" and key != "n":
        key = getch()
    print(key)
    if key == "y":
        print("exiting...")
        exit()
    print("Continuing on...")

def ask_confirm(message):
    key = ""
    print()
    print(message + " y/n ", end='', flush=True)
    while key != "y" and key != "n":
        key = getch()
    print(key)
    if key == "y":
        time.sleep(.5)
        return True
    else:
        print("skipping...")
        time.sleep(.5)
        return False

#exit menu
def exit_menu(user):

    #print menu
    print()
    print("--------User Exit Menu--------")
    print()
    print(" 1 - Initiate New Exit")
    print(" 2 - Run Delegation")
    print(" 3 - Run Transfer")
    print(" 4 - Run Removal")
    print(" 5 - Verify & Destroy")
    print(" 6 - Cleanup")
    print("")
    print(" U - Choose New User")
    print(" X - Quit")
    print()
    print("Please choose an option: ",end='',flush=True)
    key = ""

    #get valid choice
    while ( 
        key != "1" and key != "2" and key != "3" and key != "4" 
        and key != "5" and key != "6" and key !="u" and key != "x" 
        ):
        key = getch()

    print(key)
    time.sleep(.25)
    if key == "3":
        print()
        print("Starting User Transfer Process...")
        time.sleep(.7)
        gam.exit_transfer(user)
    if key == "x":
        print("exiting...")
        exit()
    elif key == "u":
        user = get_user()
        exit_menu(user)
    else: 
        print("Functionality not yet supported...")


    