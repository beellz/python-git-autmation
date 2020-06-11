import os
import sys

os.system("git status")

os.system("git add *")
commit = sys.argv[1] 


print (f" The commit u are adding is  {commit}")



os.system("git commit -m {commit}")

