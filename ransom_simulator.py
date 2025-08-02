import os
import time

# Target folder (Desktop/TestFiles)
folder_path = os.path.expanduser("~/Desktop/TestFiles")

# Simulate encryption
for file_name in os.listdir(folder_path):
    file_path = os.path.join(folder_path, file_name)
    if os.path.isfile(file_path):
        os.rename(file_path, file_path + ".encrypted")

# Create ransom note
ransom_note_path = os.path.join(folder_path, "README.txt")
with open(ransom_note_path, "w") as note:
    note.write(
        "Your files have been encrypted!\n\n"
        "To decrypt them, send 100 Bitcoins to this fake address.\n"
        "This is a simulation. Do NOT panic.\n"
    )

# Simulate delay and pop-up
time.sleep(2)
os.system('msg * "Your files have been encrypted. Check README.txt."')
