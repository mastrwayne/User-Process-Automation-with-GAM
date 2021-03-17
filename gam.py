import subprocess
import os
import time
import functions

gam_location = os.path.expanduser("~/bin/gamadv-xtd3/gam ")

class GamInfo:
    def __init__(self,returncode,output):
        self.returncode = returncode
        self.output = output

#run gam command function
def run(cmd, showerror=True):
    print()
    print(" > gam "+cmd)
    print("   waiting on gam...")
    print()
    full_cmd = gam_location + cmd
    split_cmd = full_cmd.split()
    result = subprocess.run(split_cmd,capture_output=True, text=True)
    if result.returncode != 0:
        ginfo = GamInfo(result.returncode,result.stderr)
        if showerror:
            show_gam_error(ginfo)
    else: 
        ginfo = GamInfo(result.returncode,result.stdout)
    
    return ginfo

#show gam error, ask abort
def show_gam_error(gam_data):
    print("GAM Error Occoured:")
    print("-----------------------")
    print(gam_data.output)
    print("-----------------------")
    functions.ask_abort()


#gam exit transfer process
def exit_transfer(user):
    #turn off directory sharing
    print()
    print("-- Directory Sharing --")
    time.sleep(.5)
    if functions.ask_confirm("Turn off directory sharing?"):
        gam_data = run("update user "+ user.id + " gal off")
        print(gam_data.output)
    time.sleep(.5)
    #remove from groups
    print()
    print("-- User Groups --")
    time.sleep(.5)
    print("Getting user groups...")
    gam_data = run("user " + user.id + " print groups role member", False)
    print(gam_data.output)
