

import shutil
import os

sourceFolder = 'C:\Users\user\Desktop\c projects'
destFolder = 'D:'


#for every file in the folder
for node in os.listdir(sourceFolder):
    #move the file to another folder
    shutil.move(os.path.join(sourceFolder, node), os.path.join(destFolder,node))
    #print the new location
    print "Operation successful"
    print node,os.getcwd()