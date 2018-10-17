import shutil
import os
source='C:/Users/user/Desktop'
txt='D:/txt'
for file in os.listdir(source):
    if file.endswith(".txt"):
        if not os.path.exists(txt):
            os.makedirs(txt)
        shutil.move(os.path.join(source,file),os.path.join(txt,file))
print "Operation successful"
    
