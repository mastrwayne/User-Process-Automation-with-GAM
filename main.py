#import useful things
import functions
import time
import subprocess
import output
import menus

user = functions.User("","",False)

###start program###
output.header(user)

#get valid user
user = functions.get_user()

#valid user established. prompt for commands
menus.main_menu(user)

