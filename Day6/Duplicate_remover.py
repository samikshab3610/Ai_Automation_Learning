import os

folder_path = r"C:\Users\SAMIKSHA BHORE\Desktop\Test_Folder"

files = os.listdir(folder_path)

seen_sizes = {}
duplicates = []

for file in files:
    file_path = os.path.join(folder_path, file)

    if os.path.isdir(file_path):
        continue

    size = os.path.getsize(file_path)

    if size in seen_sizes:
        duplicates.append(file_path)
    else:
        seen_sizes[size] = file_path

#print duplicates
print("Duplicate files: ")
for dup in duplicates:
    print(dup)            
    

# delete duplicates
for dup in duplicates:
    os.remove(dup)
    print(f"Deleted: {dup}")    