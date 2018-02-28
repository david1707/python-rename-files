import os

number = 1

path = input("Path of the files:\n")
new_name = input("New name for the files:\n")
extension = input("What type of files do you want to affect?\n").lower()

if extension == 'images':
    extension = ['png', 'jpg', 'bmp', 'jpeg']
    extensionFinal = input("What type of file do you want to convert to?:\n").lower().replace('.', '')

else:
    extensionFinal = extension.replace('.', '')

files = [file for file in os.listdir(path) if os.path.isfile(''.join(path+file))]

for file in files:
    if file.split('.',)[1] in extension:
        print("Entra")  # ToDo
        os.rename(''.join(path+file), ''.join(path + new_name + "_" + str(number) + "."+extensionFinal))
        number += 1
