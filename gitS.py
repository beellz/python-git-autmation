import os
import sys
from time import sleep

os.system("git status")

os.system("git add *")


#sleep(2)
commit = sys.argv[1:]

NewC = str(commit)


print (f" The commit u are adding is  {NewC}")

#print (f" The commit u are adding is  {commit}")


os.system("git commit -m " +NewC)

os.system("git push -u origin master")
