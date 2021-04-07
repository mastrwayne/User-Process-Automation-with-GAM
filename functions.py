import subprocess
import os
import time
import gam
import output
import menus

#User class
class User:
    def __init__(self, id, email, exists=False, delegate = "", backup = ""):
        self.id = id
        self.email = email
        self.exists = exists
        self.delegate = delegate
        self.backup = backup

#Step class -- used to store info about a gam command / step in a process
class Step:
    def __init__(self, name, command, question):
        self.name = name
        self.command = command
        self.question = question
        self.complete = False

#prompt for user function
def prompt_user(prompt = "Enter User: "):
    #prompt for username
    print()

    this_id = input(prompt)

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
        user = verify_user(user)
        
    return user

def verify_user(user):
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

def user_add_delegate(user):
    if user.delegate = "":
        delegate = User("","")
        while delegate.exists == False:
            delegate = prompt_user("Please enter " + user.id + "'s delegate: ")
            time.sleep(.25)
            delegate = verify_user(delegate)
        
        user.delegate = delegate.email
    return user

def user_add_former(user):
    if user.former == "":
        former = User("","")
        while former.exists == False:
            former = prompt_user("Please enter " + user.id + "'s backup account: ")
            time.sleep(.25)
            former = verify_user(former)
        
        user.backup = former.email
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

def ask_confirm(message=""):
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

def input_to_continue():
    print()
    print("Press any key to continue...",end='',flush=True)
    time.sleep(.25)
    getch()

#gam exit delegation process
def exit_delegation(user):
    heading = "User Delegation"
    #"Change Org Unit", "Remove from Staff Groups",  "Reset Password", "Turn off 2sv" "Set up Delegation", "Backup Account - Filter", "Backup Account - Initiate Drive Transfer"
    steps = [
        Step(
            "Change Org Unit",
            "update org \"User Accounts/Exiting Users\" move user "+ user.id,
            "Move " + user.id + " to Exiting Users group?"
        ),
        Step(
            "Remove from Staff Groups",
            del_remove_from_staff_groups,
            "Remove " + user.id + ("from ALL staff groups?\n" +
            "(gastaff, fulllist, domesticstaff, internationalstaff)")
        ),
        Step(
            "Reset Password",
            "gam update user " + user.id + " password S@lvation7",
            "Reset password?"
        ),
        Step(
            "Turn off 2sv",
            "gam user " + user.id + " turnoff2sv",
            "Turn off 2-step verification?"
        ),
        Step(
            "Delegate Inbox",
            "user "  + user.id + " add delegate " + user.delegate,
            "Delegate " + user.id + "'s inbox to delegate?"
        ),
        Step(
            "Backup Account Setup",
            "user " + user.backup + " filter to " + user.email + "archive label"  + user.email,
            "Create backup account filter?"
        ),
        Step(
            "Transfer Drive to Backup Account",
            "create datatransfer " + user.id + " gdrive "+ user.backup  + " privacy_level shared,private",
            ""
        )
    ]
    #get user delegate and former
    if user.delegate == "" and ask_confirm("Notate user delegate?"):
        user = user_add_delegate(user)
    if user.backup ==  "" and ask_confirm("Notate user backup account?"):
        user = user_add_former(user)
    #run steps
    run_steps(user,heading,steps)
    #all steps done.
    print()
    print("Transfer Process Complete.")
    input_to_continue()
    menus.exit_menu(user)

#gam exit transfer process
def exit_transfer(user):
    #define steps
    heading = "User Transfer"
    steps = [
        Step(
            "Directory Sharing",
            "update user "+ user.id + " gal off",
            "Turn off directory sharing?"
        ),
        Step(
            "Remove from Groups",
            xfer_remove_from_groups,
            "Remove " + user.id + " from groups?"
        ),
        Step(
            "Remove Recovery Info",
            "",
            ""
        ),
        Step(
            "Reset Signin Cookies",
            "",
            ""
        ),
        Step(
            "Deprovision User",
            "",
            ""
        ),
        Step(
            "Share Calendars",
            "",
            ""
        ),
        Step(
            "Share Groups",
            "",
            ""
        )
    ]
    #run steps
    run_steps(user,heading,steps)
    #all steps done.
    print()
    print("Transfer Process Complete.")
    input_to_continue()
    menus.exit_menu(user)

#step unpacking
def run_steps(user,heading,steps):
    #loop through all steps
    for i in range(len(steps)):
        output.header(user)
        output.show_steps(heading,steps,i)
        time.sleep(.5)
        #single command
        if type(steps[i].command) == str and steps[i].command != "":
            gam_data = gam.preview_run(steps[i].command,steps[i].question)
            print(gam_data.output)
            if gam_data.returncode == 0:
                steps[i].complete = True
        #function to run with multiple commands
        elif type(steps[i].command) != str:
            if ask_confirm(steps[i].question):
                steps[i].complete = steps[i].command(user)
        #not programmed yet
        else:
            print()
            print("ERROR:  functionality not implemented yet")
            ask_abort()
        print()
        time.sleep(.5)
        input_to_continue()



#############################################
#multi-stage step command functions


def xfer_remove_from_groups(user):
    gam_data = gam.preview_run("user " + user.id + " print groups role member", "Get " + user.id + "'s Groups?", False)
    if gam_data.output != "":
        print("Group info:")
        print(gam_data.output)
    time.sleep(.5)
    print()
    print("ERROR:  Additional functionality not implemented")
    ask_abort()
    return False

def del_remove_from_staff_groups(user):
    #gastaff
    gam_data = gam.run("update group gastaff remove user " + user.email,False)
    print(gam_data.output)
    #fulllist
    gam_data = gam.run("update group fulllist remove user " + user.email,False)
    print(gam_data.output)
    #domesticstaff
    gam_data = gam.run("update group domesticstaff remove user " + user.email,False)
    print(gam_data.output)
    #internationalstaff
    gam_data = gam.run("update group internationalstaff remove user " + user.email,False)
    print(gam_data.output)
    print()
    print("Process Complete.")
    input_to_continue()
    return True
