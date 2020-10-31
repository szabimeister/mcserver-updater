###################
#       LOGO      #
###################

print("___  ____                            __ _     _____                            _   _           _       _            ")
print("|  \/  (_)                          / _| |   /  ___|                          | | | |         | |     | |           ")
print("| .  . |_ _ __   ___  ___ _ __ __ _| |_| |_  \ `--.  ___ _ ____   _____ _ __  | | | |_ __   __| | __ _| |_ ___ _ __ ")
print("| |\/| | | '_ \ / _ \/ __| '__/ _` |  _| __|  `--. \/ _ \ '__\ \ / / _ \ '__| | | | | '_ \ / _` |/ _` | __/ _ \ '__|")
print("| |  | | | | | |  __/ (__| | | (_| | | | |_  /\__/ /  __/ |   \ V /  __/ |    | |_| | |_) | (_| | (_| | ||  __/ |   ")
print("\_|  |_/_|_| |_|\___|\___|_|  \__,_|_|  \__| \____/ \___|_|    \_/ \___|_|     \___/| .__/ \__,_|\__,_|\__\___|_|   ")
print("                                                                                    | |                             ")
print("                                                                                    |_|                             ")

######################
#       Imports      #
######################
import requests
import os
import subprocess
from sys import platform
import sys
###############################
#       Global Variables      #
###############################
slash = ""
currentDirectory = ""
systemType = ""
##############################
#       Main functions       #
##############################
def systemtypef(): #decides whether to use forwardslash or backslash according to filepath in different operating systems
    global slash
    global systemType
    if platform == "linux" or platform == "linux2":
        systemType = "linux"
        print("OS DETECTED: GNU/LINUX\n\n\n")
        slash = "/"
    elif platform == "win32":
        systemType = "win"
        print("OS DETECTED: WINDOWS\n\n\n")
        slash = chr(92)
    elif platform == "darwin":
        systemType = "osx"
        print("OS DETECTED: OSX\n\n\n")
        slash = "/"

def get_cwd():
    global currentDirectory
    currentDirectory = os.getcwd() #gets the Current Working Directory
    print("This script is located in " + currentDirectory + "\nIt will be used as the install directory!\n\n\n\n")

def slashcheck():
    global currentDirectory
    if currentDirectory[-1] != slash:
        currentDirectory = currentDirectory + slash

def download_file():
    url = "https://launcher.mojang.com/v1/objects/f02f4473dbf152c23d7d484952121db0b36698cb/server.jar"
    print("Downloading server.jar to " + currentDirectory)
    r = requests.get(url) # create the HTTP response object
    rstr = str(r) #makes it into a string (debug purposes,and feedback for the user)

    if rstr == "<Response [200]>":
        print("Successfully grabbed URL! Downloading!!!\n\n")
    else:
        print(rstr)
        print("HTTP Response code abnormal! Aborting!!!\nIF THIS ISSUE PERSISTS github.com/szabi1035/Minecraft-spigot-updater/issues")
        sys.exit(0)

    with open(currentDirectory + "server.jar",'wb') as f: 
        # Saving received content as a jar file in 
        # binary format 
        # write the contents of the response (r.content) 
        # to a new file in binary mode.
        f.write(r.content)

def run_firststart():
    subprocess.call(['java', '-jar', 'server.jar'])

def run_prompt():
    answer = input("Would you like to run the server now? (Y/N) ")
    if answer == "Y":
        os.system('python3 runserverscript.py')
    elif answer == "N":
        sys.exit(0)
    else:
        print("Invalid input!")
        run_prompt()
##########################
#       Main execs       #
##########################
systemtypef()
get_cwd()
slashcheck()
download_file()
run_firststart()
run_prompt()