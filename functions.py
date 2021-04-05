import subprocess
import os
import time
import gam
import output

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

        gam_data = gam.run("info user " + user.id,False)

        if gam_data.returncode == 0:
            print()
            print("User",user.email,"exists.")
            user.exists = True
            time.sleep(1)
        else:
            output.header(user)
            print("User "+user.id+" doesn't exist, please try again")
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
        print("   exiting...")
        exit()
    print("   Continuing on...")

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
        print("   skipping...")
        time.sleep(.5)
        return False

#exit menu
def exit_menu(user):

    #print menu
    output.header(user)
    output.exit_menu()
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
        time.sleep(1)
        exit_transfer(user)
    if key == "x":
        print("exiting...")
        exit()
    elif key == "u":
        user.exists = False
        output.header(user)
        user = get_user()
        exit_menu(user)
    else: 
        print("Functionality not yet supported...")


#gam exit transfer process
def exit_transfer(user):
    #step 0 - turn off directory sharing
    output.header(user)
    output.transfer_steps(0)
    time.sleep(.5)
    if ask_confirm("Turn off directory sharing?"):
        gam_data = run("update user "+ user.id + " gal off")
        print(gam_data.output)
    time.sleep(.5)
    #step 1 - remove from groups
    output.header(user)
    output.transfer_steps(1)
    time.sleep(.5)
    if ask_confirm("Get " + user.id + "'s Groups?"):
        print("Getting user groups...")
        gam_data = gam.run("user " + user.id + " print groups role member", False)
        print("Group info:")
        print(gam_data.output)
    time.sleep(.5)
    print()
    print("ERROR:  Task not implemented")
    ask_abort()
    #step 2 - remove recovery info
    output.header(user)
    output.transfer_steps(2)
    print("ERROR: Task not implemented")
    time.sleep(.5)
    ask_abort()
    #step 3 - reset sign-in cookies
    output.header(user)
    output.transfer_steps(3)
    print("ERROR: Task not implemented")
    time.sleep(.5)
    ask_abort()
    #step 4 - Deprovision User
    output.header(user)
    output.transfer_steps(4)
    print("ERROR: Task not implemented")
    time.sleep(.5)
    ask_abort()
    #step 5 - share calendars
    output.header(user)
    output.transfer_steps(5)
    print("ERROR: Task not implemented")
    time.sleep(.5)
    ask_abort()
    #step 6 - share groups
    output.header(user)
    output.transfer_steps(6)
    print("ERROR: Task not implemented")
    time.sleep(.5)
    ask_abort()
    #complete
    output.header(user)
    output.transfer_steps(7)
    print("Transfer Complete")
    print("    Returning to main menu...")
    time.sleep(1)
    exit_menu(user)