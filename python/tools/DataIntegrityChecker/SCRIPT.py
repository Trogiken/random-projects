"""Create hash for each file in a directory and subdirectories to check for data integrity."""

# import modules
import os
import sys
import hashlib
import json
import logging
from PyQt6.QtWidgets import QApplication, QFileDialog


logging.basicConfig(level=logging.WARNING, format='%(asctime)s - %(levelname)s - %(message)s')


def ask_filelocation(title: str, name_filter: str) -> str:
    """Return the file path of the file selected."""
    file_dialog = QFileDialog()
    file_dialog.setWindowTitle(title)
    file_dialog.setFileMode(QFileDialog.FileMode.AnyFile)
    file_dialog.setNameFilter(name_filter)

    if file_dialog.exec():
        return file_dialog.selectedFiles()[0]
    else:
        print('Canceled')
        sys.exit()

def ask_directory(title: str) -> str:
    """Return the directory path of the directory selected."""
    directory_dialog = QFileDialog()
    directory_dialog.setWindowTitle(title)
    directory_dialog.setFileMode(QFileDialog.FileMode.Directory)

    if directory_dialog.exec():
        return directory_dialog.selectedFiles()[0]
    else:
        print('Canceled')
        sys.exit()


def create_hash(file_path: str) -> str:
    """Create hash from file bytes, return hash as a string if found."""
    try:
        with open(file_path, 'rb') as file:
            file_read = file.read()
            file_hash = hashlib.sha256(file_read).hexdigest()
            return file_hash
    except BaseException as error:
        logging.error(f"Failed to hash '{file_path}' | {error}")
        return None

def create_hash_dict(directory_path: str) -> dict:
    """Walk through a directory and subdirectories to create a dictionary of hashes for each file."""
    hash_dict = {'attributes': {'working_directory': directory_path},
                 'hashes': {}}  # create dictionary with working directory as attribute

    print('\nCreating Hash Dictionary...\n')
    hashes = hash_dict['hashes']
    for root, _, files in os.walk(directory_path):
        for file in files:
            file_path = os.path.join(root, file)
            calculated_hash = create_hash(file_path)
            if calculated_hash is None:  # if hash creation failed then set hash to '?'
                hash_dict[file_path] = '?'
            # add file path and file hash to dictionary
            hashes[file_path] = calculated_hash
            print(f"'{file_path}' -> '{calculated_hash}'")
    
    return hash_dict

def check_data_integrity(directory_path: str, hashes: dict) -> dict:
    """Walk through a directory and subdirectories to check for data integrity, return a summary of the results."""
    print('\nChecking for Data Integrity...\n')

    number_new_files = 0
    number_deleted_files = 0
    number_bad_files = 0
    number_ok_files = 0
    number_unknown_files = 0

    files_checked = False
    for file_path in hashes:
        files_checked = True
        file_hash = hashes[file_path]
        calculated_hash = create_hash(file_path)

        if not os.path.exists(file_path):
            print(f"'{file_path}' -> '{file_hash}' : Deleted")
            number_deleted_files += 1
            continue
        
        if file_hash == '?':
            print(f"'{file_path}' : ?")
            number_unknown_files += 1
        elif file_hash == calculated_hash:
            print(f"'{file_path}' -> '{file_hash}' : Ok")
            number_ok_files += 1
        else:
            print(f"'{file_path}' -> '{file_hash}' != '{calculated_hash}' : Bad")
            number_bad_files += 1
    if not files_checked:
        print('No files checked')
    
    print('\nChecking for new files...\n')
    new_files = False
    for root, _, files in os.walk(directory_path):
        for file in files:
            file_path = os.path.join(root, file)
            calculated_hash = create_hash(file_path)

            if file_path not in hashes:
                new_files = True
                print(f"'{file_path}' -> '{calculated_hash}' : New File")
                number_new_files += 1
    if not new_files:
        print('No new files found')


    return {'number_new_files': number_new_files, 'number_deleted_files': number_deleted_files, 
            'number_bad_files': number_bad_files, 'number_ok_files': number_ok_files, 'number_unknown_files': number_unknown_files}



if __name__ == '__main__':
    app = QApplication([])

    print("""
        Options:
        1. Create Hash Dictionary
        2. Check Data Integrity
    """)
    option_selected = input('Enter option: ')

    if option_selected == '1':
        print('Select directory to start creating a hash dictionary')
        directory_path = ask_directory('Select a Start Directory')

        hash_dict = create_hash_dict(directory_path)

        print('Select a location to store the hash dictionary')
        save_path = ask_directory('Select a Save Directory')

        with open(os.path.join(save_path, 'hash_dict.json'), 'w') as file:
            json.dump(hash_dict, file, indent=4)

        print(f"DONE!\n{len(hash_dict['hashes'])} Files Hashed\nHash dictionary saved to '{save_path}'")
        print()
    elif option_selected == '2':
        print('Select Hash Dictionary')
        dict_path = ask_filelocation('Select Hash Dictionary', 'JSON (*.json)')

        with open(dict_path, 'r') as file:
            hash_dict = json.load(file)
            hashes = hash_dict['hashes']
            working_directory = hash_dict['attributes']['working_directory']

        attributes = hash_dict['attributes']
        data_summary = check_data_integrity(working_directory, hashes)

        summary_msg = f"Summary [{working_directory}]"
        print(f"""
        {summary_msg}
        {'-' * len(summary_msg)}
            {len(hashes)} Total Files Checked:

            New: {data_summary['number_new_files']:>5}
            Deleted: {data_summary['number_deleted_files']}
            Bad: {data_summary['number_bad_files']:>5}
            Ok: {data_summary['number_ok_files']:>6}
            Unknown: {data_summary['number_unknown_files']}
              """)
    else:
        print('Invalid option selected.')
        sys.exit()
