#!/usr/bin/env python3
import webbrowser, sys, pyperclip

sys.argv

if len(sys.argv) > 1:  
  issue_number = ' '.join(sys.argv[1:])
else:  
  issue_number = pyperclip.paste()

webbrowser.open_new_tab("https://armory.atlassian.net/browse/" + issue_number)

