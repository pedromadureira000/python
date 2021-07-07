import os
import shutil

path = "/home/phsw/Downloads/layoutit/outrapasta"
path2 = "/home/phsw/Downloads/layoutit/pasta"

try:
    os.mkdir(path2)
except FileExistsError as FileExists:
    print(f'File Already exists.')

for root, dirs, files in os.walk(path):
    for file in files:

        old_file_path = os.path.join(root, file)
        new_file_path = os.path.join(path2, file)
        if '.map' in file:
            shutil.copy(old_file_path, new_file_path)  # move, copy,
            print(root, file, dirs)
            print(f'file {file} copied successfully to {path2}.')
        if '.map' in file: # delete from old file path
            os.remove(old_file_path)
            print(f'file {file} deleted successfully from {root}')