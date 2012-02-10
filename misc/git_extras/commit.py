

#This is a script I wrote that replaces the git commit command, it allows you to
#use:
# $> gcommit This is my comment
#Instead of
# $> git commit -m "This is my comment"


import os
import sys
import subprocess

#script_util imports
sys.path.insert(0, os.getenv("SCRIPT_UTIL"))
import arguements


args = sys.argv
args.pop(0)

message = " '"
first = True

for str in args:
    if not first:
        message += " " 
    else:
        first = False
    message += str
    
    
message += "' "

command = ['git', 'commit', '-m', message]

subprocess.call(command)
