import os
from datetime import date
import time


first_path = input("folder 1 path:")
second_path = input("folder 2 path:")
first_path_len = len(folder1_path)
second_path_len = len(folder2_path)
choice = input("check only .exe files? y/n\n->")
file_type_to_check = ".exe" if choise == 'y' else "" 
print("\nfolder1:")
dic_files1 = {}

# r=root, d=directories, f = files
for root, dirs, files in os.walk(folder1_path):
    for file in files:
        file_path = os.path.join(root, file)
        if file_type_to_check in file_path:
            dic_files1[file_path[folder1_path_len:]] = os.path.getsize(file_path)

for f in dic_files1.keys():
    print(f)
    
print("\nfolder2:")
dic_files2 = {}
for r, d, f in os.walk(folder2_path):
    for file in f:
        file_path = os.path.join(r, file)
        if file_type_to_check in file_path:
            dic_files2[file_path[folder2_path_len:]] = os.path.getsize(file_path)

for f in dic_files2.keys():
    print(f)

counter = 0
print("\nfiles that found infected:")
for key, value in dic_files1.items():
    if not dic_files2[key] == value:
        print(key)
        modTimesinceEpoc = os.path.getmtime(folder1_path + key)
        modificationTime = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(modTimesinceEpoc))
        print(f"last changed:{modificationTime}")
        counter += 1

print(f"num files that found infected:{counter}")
print(f"date:{date.today()}")
print(f"folder 1:{folder1_path}")
print(f"folder 2:{folder2_path}")
print(f"num of files that scaned:{len(dic_files1.keys())}")


