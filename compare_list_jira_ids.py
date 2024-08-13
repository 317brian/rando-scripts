import re
import sys

# Expects 2 txt files, namely the output of the jira_scrape script
# The idea is that the first argument is the earlier scrape (e.g. preview 1) and the second argument is the later scrape (e.g. preview 2).

# Example command:
# python diff_release_notes.py preview1.txt preview2.txt

# Read the file and pull out the lines with Jira IDs
def read_lines_with_ids_from_file(filename):
    with open(filename, 'r') as file:
        lines = file.readlines()
        lines_with_ids = {}
        current_heading = None

        for line in lines:
            # Check for heading (lines that start with "####")
            heading_match = re.match(r'^####\s*(.*)', line)
            if heading_match:
                current_heading = heading_match.group(1).strip()
                continue

            # Match lines that contain an ID
            id_match = re.search(r'\bid:\s*(\d+)\b', line)
            if id_match and current_heading:
                # Store the full line and the current heading
                lines_with_ids[id_match.group(1)] = {
                    'line': line.strip(),
                    'heading': current_heading
                }
        
        return lines_with_ids

if len(sys.argv) != 3:
    print("Usage: python diff_release_notes.py <preview1.txt> <preview2.txt>")
    sys.exit(1)

# Read the lines with IDs from the two text files
old_list = sys.argv[1]
new_list = sys.argv[2]

old_jiras = read_lines_with_ids_from_file(old_list)
new_jiras = read_lines_with_ids_from_file(new_list)

# Find lines with Jiras only in preview 1
only_in_preview1 = {id: info for id, info in old_jiras.items() if id not in new_jiras}

# Find lines with Jiras only in preview 2
only_in_preview2 = {id: info for id, info in new_jiras.items() if id not in old_jiras}

# Print results
if only_in_preview1:
    print("\n**These Jiras are only in the old list. Remove them from release.md:**\n")
    for jira_info in only_in_preview1.values():
        print(f"- [{jira_info['heading']}] {jira_info['line']}")
else:
    print("No Jiras removed.")

if only_in_preview2:
    print("\n**These Jiras were added in the new list. Add them to release.md:**\n")
    for jira_info in only_in_preview2.values():
        print(f"- [{jira_info['heading']}] {jira_info['line']}")
else:
    print("No new Jiras.")
