"""Sort dir files by extension"""
import os


def gather_files(directory: str) -> dict:
    """Gather and sort file by extension"""
    gathered_data = {}

    if not os.path.exists(directory):
        print(f"Directory '{directory}' does not exist")
        return gathered_data
    if not os.path.isdir(directory):
        print(f"'{directory}' is not a directory")
        return gathered_data
    files_in_directory = [file for file in os.listdir(directory) if os.path.isfile(os.path.join(directory, file))]  # List of only files in directory
    if ( len(files_in_directory) == 1 and os.path.basename(__file__) in os.listdir(directory) ) or ( not len(files_in_directory) ):  # If only file in directory is this script or no FILES in directory
        print(f"No files in '{directory}' to sort")
        return gathered_data

    print(f"Gathering files in {directory}...")
    for file in os.listdir(directory):
        if os.path.isdir(os.path.join(directory, file)):  # Don't continue if file is directory
            continue

        extension = os.path.splitext(file)[1][1:]  # Get last file extension (filename.pdf.txt -> txt)
        if not extension:  # If file has no extension
            extension = 'NOEXTENSION'
        print(extension)
        if not extension in gathered_data:
            gathered_data.update({extension: []})
        gathered_data[extension].append((file, os.path.join(directory, file)))  # Append tuple of filename and path (filename, path)
    
    return gathered_data


def move_file(source, destination):
    """
    Move the file to the destination path
    If destination path already exists, rename the file with index
    """
    if os.path.exists(destination):
        file_name, file_extension = os.path.splitext(os.path.basename(source))
        index = 1
        while True:
            new_file_name = f"{file_name}_{index}{file_extension}"
            new_destination = os.path.join(os.path.dirname(destination), new_file_name)
            if not os.path.exists(new_destination):
                os.rename(source, new_destination)
                break
            index += 1
    else:
        os.rename(source, destination)


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
                    os.makedirs(extension_folder)
                move_file(file[1], os.path.join(extension_folder, file[0]))
            print(f"{file[0]} : {file[1]}")
        print()
