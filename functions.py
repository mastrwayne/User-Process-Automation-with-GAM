import subprocess
import os
import time

#User class
class User:
    def __init__(self, id, email, exists=False):
        self.id = id
        self.email = email
        self.exists = exists

class GamInfo:
    def __init__(self,returncode,output):
        self.returncode = returncode
        self.output = output

#gam function
def gam(cmd, showerror=False):
    gam_location = os.path.expanduser("~/bin/gamadv-xtd3/gam ")
    print(" > gam "+cmd)
    print("   waiting on gam...")
    full_cmd = gam_location + cmd
    split_cmd = full_cmd.split()
    result = subprocess.run(split_cmd,capture_output=True, text=True)
    if result.returncode != 0:
        if showerror:
            print("ERROR("+str(result.returncode)+"): ", result.stderr)
        ginfo = GamInfo(result.returncode,result.stderr)
    else: 
        ginfo = GamInfo(result.returncode,result.stdout)
    
    return ginfo

#get user function
def get_user():
    #prompt for username
    print()
    this_id = input("Enter User:")

    #remove any whitespace
    this_id = this_id.replace(" ","")

    #process username -> email
    this_email = this_id
    if "@" not in this_id:
        this_email+= "@adventures.org"

    return User(this_id,this_email)

#get key 
import termios, sys , tty
def getch():
   fd = sys.stdin.fileno()
   old_settings = termios.tcgetattr(fd)
   try:
      tty.setraw(fd)
      ch = sys.stdin.read(1)     #This number represents the length
   finally:
      termios.tcsetattr(fd, termios.TCSADRAIN, old_settings)
   return ch