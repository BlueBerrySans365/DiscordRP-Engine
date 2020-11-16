## Global import's
import pypresence ## Main module (:D Yep, this is the main module in this script)
import time ## Time module (Will be used in time.sleep())
import os ## File managing module (Monika will help xD)
import sys ## Still can't remember for what it used .w.
import datetime ## Date and Time module (Hehe :D)
import json ## Umm... Really? I don't know



## Local import's
from Configs.log import addLog as aal  ## Logging operations
from Configs.log import debugHelp as dgh  ## Send the same message each time
from Configs.config import configs as c  ## Configurations


## To add your local modules add [ from (your file name without .py) import (def or classes name) (optional [ as (name or letter for def/classes) ]
## Or if your modules in other folder add in [ from (your file name without .py) ...] name of folder [ from (your folder name).(your file name without .py) ].


## Starter script
try:
    import pypresence as pypr
    from json import loads  ## API uses json
    import requests  ## Connection to API requires requests
except Exception as e: # If# module could not be imported
    print("[!] We ran in to a problem. " + str(e)) ## Let the user know there was a problem
    dgh() # Print the debug message
    aal("FTL","Failed to import a module: " + str(e)) # Output error to log



aal("LOD", c.application_name + " v" + c.version + " started. Thanks for using DiscordRP-Engnine :)")  ##  Test logging
aal("LOD", "If you ever need to debug something, please send this log to https://discord.gg/yTxrCGR.") 



try:
    open(".nocol", "r")  ## If we can open .nocol, it must exist
    from Configs.color import nocolours as p  ## Import the disabled colour scheme
    aal("INF", "Disable terminal color")  ## Output info to log
except:
    from Configs.color import colours as p  ## Import the enabled colour scheme
    aal("INF", "Enable terminal color")  ## Output info to log



## Connectig to application
rpc = pypr.Presence(c.application_DID)
rpc.connect()



## Def's for commands UwU

def setStatus(silent,large,small,ltext,stext,details,state):  ## This is default def for changing presence
    try:
        rpc.update(large_image=large,small_image=small,large_text=ltext,small_text=stext,details=details,state=state,start=int(time.time())) # Update presence
        aal("INF","Updated presence: " + str(silent) + ", " + str(large) + ", " + str(small) + ", " + str(ltext) + ", " + str(stext) + ", " + str(details) + ", " + str(state)) # Output presence to log
        if silent == 0:
            print(p.success + "Presence updated.") # Give success message
    except Exception as e:
        print(p.fail + "There was a problem updating your presence: " + str(e)) # Presence update failed, print error message
        aal("ERR","Couldn't update presence: " + str(e)) # Output error to log
        aal("ERR","Failed presence:" + str(silent) + ", " + str(large) + ", " + str(small) + ", " + str(ltext) + ", " + str(stext) + ", " + str(details) + ", " + str(state)) # Output presence to log


def info(): ## This def for info command
    print(p.info + " " + c.application_name + "App v" + c.version + " | Made with DiscordRP Engine! ")
    if c.version != webver:
        print(p.info + " Needs update?: Yes")
    if c.version == webver:
        print(p.info + " Needs update?: No")


def help():
    print(p.info + "--------------------------------------------------------------------------")
    print(p.info + "lobby         ---  Application lobby (Default).                           ")
    print(p.info + "default       ---  Application lobby (Server Lobby).                      ")
    print(p.info + "help          ---  Help command.                                          ")
    print(p.info + "info          ---  Application information.                               ")
    print(p.info + "--------------------------------------------------------------------------")


def menu():
    setStatus(1, "bigimagekay", "smallimagekey", c.version + "|" + c.version_name,
              "smallimagetext", "Details", "Status")  # Default presence

    while True:
        opt = input(p.cmd)
        if opt == ("default"): ## Early opt was used like opt.startswith
            setStatus(0, "bigimagekay", "smallimagekey", c.version + "|" + c.version_name,
              "smallimagetext", "Details", "Status")


        elif opt == ("lobby"):
            setStatus(0, "bigimagekay", "smallimagekey", c.version + "|" + c.version_name,
              "smallimagetext", "Details", "Status")


        elif opt == ("help"):
            help()


        elif opt == ("info"):
            info()




## Scripts .w.

print(p.smile + "Welcome to " + c.application_name + " v" + c.version + "!")
webver = str(requests.get(c.version_url).text[:4])
if c.version != webver:
    print(p.warn + "You're out of date! The current version on " + c.devwebsite_name + " is " + webver + ". Update at " + c.devwebsite + "!")
else:
    print(p.success + "You're up-to-date. Thanks for using " + c.application_name + "!")
print(p.warn + "Questions, comments, rants? Head to [issue or repo link] or [Discord link]!")


try:
    menu()
except KeyboardInterrupt:
    print()
    print(p.warn + "Exiting...")
    aal("ERR", "Exited via keyboard interrupt with status code 1")


