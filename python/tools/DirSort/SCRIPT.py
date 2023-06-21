"""Sort dir files by extention"""
import os


def gather_files(directory: str) -> dict:
    """Gather and sort file by extention"""
    gathered_data = {}
    for file in os.listdir(directory):
        if os.path.isdir(os.path.join(directory, file)):  # Don't continue if file is not a file
            continue

        dot_hit = False
        extention = ''
        for character in file:
            if character == '.':  # Once character is designating an extension (file ->.<- txt)
                dot_hit = True
                continue
            if dot_hit is True:  # Add all characters after the '.' as the extention
                extention += character
        
        if not extention in gathered_data.keys():  # If extension name is not already in dictonary
            gathered_data.update({extention: []})
        gathered_data.get(extention).append((file, os.path.join(directory, file)))  # Append tuple of filename and path (filename, path)
    
    return gathered_data


if __name__ == '__main__':
    currect_directory = os.path.dirname(__file__)
    data = gather_files(currect_directory)

    for extension in data.keys():
        header = f"All [{extension}'s]"
        print(header)
        print('-' * len(header))
        for file in data.get(extension):  # for file (filename.extension, filename path)
            if not file[0] == os.path.basename(__file__):  # if current file is not main script
                extension_folder = os.path.join(currect_directory, extension)
                if not os.path.exists(extension_folder):  # Don't create folder if it already exists
                    os.mkdir(extension_folder)
                os.rename(file[1], os.path.join(extension_folder, file[0]))  # move file into folder
            print(f"{file[0]} : {file[1]}")
        print()
    
    