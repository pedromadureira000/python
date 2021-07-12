#!/home/phsw/.pyenv/versions/3.9.1/bin/python
import os
import sys

arguments = sys.argv
print(arguments)
if len(arguments) < 1:
    print("Missing arguments")
    print("-a to list all files in this folder")
    print("-d to list all directories in this folder")
    sys.exit()

only_files = False
if "-f" in arguments:
    only_files = True

only_directories = False
if "-d" in arguments:
    only_directories = True

for arquivo in os.listdir('.'):
    if only_files:
        if os.path.isfile(arquivo):
            print(arquivo)

    if only_directories:
        if os.path.isdir(arquivo):
            print(arquivo)