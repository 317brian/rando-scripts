#!/usr/bin/env python3

import sys, pyperclip, os

# Get the latest copy of the repo.

os.system("git checkout master || git checkout main")
os.system("git pull --rebase")

if len(sys.argv) > 1:  
  branch_name = ' '.join(sys.argv[1:])
else:  
  branch_name = pyperclip.paste()


os.system (f"git checkout {branch_name} && git diff --name-only origin/master > file_list.txt" )

# iterate through the file list and open the files
f = open("file_list.txt", "r")
for modified_file in f:
  print(modified_file)
  os.system(f"open {modified_file}")

# close the file
f.close()

# delete file list
os.remove("file_list.txt")
