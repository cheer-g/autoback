import shutil
import os
source='C:/Users/user/Desktop'
txt='D:/txt'
c='D:/txt'
random='D:/random'
for file in os.listdir(source):
    if file.endswith(".txt"):
        if not os.path.exists(txt):
            os.makedirs(txt)
        shutil.move(os.path.join(source,file),os.path.join(txt,file))
    elif file.endswith(".c"):
        if not os.path.exists(c):
            os.makedirs(c)
        shutil.move(os.path.join(source,file),os.path.join(c,file))
    else:
        if not os.path.exists(random):
            os.makedirs(random)
        shutil.move(os.path.join(source,file),os.path.join(random,file))
print "Operation successful"
    
