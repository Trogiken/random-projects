"""Create hash for each file in a directory and subdirectories to check for data integrity."""

import os
import sys
import hashlib
import json
import shelve
import sqlite3
from PyQt6.QtWidgets import QApplication, QFileDialog


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
    """Create hash from file bytes using the chunk method, return hash as a string if found."""
    try:
        chunk_size = 4096  # TODO Adjust the chunk size as per requirements (1 Gb in size use 8096)
        hasher = hashlib.sha256()
        
        with open(file_path, 'rb') as file:
            while True:
                chunk = file.read(chunk_size)
                if not chunk:
                    break
                hasher.update(chunk)
        
        file_hash = hasher.hexdigest()
        return file_hash
    except BaseException as error:
        print(f"Failed to create hash! | {error}\nReplacing hash with '?'")
        return '?'

def create_hash_dict_memory(directory_path: str) -> dict:
    """Utilizing the disk, walk through a directory and subdirectories to create a dictionary of hashes for each file, return dictionary."""
    hash_dict = {'attributes': {'working_directory': directory_path},
                 'hashes': {}}  # create dictionary with working directory as attribute

    print('\nCreating Hash Dictionary...\n')
    hashes = hash_dict['hashes']
    for root, _, files in os.walk(directory_path):
        for file in files:
            file_path = os.path.join(root, file)
            calculated_hash = create_hash(file_path)
            # add file path and file hash to dictionary
            hashes[file_path] = calculated_hash
            print(f"'{file_path}' -> '{calculated_hash}'")
    
    return hash_dict

def check_data_integrity_memory(directory_path: str, hashes: dict) -> dict:
    """Utilizing Memory, Walk through a directory and subdirectories to check for data integrity, return a summary of the results."""
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

# TODO now that hash function is fixed with chunks this may be able to be used
# def create_hash_dict_disk(directory_path: str, dict_save_path: str) -> int:
#     """Utilizing the disk, walk through a directory and subdirectories to create a dictionary of hashes for each file, return number of files."""
#     with shelve.open(dict_save_path) as shelf:
#         shelf['attributes'] = {'working_directory': directory_path, 'function': 'disk'}
#         shelf['hashes'] = {}
#         for root, _, files in os.walk(directory_path):
#             for file in files:
#                 file_path = os.path.join(root, file)
#                 calculated_hash = create_hash(file_path)
#                 # add file path and file hash to dictionary
#                 shelf['hashes'][file_path] = calculated_hash
#                 print(f"'{file_path}' -> '{calculated_hash}'")
    
#     return len(shelf['hashes'])
def create_hash_dict_disk(directory_path: str, data_save_path: str) -> int:
    connection = sqlite3.connect(data_save_path)
    cursor = connection.cursor()
    
    # Create table for hashes
    cursor.execute('''CREATE TABLE IF NOT EXISTS hashes (
                        file_path TEXT PRIMARY KEY,
                        calculated_hash TEXT
                    )''')
    # create attribute table
    cursor.execute('''CREATE TABLE IF NOT EXISTS attributes (
                        working_directory TEXT PRIMARY KEY,
                        function TEXT
                    )''')
    # Insert working directory and function into the table
    cursor.execute('INSERT OR REPLACE INTO attributes (working_directory, function) VALUES (?, ?)', (directory_path, 'disk'))

    for root, _, files in os.walk(directory_path):
        for file in files:
            file_path = os.path.join(root, file)
            calculated_hash = create_hash(file_path)
            # Insert file path and hash into the table
            cursor.execute('INSERT OR REPLACE INTO hashes (file_path, calculated_hash) VALUES (?, ?)', (file_path, calculated_hash))
            print(f"'{file_path}' -> '{calculated_hash}'")
    connection.commit()
    connection.close()

    connection = sqlite3.connect(data_save_path)
    cursor = connection.cursor()
    cursor.execute('SELECT COUNT(*) FROM hashes')
    num_files = cursor.fetchone()[0]
    connection.close()

    return num_files

def check_data_integrity_disk(directory_path: str, data_save_path: str) -> dict:
    """Utilizing the disk, walk through a directory and subdirectories to check for data integrity, return a summary of the results."""
    connection = sqlite3.connect(data_save_path)
    cursor = connection.cursor()

    print('\nChecking for Data Integrity...\n')

    number_new_files = 0
    number_deleted_files = 0
    number_bad_files = 0
    number_ok_files = 0
    number_unknown_files = 0

    files_checked = False
    for row in cursor.execute('SELECT file_path, calculated_hash FROM hashes'):
        files_checked = True
        file_path = row[0]
        file_hash = row[1]
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

            cursor.execute('SELECT COUNT(*) FROM hashes WHERE file_path=?', (file_path,))
            if cursor.fetchone()[0] == 0:
                new_files = True
                print(f"'{file_path}' -> '{calculated_hash}' : New File")
                number_new_files += 1
    if not new_files:
        print('No new files found')

    connection.close()

    return {'number_new_files': number_new_files, 'number_deleted_files': number_deleted_files, 
            'number_bad_files': number_bad_files, 'number_ok_files': number_ok_files, 'number_unknown_files': number_unknown_files}
        


if __name__ == '__main__':
    app = QApplication([])

    print("""
        Options:
        1. Create Hash Dictionary
        2. Check Data Integrity
    """)

    main_option_selected = input('Enter option: ')

    if main_option_selected == '1':
        print("""
            Mode:
            1. RAM - Faster, needs a lot of RAM (Recommended for small - medium amount of files)
            2. Disk - Slower, uses disk read/write (Recommended for large amount of files)
        """)
        mode = input('Mode: ')

        print('Select directory to start creating a hash dictionary')
        directory_path = ask_directory('Select a Start Directory')
        print(f'Selecting directory: {directory_path}')

        print('Select a location to store the hash dictionary')
        data_save_path = ask_directory('Select a Save Directory')
        

        if mode == '1':
            data_save_path = os.path.join(data_save_path, 'hash_data.json')
            hash_dict = create_hash_dict_memory(directory_path)
            with open(data_save_path, 'w') as file:
                json.dump(hash_dict, file, indent=4)
                number_files = len(hash_dict['hashes'])
        elif mode == '2':
            data_save_path = os.path.join(data_save_path, 'hash_data.sqlite3')
            number_files = create_hash_dict_disk(directory_path, data_save_path)
        else:
            print('Invalid mode selected')
            sys.exit()

        print(f"DONE!\n{number_files} Files Hashed\nHash dictionary saved to '{data_save_path}'")
    elif main_option_selected == '2':
        print('Select Hash Dictionary')

        data_save_path = ask_filelocation('Select Hash Dictionary', 'JSON (*.json);;SQLite3 (*.sqlite3)')

        # get extension
        _, extension = os.path.splitext(data_save_path)

        if extension == '.json':
            with open(data_save_path, 'r') as file:
                hash_dict = json.load(file)
                hashes = hash_dict['hashes']
                working_directory = hash_dict['attributes']['working_directory']
                function = hash_dict['attributes']['function']
            
            data_summary = check_data_integrity_memory(working_directory, hashes)
        elif extension == '.sqlite3':
            connection = sqlite3.connect(data_save_path)
            cursor = connection.cursor()
            cursor.execute('SELECT file_path, calculated_hash FROM hashes')
            hashes = cursor.fetchall()
            cursor.execute('SELECT working_directory, function FROM attributes')
            working_directory, function = cursor.fetchone()
            connection.close()

            data_summary = check_data_integrity_disk(working_directory, data_save_path)
        else:
            print('Invalid function detected.')
            sys.exit()
        

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
