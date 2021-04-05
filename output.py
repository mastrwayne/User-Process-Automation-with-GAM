import subprocess
import os
import time
import gam

def header(user):
    subprocess.run(["clear"])
    print("------------------------------------------------------")
    print("          GAM User Process Automation")
    if user.exists == True:
        print("              USER:  "+ user.id)
    print("------------------------------------------------------")
    print()
    

def exit_menu():
    print()
    print("---- User Exit Menu ----")
    print()
    print(" 1 - Initiate New Exit (not implemented)")
    print(" 2 - Run Delegation    (not implemented)")
    print(" 3 - Run Transfer")
    print(" 4 - Run Removal       (not implemented)")
    print(" 5 - Verify & Destroy  (not implemented)")
    print(" 6 - Cleanup           (not implemented)")
    print("")
    print(" U - Choose New User")
    print(" X - Quit")
    print()

def transfer_steps(current_step):
    print()
    print(" ---- User Transfer ----")
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
    