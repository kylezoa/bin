#for only kylezoa.com html files
#because hosts change and things get annoying with static files

import os, sys, re
from time import sleep

#strings
strFind = "<a href="http://www.wilsonadams.net">Host by Wilson Adams Design</a><br/>"
strToRe = "<a href="https://clients.thrustvps.com/aff.php?aff=128">Host by ThrustVPS</a><br/>"
    
#input wanted directory
path = input ("directory: ")

#change to <path>
os.chdir(path)
#confirm if directory is correct
print ("Making changes in", os.getcwd(), "you have three seconds to kill")
sleep (3)

#list then find .html files and assemble it into a list to edit

os.listdir(path)

