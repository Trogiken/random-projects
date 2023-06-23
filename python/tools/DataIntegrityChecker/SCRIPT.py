"""Create hash for each file in a directory and subdirectories to check for data integrity."""

# import modules
import os
import sys
import hashlib
import json
import logging
from PyQt6.QtWidgets import QApplication, QFileDialog


logging.basicConfig(level=logging.WARNING, format='%(asctime)s - %(levelname)s - %(message)s')


def ask_filelocation(title, name_filter):
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

def ask_directory(title):
    """Ask for a directory path."""
    directory_dialog = QFileDialog()
    directory_dialog.setWindowTitle(title)
    directory_dialog.setFileMode(QFileDialog.FileMode.Directory)

    if directory_dialog.exec():
        return directory_dialog.selectedFiles()[0]
    else:
        print('Canceled')
        sys.exit()


def create_hash(file_path):
    """Create hash from file bytes."""
    try:
        with open(file_path, 'rb') as file:
            file_read = file.read()
            file_hash = hashlib.sha256(file_read).hexdigest()
            return file_hash
    except BaseException as error:
        logging.error(f"Failed to hash '{file_path}' | {error}")
        return None

def create_hash_dict(directory_path):
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

    # TODO No files to hash message
    
    return hash_dict

def check_data_integrity(directory_path, hashes):
    """Walk through a directory and subdirectories to check for data integrity."""
    print('\nChecking for Data Integrity...\n')

    for file_path in hashes:
        file_hash = hashes[file_path]
        calculated_hash = create_hash(file_path)

        if not os.path.exists(file_path):
            print(f"'{file_path}' -> '{file_hash}' : Deleted")
            continue
        
        if file_hash == '?':
            print(f"'{file_path}' : ?")
        elif file_hash == calculated_hash:
            print(f"'{file_path}' -> '{file_hash}' : Ok")
        else:
            print(f"'{file_path}' -> '{file_hash}' != '{calculated_hash}' : Bad")
    
    print('\nChecking for new files...\n')
    new_files = False
    for root, _, files in os.walk(directory_path):
        for file in files:
            file_path = os.path.join(root, file)
            calculated_hash = create_hash(file_path)

            if file_path not in hashes:
                new_files = True
                print(f"'{file_path}' -> '{calculated_hash}' : New File")
    if not new_files:
        print('Now new files found')

    return False # TODO Use boolean to return if data is corrupted or not



if __name__ == '__main__':
    app = QApplication([])

    print("""
        Options:
        1. Create hash dictionary
        2. Check data integrity
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

        print(f"DONE!\nHash dictionary saved to '{save_path}'")
    elif option_selected == '2':
        print('Select hash dictionary')
        dict_path = ask_filelocation('Select a Hash Dictionary', 'JSON (*.json)')

        with open(dict_path, 'r') as file:
            hash_dict = json.load(file)
        attributes = hash_dict['attributes']
        check_data_integrity(attributes.get('working_directory'), hash_dict['hashes'])

        # TODO use boolean from function to determine if data is corrupted or not
    else:
        print('Invalid option selected.')
        sys.exit()
