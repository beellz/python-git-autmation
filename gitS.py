import os
import sys
import time

os.system("git status")

os.system("git add *")


time.sleep(2)
commit = sys.argv[1] 



print (f" The commit u are adding is  {commit}")



os.system("git commit -m {commit}")

