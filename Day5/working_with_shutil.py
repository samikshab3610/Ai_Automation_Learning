# The shutil module is built on top of os. It’s designed for file management in bulk or complex tasks.

# Think of it as: “power tools for file handling”

# 🔑 Core concepts:
# Copy files/folders
# Move files
# Delete directories safely
# Archive (zip/unzip)

import shutil

#copy file
# shutil.copy("source.txt", "destination.txt") #here destion.txt is copy of source

# Copy entore folder
# shutil.copytree("folder1", "folder2")  #here folder2 is copy of folder1 means folder1 = source  folder2 = destination

# Move file
# shutil.move("file.txt", r'C:\Users\SAMIKSHA BHORE\Desktop\Automation\Day5\folder2/file.txt')

# Delete folder
# shutil.rmtree("folder2")
