import os

folder_path = r"C:\Users\SAMIKSHA BHORE\Desktop\Test_Folder"

files = [f for f in os.listdir(folder_path) 
         if os.path.isfile(os.path.join(folder_path, f))]

for i, file in enumerate(files):
    file_path = os.path.join(folder_path, file)

    name, ext = os.path.splitext(file)   # safer

    new_name = f"file_{i}{ext}"
    new_path = os.path.join(folder_path, new_name)

    os.rename(file_path, new_path)