"""Create hash for each file in a directory and subdirectories to check for data integrity."""

# import modules
import os
import sys
import hashlib
import json
import logging
from tkinter import filedialog

logging.basicConfig(level=logging.WARNING, format='%(asctime)s - %(levelname)s - %(message)s')


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
    hash_dict = {}
    for root, _, files in os.walk(directory_path):
        for file in files:
            file_path = os.path.join(root, file)
            file_hash = create_hash(file_path)
            if file_hash is None:
                hash_dict[file_path] = '?'
            # add file path and file hash to dictionary
            hash_dict[file_path] = file_hash
            print(f'{file_path} -> {file_hash}')
    return hash_dict

if __name__ == '__main__':
    print("""
        Options:
        1. Create hash dictionary
        2. Check data integrity
    """)
    option_selected = input('Enter option: ')
    if option_selected == '1':
        directory_path = filedialog.askdirectory(title='Select directory to start creating a hash dictionary')
        hash_dict = create_hash_dict(directory_path)
        with open(os.path.join(os.path.dirname(os.path.abspath(__file__)), 'hash_dict.json'), 'w') as file:
            json.dump(hash_dict, file, indent=4)
    elif option_selected == '2':
        pass
    else:
        print('Invalid option selected.')
        sys.exit()


# define function to create hash for each file in a directory and subdirectories.
# print and save the hash for each file in a directory and subdirectories in a dictionary.
# example of the creation print statements: file_name -> hash
# example of the check print statements: hash -> file_name : Bad (Hash doesn't match current) or Ok (Hash matches current) or ? (Missing data/file/hash)


# create two options for the user to choose from to either check the data integrity of a directory or to create the dictionary of hashes.
# use tkinter to ask for the directory path.