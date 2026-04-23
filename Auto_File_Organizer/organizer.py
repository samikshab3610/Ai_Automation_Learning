import os
import shutil

# Folder path 
folder_path = r"C:\Users\SAMIKSHA BHORE\Downloads"

# Get all files
files = os.listdir(folder_path)

for file in files:
    file_path = os.path.join(folder_path, file)

    # Skip folders
    if os.path.isdir(file_path):
        continue

    # Get extension
    ext = file.split(".")[-1]

    #create folder based on extension
    dest_folder = os.path.join(folder_path, ext.upper())

    if not os.path.exists(dest_folder):
        os.makedirs(dest_folder)

    # Move file
    shutil.move(file_path, os.path.join(dest_folder, file))

