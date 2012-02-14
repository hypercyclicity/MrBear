
import subprocess
import os

SCP = "scp"
IO = "-i"
IFILE = os.getcwd() + os.sep +  "MrBear001.pem"
VM = "bitnami@107.21.232.70"


TOP = "MBServer/"

subprocess.call([SCP, "-r", IO, IFILE, os.getcwd() + os.sep + "/server", VM + ":" + TOP])
exit()
walk = os.walk(os.getcwd() + "/server")

for e in walk:
    d = e[0]
    dir = d.split(os.sep + "server")[-1]
    dir = dir[1:]
    
    for file in e[2]:  
        sendto = VM + ":" + TOP + dir + os.sep
        tosend = d + os.sep + file
        print "Sending ", tosend, " to ", sendto
        subprocess.call([SCP, IO, IFILE, tosend, sendto])