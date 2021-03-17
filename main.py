#import useful things
import functions
import time
import subprocess

subprocess.run(["clear"])
print("------------------------------------------------------")
print("          GAM User Process Automation")
print("------------------------------------------------------")

###start program###

#get valid user
user = functions.get_user()

#valid user established. prompt for commands
functions.exit_menu(user)

