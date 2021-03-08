#import useful thingssss
import subprocess
import os
import time

#prompt for username
user = input("Enter User:")

#remove any whitespace
user = user.replace(" ","")

#process username -> email
user_full = user
if "@" not in user:
    user_full+= "@adventures.org"

#output user email
print()
print("Processing User: "+user_full)

#pause for effect
time.sleep(1)
print() #empty line

#setup gam command variables
gam_location = os.path.expanduser("~/bin/gamadv-xtd3/gam")
#gam_command = "user"
gam_input = [gam_location,"info","user",user]

#output gam command to be run
print("Running Command: gam info user",user)
print()

#run gam command
result = subprocess.run(gam_input,capture_output=True, text=True)
if result.returncode != 0:
    print("ERROR("+str(result.returncode)+"): ", result.stderr)
else :
    print(result.stdout)

