import subprocess
import os
import time
import gam

def header(user):
    subprocess.run(["clear"])
    print("------------------------------------------------------")
    print("          GAM User Process Automation")
    print("------------------------------------------------------")
    if user.exists == True:
        print("USER: " + user.id)
        print("EMAIL: " + user.email)
        if user.delegate != "":
            print("DELEGATE: " + user.delegate)
        if user.backup != "":
            print("BACKUP: " + user.backup)
    print()

def main_menu():
    print()
    print("   ---- Main Menu ----")
    print()
    print(" 1 - New User      (not implemented)")
    print(" 2 - User Exit ")
    print(" 3 - Quick Tasks")
    print("")
    print(" U - Choose New User")
    print(" X - Quit Program")
    print()  

def quick_menu():
    print()
    print("   ---- Quick Tasks Menu ----")
    print()
    print(" 1 - Reset Password")
    print("")
    print(" U - Choose New User")
    print(" X - Return to Main Menu")
    print() 

def exit_menu():
    print()
    print("   ---- User Exit Menu ----")
    print()
    print(" 1 - Run Delegation")
    print(" 2 - Run Transfer")
    print(" 3 - Run Removal       (not implemented)")
    print(" 4 - Verify & Destroy  (not implemented)")
    print(" 5 - Cleanup           (not implemented)")
    print("")
    print(" U - Choose New User")
    print(" X - Return to Main Menu")
    print()

def show_steps(heading, steps, current_step):
    print()
    print("   ---- " + heading + " ----")
    print()
    for step in range(len(steps)):
        this_string = ""
        if current_step < step:
            this_string += "    [ ] "
        elif current_step == step:
            this_string += " -> [ ] "
        else:
            if steps[step].complete:
                this_string += "    [✓] "
            else:
                this_string += "    [X] "
        this_string += steps[step].name
        print(this_string)
    print()


def delegation_steps(current_step):
    print()
    print("   ---- User Delegation ----")
    print()
    steps = ["Change Org Unit", "Remove from Staff Groups",  "Reset Password & 2sv", "Set up Delegation", "Backup Account - Filter", "Backup Account - Initiate Drive Transfer"]
    
    for step in range(len(steps)):
        this_string = ""
        if current_step < step:
            this_string += "    [ ] "
        elif current_step == step:
            this_string += " -> [ ] "
        else:
            this_string += "    [✓] "
        this_string += steps[step]
        print(this_string)
    print()

def transfer_steps(current_step):
    print()
    print("   ---- User Transfer ----")
    print()
    steps = ["Directory Sharing", "Remove from Groups",  "Remove Recovery Info", "Reset Signin Cookies", "Deprovision User", "Share Calendars", "Share Groups"]
    for step in range(len(steps)):
        this_string = ""
        if current_step < step:
            this_string += "    [ ] "
        elif current_step == step:
            this_string += " -> [ ] "
        else:
            this_string += "    [✓] "
        this_string += steps[step]
        print(this_string)
    print()
    