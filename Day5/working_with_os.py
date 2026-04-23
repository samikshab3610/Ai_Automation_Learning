# os module (Low-level control)

# The os module lets you talk directly to the operating system—files, folders, paths, environment variables, etc.
# Think of it as: “basic system operations”
# 🔑 Core concepts:
# Work with directories
# Handle file paths
# Execute system commands
# Get system info
# ⚠️ Important:
# os is manual and basic
# You handle things step-by-step
# Less safe for complex operations


import os

#Current working directory
# print(os.getcwd())

# Change directory
# os.chdir(r"C:\Users\SAMIKSHA BHORE\Desktop\Automation\Day5")
# print(os.getcwd())

# List files/folders
# print(os.listdir())

#create folder
# os.mkdir("Folder_made_by_os")

# Remove folder
# os.rmdir("Folder_made_by_os")