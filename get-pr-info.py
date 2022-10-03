#!/usr/bin/env python3
import sys, os, re, xlsxwriter

# Requires you to have the GitHub CLI set up 
# 1. Install: brew install gh
# 2. Login: gh auth login

# Current method
# 1. Get list of commits by running something like  git log --pretty=oneline 2855fb6ff8181d83fa679db26c8bbddf839391fd..02914c17b9cfd4a81a9db5f650d1a1d378b14414 > oss-commits.txt
# 2. Get the PRs from the list of commits, ie the (#NUMBER) values. One way to do this is to copy/paste it all into a spreadsheet and split the cells on '(#'
# 3. Run this script with just the PR numbers.

# To do: 

# Automate getting the list of PRs. Ask Abhishek how he did it.
# Alternatively, the brute force way is ot 
# Get a list of commits by doing git log STARTING_HASH..ENDING_HASH > oss-commits.txt but that gives you a ton of other info you don't need
# From the commit msgs, grab the PR number

# Expects a new line delimited file with one PR number per line. There's no error handling right now, so your input needs to be clean.

source_file = open(os.path.join(os.path.dirname(__file__), "oss_commits.txt"), "r")

# Read the lines in a file
for line in source_file:
  PR_NUMBER = str(line.strip())
  # Call the GitHub cli client and grab the header, which has the title, author, state, labels, and URL and write it to a temporary file
  os.system (f"gh pr view {PR_NUMBER} --repo apache/druid | head >> pr-list.txt")

source_file.close()

# initialize spreadsheet
workbook = xlsxwriter.Workbook('pr-list.xlsx')
worksheet = workbook.add_worksheet()

worksheet.write_string(0,0, "URL")
worksheet.write_string(0,1, "Title")
worksheet.write_string(0,2, "Author")
worksheet.write_string(0,3, "Label")
worksheet.write_string(0,4, "Release note (Yes/No/Maybe")

row = 1
column = 0

pr_info = open("pr-list.txt", "r")

for line in pr_info:
  # Organized by the order they appear in the GitHub CLI info
  if line != None and "title" in line:
    # Search for the title field
    the_title = re.search("\t(.*)", line)
    #Qprint(the_title.group(0).lstrip())
    # Write the field to a cell in the second column
    worksheet.write_string(row, 1, the_title.group(0).lstrip())
  elif line != None and "author" in line:
    the_author = re.search("\t(.*)", line)
    #print(the_author.group(0).lstrip())
    worksheet.write_string(row, 2, the_author.group(0).lstrip())
  elif line != None and "labels" in line:
    the_labels = re.search("\t(.*)", line)
    #print(the_labels.group(0).lstrip())
    worksheet.write_string(row, 3, the_labels.group(0).lstrip())
  elif line != None and "url" in line:
    the_url = re.search("https:\/\/github\.com\/apache\/druid\/pull\/[0-9]+", line)
    #print(the_url.group(0).lstrip())
    worksheet.write_string(row, 0, the_url.group(0).lstrip())
    row +=1

workbook.close()

# Delete the temp file
os.remove("pr-list.txt")
