import hashlib
import os
from tkinter import Tk
from tkinter.filedialog import askdirectory

from termcolor import colored

# prevent FullScreen
Tk().withdraw()


# function to print on which folder I am in the walker and to improve terminal Readability
def print_red(x):
    return print(colored(x, "red"))


# A GUI that will ask the user for the wanted folder
rootfolder = askdirectory(title="Select a folder")

# Now what we need is all the file paths in the whole directory tree
# first we need to define a walker that will iterate through the whole directory tree
walker = os.walk(rootfolder)

# then we should add all filepaths to an array
# Dictionnary with hash as key and filepath as value
# if a filehash is found in the dictionnary it means it is a duplicate
# NOTE
# BLAKE2 was used instead of MD5 as hashing algorithm
#
UniqueFiles = dict()

for folder, sub_folders, files in walker:
    print_red(f"Starting with {folder} now")
    for f in files:
        filepath = os.path.join(folder, f)
        filehash = None
        with open(filepath, "rb") as f:
            filehash = hashlib.blake2b(f.read()).hexdigest()

        if filehash in UniqueFiles:
            os.remove(filepath)
            print(f"{filepath} has been Removed!")
        else:
            UniqueFiles[filehash] = filepath
