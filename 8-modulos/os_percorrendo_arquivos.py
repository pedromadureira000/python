import os

# print(os.getcwd())  # mostra o path atual
# os.chdir('/home/phsw/PycharmProjects/python/')  # muda pra esse diretorio
# print(os.getcwd())
#os.path.isfile(file_path)

# -------/ verificar todos os diretorios e arquivos de um diretorio
path_search = input("type a path") # a partir do diretorio '/'
term_search = input('type a pattern to search')
count = 0

if path_search == "":
    path_search = '/home/phsw/Downloads'  # a partir do diretorio '/'
if term_search == "":
    term_search = '.map'



def format_size(file_size):
        base = 1024
        kilo = base
        mega = base ** 2
        giga = base ** 3
        tera = base ** 4
        peta = base ** 5

        if file_size < kilo:
            text = "B"
        elif file_size < mega:
            file_size /= kilo
            text = "M"
        elif file_size < giga:
            file_size /= mega
            text = "G"
        elif file_size < tera:
            file_size /= giga
            text = "T"
        elif file_size < peta:
            file_size /= tera
            text = "P"
        file_size = round(file_size, 2)
        return f'{file_size}{text}'.replace('.', ',')

print(os.walk(path_search))
for root, dirs, files in os.walk(path_search):
    # print(root) # path starting in /home
    # print(dirs) # list with all directories
    # print(files) # list with all files
    for file in files:
        if term_search in file:
            try:
                count += 1
                file_path = os.path.join(root, file)
                file_name, file_ext = os.path.splitext(file)
                file_size = os.path.getsize(file_path)  # will be in bytes
                print("Find the file: ", file_path)
                print("with file name: ", file_name)
                print("with extension: ", file_ext)
                print("with size: ", file_size)
                print("with formated size: ", format_size(file_size))
                print("______________")
            except PermissionError as PermissionError:
                print("Without permissions")
            except FileNotFoundError as FileNotFoundError:
                print("The file was not found")
            except Exception as GeneralException:
                print("Unknow error")
print()
print(f'{count} files found')