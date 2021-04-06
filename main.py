#import useful things
import functions
import time
import subprocess
import output

user = functions.User("","",False)

###start program###
output.header(user)

#get valid user
user = functions.get_user()

#valid user established. prompt for commands
functions.main_menu(user)

