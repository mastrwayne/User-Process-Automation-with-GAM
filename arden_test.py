import subprocess
import os
import time

user = input("Enter user:")

user_full = user
if "@" not in user:
    user_full+= "@adventures.org"

print("User to process: "+user_full)
time.sleep(1)
print()
gam_location = os.path.expanduser("~/bin/gamadv-xtd3/gam")
gam_command = "whatis"
gam_input = [gam_location,gam_command,user]
print("Running Command: gam",gam_command,user)
print()

#list_files = os.popen(gam_input)

list_files = subprocess.run(gam_input)
