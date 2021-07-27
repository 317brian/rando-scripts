#!/usr/bin/env python3

# Clone the repo or just copy the contents of this file to a python (.py) file. Update the URL on line 16 to the URL for your Jira instance.
# Save it somewhere that's already in your PATH or add it to your PATH
# Use it by running the following command: jira <key>-issue_number. For example jira doc-412

import webbrowser, sys, pyperclip

sys.argv

if len(sys.argv) > 1:  
  issue_number = ' '.join(sys.argv[1:])
else:  
  issue_number = pyperclip.paste()

webbrowser.open_new_tab("https://<company>.atlassian.net/browse/" + issue_number)

