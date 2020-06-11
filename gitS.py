import os
import sys
from time import sleep

os.system("git status")

os.system("git add *")


#sleep(2)
commit = str(sys.argv[1])



print (f" The commit u are adding is  {commit}")



os.system("git commit -m"+commit)

