
import subprocess
import os

SCP = "scp"
IO = "-i"
IFILE = os.getcwd() + os.sep +  "MrBear001.pem"
VM = "bitnami@107.21.232.70"


TOP = "MBServer/"

subprocess.call([SCP, "-r", IO, IFILE, os.getcwd() + os.sep + "server", VM + ":" + TOP])
