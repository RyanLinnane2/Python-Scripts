"""Script allowing users to create and name multiple folders and subfolders through a text file"""

import os

# file to read from
file_name = r"C:\Users\ryanl\Desktop\folder_maker.txt"
folder_directory = input("Enter the directory for the new folders to be created: ")


# open text file on desktop to create folders

def make_folder(path):
    try:
        os.mkdir(path)
    except OSError as err:
        print("OS error: {0}".format(err))


with open(file_name, encoding="utf-8") as f:
    for line in f:
        # remove \n at end of the each line
        line = line.strip()
        if '/' in line:
            # split the line into a list of words (folder names) seperated by the '/' symbol
            folder_names = line.split("/")
            path = os.path.join(folder_directory, folder_names[0])
            # variable to be updated with each directory as it is created
            prev_path = path
            # create the first parent folder outside of the loop
            make_folder(path)
            i = 0
            while i + 1 < len(folder_names):
                # the next name in the list is added the directory of the last folder created
                path = os.path.join(prev_path, folder_names[i + 1])
                prev_path = path
                # create the new folder
                make_folder(path)
                i += 1
        else:
            # for folders with no sub-folders specified
            path = os.path.join(folder_directory, line)
            prev_folder = path
            make_folder(path)

print("Folder Creation complete")
