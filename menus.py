import subprocess
import os
import time
import gam
import output
import functions


#main menu
def main_menu(user, message=""):

    #print menu
    output.header(user)
    if message != "":
        print(message)
    output.main_menu()
    print("Please choose an option: ",end='',flush=True)
    key = ""

    #get valid choice
    while ( 
        key != "1" and key != "2" and key != "3" and key !="u" and key != "x" 
        ):
        key = functions.getch()

    print(key)
    time.sleep(.25)
    if key == "2":
        print()
        print("   Starting Deprovision Process...")
        time.sleep(1)
        exit_menu(user)
    elif key == "3":
        print()
        print("   Starting Quick Tasks...")
        time.sleep(1)
        quick_menu(user)
    elif key == "x":
        print("   Exiting...")
        time.sleep(.5)
        exit()
    elif key == "u":
        user.exists = False
        output.header(user)
        user = functions.get_user()
        main_menu(user)
    else: 
        print("   Functionality not yet supported...")
        time.sleep(1)
        main_menu(user)

#quick menu
def quick_menu(user, message=""):

    #print menu
    output.header(user)
    if message != "":
        print(message)
    output.quick_menu()
    print("Please choose an option: ",end='',flush=True)
    key = ""

    #get valid choice
    while ( 
        key != "1" and key !="u" and key != "x" 
        ):
        key = functions.getch()

    print(key)
    time.sleep(.25)
    if key == "1":
        command = "update user "+ user.id + " password S@lvation7 changepassword on"
        gam_data = gam.preview_run(command,"Reset " + user.id + "'s password?")
        print()
        if gam_data.output != "":
            print(gam_data.output)
            print()
        input_to_continue()
        quick_menu(user)
    elif key == "x":
        print("   Returning to main Menu...")
        time.sleep(.5)
        main_menu(user)
    elif key == "u":
        user.exists = False
        output.header(user)
        user = functions.get_user()
        quick_menu(user)
    else: 
        print("   Functionality not yet supported...")
        time.sleep(1)
        main_menu(user)

#exit menu
def exit_menu(user, message=""):

    #print menu
    output.header(user)
    if message != "":
        print(message)
    output.exit_menu()
    print("Please choose an option: ",end='',flush=True)
    key = ""

    #get valid choice
    while ( 
        key != "1" and key != "2" and key != "3" and key != "4" 
        and key != "5" and key !="u" and key != "x" 
        ):
        key = functions.getch()

    print(key)
    time.sleep(.25)
    if key == "1":
        print()
        print("   Starting User Delegation Process...")
        time.sleep(1)
        functions.exit_delegation(user)
    elif key == "2":
        print()
        print("   Starting User Transfer Process...")
        time.sleep(1)
        functions.exit_transfer(user)
    elif key == "x":
        print("   Returning to main menu...")
        time.sleep(.5)
        main_menu(user)
    elif key == "u":
        user.exists = False
        output.header(user)
        user = functions.get_user()
        exit_menu(user)
    else: 
        print("   Functionality not yet supported...")
        time.sleep(1)
        exit_menu(user)
