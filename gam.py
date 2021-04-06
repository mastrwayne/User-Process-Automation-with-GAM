import subprocess
import os
import time
import functions
import output

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

def preview_run(cmd, message, showerror = True):
    print()
    print(message)
    print(" > gam " + cmd)
    if functions.ask_confirm():
        ginfo = run(cmd,showerror)
        return ginfo
    else: 
        return GamInfo(0,"")
    

#show gam error, ask abort
def show_gam_error(gam_data):
    print("GAM Error Occoured:")
    print("------------------------------")
    print(gam_data.output)
    print("------------------------------")
    functions.ask_abort()
