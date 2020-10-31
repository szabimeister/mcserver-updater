import os
import subprocess
from sys import platform

systemType = ""


def systemtypef(): #decides whether to use forwardslash or backslash according to filepath in different operating systems
    global systemType
    if platform == "linux" or platform == "linux2":
        systemType = "linux"
    elif platform == "win32":
        systemType = "win"
    elif platform == "darwin":
        systemType = "osx"
systemtypef()

def run_serverfile():
    allocramamount = input("How much memory do you want to allocate to the server(in megabytes)? ")
    if systemType == "win":
        subprocess.call(['java', '-jar', '-Xms' + allocramamount + 'm','-Xmx' + allocramamount + 'm', 'server.jar'])
    elif systemType == "linux" or "osx":
        subprocess.call(['java', '-jar', '-Xms' + allocramamount + 'M','-Xmx' + allocramamount + 'M', 'server.jar'])
run_serverfile()