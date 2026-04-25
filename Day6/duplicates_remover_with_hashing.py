import os
import hashlib

folder_path = r"C:\Users\SAMIKSHA BHORE\Desktop\Test_Folder"

def get_hash(file_path):
    with open(file_path, "rb") as f:
        return hashlib.md5(f.read()).hexdigest()

hash_map = {}
duplicates = []

for file in os.listdir(folder_path):
    file_path = os.path.join(folder_path, file)

    if os.path.isdir(file_path):
        continue

    file_hash = get_hash(file_path)

    if file_hash in hash_map:
        duplicates.append(file_path)
    else:
        hash_map[file_hash] = file_path

print("Duplicates:")
for dup in duplicates:
    print(dup)