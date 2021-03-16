#import useful things
import functions
import time

user = functions.User("","")

###start program###

#get valid user
while user.exists == False:
    user = functions.get_user()
    time.sleep(.25)
    print("Checking to see if",user.id,"exists...")
    time.sleep(.25)

    gam_data = functions.gam("info user " + user.id)

    if gam_data.returncode == 0:
        print("User",user.email,"exists.")
        print("Continue? y/n ",end='', flush=True)
        key = ""
        while key != "y" and key != "n":
            key = functions.getch()
        print(key)
        time.sleep(.25)
        if key == "n":
            print("quitting...")
            exit()
        user.exists = True
    else:
        print("User doesn't exist, please try again")
        time.sleep(.2)

#valid user established. start running commands
print("nothing to do yet...")
