#!/usr/bin/env python3

# If you clone the repo, I recommend using the script via a symlink:
# ln -s /Users/brian/rando-scripts/jira.py /Users/brian/jira

import webbrowser, sys, pyperclip

sys.argv

if len(sys.argv) > 1:  
  issue_number = ' '.join(sys.argv[1:])
else:  
  issue_number = pyperclip.paste()

webbrowser.open_new_tab("https://<company>.atlassian.net/browse/" + issue_number)

