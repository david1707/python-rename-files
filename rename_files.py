import os

def rename_files():
    number = 1

    # Get path and make sure it ends with a \
    path = input("Path of the files:\n")
    if not path.endswith("\\"):
        path = path + "\\"

    new_name = input("New name for the files:\n")
    extension = input("What type of files do you want to affect?\n").lower()

    # User can use 'images' to rename every single image despite the extension
    if extension == 'images':
        extension = ['png', 'jpg', 'bmp', 'jpeg']
        extension_final = input("What type of file do you want to convert to?:\n").lower().replace('.', '')

    else:
        extension_final = extension.replace('.', '')

    files = [file for file in os.listdir(path) if os.path.isfile(''.join(path+file))]

    for file in files:
        if file.split('.',)[1] in extension:
            os.rename(''.join(path+file), ''.join(path + new_name + "_" + str(number) + "."+extension_final))
            number += 1


while True:
    rename_files()

    repeat = input("Done.\nDo you want to rename more files? (Y/N)\n").lower()
    if repeat == "n":
        break

print("Closing....")
