import re
import sys

# Expects 2  txt files, namely the output of the jira_scrape script
# The idea is that first argument is the earlier scrape (e.g. preview 1) and second argument is the later scrape (e.g. preview 2).

# Example command:
# python diff_release_notes.py preview1.txt preview2.txt

# Read the file and pull out the Jira IDs
def read_lines_with_ids_from_file(filename):
    with open(filename, 'r') as file:
        lines = file.readlines()
        lines_with_ids = {}
        for line in lines:
            match = re.search(r'\bid:\s*(\d+)\b', line)
            if match:
                # Store the line using the ID as the key
                lines_with_ids[match.group(1)] = line.strip()
        return lines_with_ids

# Needs 2 files
if len(sys.argv) != 3:
    print("Usage: python diff_release_notes.py <preview1.txt> <preview2.txt>")
    sys.exit(1)

# Read the lines with IDs from the two text files
preview1 = sys.argv[1]
preview2 = sys.argv[2]

preview1_jiras = read_lines_with_ids_from_file(preview1)
preview2_jiras = read_lines_with_ids_from_file(preview2)

# Find lines with Jiras only in list1
only_in_preview1 = {id: line for id, line in preview1_jiras.items() if id not in preview2_jiras}

# Find lines with Jiras only in list2
only_in_preview2 = {id: line for id, line in preview2_jiras.items() if id not in preview1_jiras}

# Print results
if only_in_preview1:
    print("\n**These Jiras are only in preview 1. Remove them from release.md:**\n")
    for line in only_in_preview1.values():
        print(f"- {line}")
else:
    print("No Jiras removed.")

if only_in_preview2:
    print("\n**These Jiras are new in preview 2. Add them to release.md:**\n")
    for line in only_in_preview2.values():
        print(f"- {line}")
else:
    print("No new Jiras.")
