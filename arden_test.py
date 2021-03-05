#import useful thingssss
import subprocess
import os
import time

#prompt for username
user = input("Enter user:")

#remove any whitespace
user = user.replace(" ","")

#process username -> email
user_full = user
if "@" not in user:
    user_full+= "@adventures.org"

#output user email
print("User to process: "+user_full)

#pause for effect
time.sleep(1)
print() #empty line

#setup gam command variables
gam_location = os.path.expanduser("~/bin/gamadv-xtd3/gam")
gam_command = "whatis"
gam_input = [gam_location,gam_command,user]

#output gam command to be run
print("Running Command: gam",gam_command,user)
print()

#run gam command
return_code = subprocess.run(gam_input)
