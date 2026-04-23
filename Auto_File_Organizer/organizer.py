import os
import shutil

# Folder path 
folder_path = r"C:\Users\SAMIKSHA BHORE\Documents"

file_types = {
    "Images" : ["jpg", 'png', 'jpeg'],
    "Documents" : ['pdf', 'txt', 'docx'],
    "Audio": ['mp3', 'wav'],
    "Videos" : ['mp4', 'mkv']
}


for file in os.listdir(folder_path):
    file_path = os.path.join(folder_path, file)


    # Skip folders
    if os.path.isdir(file_path):
        continue

    # Get extension
    ext = file.split(".")[-1].lower()

    moved = False

    for folder, extensions in file_types.items():
        if ext in extensions:
            dest = os.path.join(folder_path, folder)

            if not os.path.exists(dest):
                os.makedirs(dest)

            shutil.move(file_path, os.path.join(dest, file))
            moved = True
            break    

    if not moved:
        other = os.path.join(folder_path, 'others')
        if not os.path.exists(other):
            os.makedirs(other)

        shutil.move(file_path, os.path.join(other,file))        
    

