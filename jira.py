#!/usr/bin/env python3

# You can create the script manually or clone the script and use it script via a symlink:
# For example `ln -s /Users/brian/rando-scripts/jira.py /usr/local/bin/jira`
# Make sure you create an environment variable named JIRA_URL for your terminal, such as .zshenv.

import webbrowser, sys, pyperclip, os
jira_url = os.environ['JIRA_URL']
sys.argv

if len(sys.argv) > 1:  
  issue_number = ' '.join(sys.argv[1:])
else:  
  issue_number = pyperclip.paste()

webbrowser.open_new_tab(jira_url + issue_number)

