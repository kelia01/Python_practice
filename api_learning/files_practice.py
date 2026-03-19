"""
A simple notes app that saves to a file.
Run it multiple times - your notes persist!
"""

import json
import os

FILENAME = "notes.json"

# YOUR CODE HERE
# 1. Check if FILENAME exists
#    - If yes, load the notes from it
#    - If no, start with empty list []

# 2. Show current notes (if any)

# 3. Ask user: "Add a note? (y/n): "
#    - If 'y', get input and add to notes

# 4. Save notes back to FILENAME

def save_notes(notes):

    if os.path.exists(FILENAME):
        with open(FILENAME, 'r') as f:
            return  json.load(f)
        return []

    title = input("Enter the title of ur notes")
    content = input("Enter ur content")

    note = {
        "title": title,
        "content": content
    }
    notes.append(note)

    # Show notes
    if not notes:
        print("No notes yet")
        return
    print("Your contacts are:\n")
    for n in notes:
        print(f"The {n.title} is and talks about {n.content}")

    #Save the notes in the file again
    with open(FILENAME, 'w') as f:
        json.dump(notes, f, indent=2)


print("Done! Check your notes.json file")