import os
import shutil

path = input("Enter Path: ")
files = os.listdir(path)

for file in files:
    filename, extension = os.path.splitext(file)
    extension = extension[1:]

    # Create the directory if it doesn't exist
    if not os.path.exists(os.path.join(path, extension)):
        os.makedirs(os.path.join(path, extension))

    # Move the file to the directory corresponding to its extension
    shutil.move(os.path.join(path, file), os.path.join(path, extension, file))
