import os
import sys
import hashlib
import sqlite3
from typing import Tuple
from multiprocessing import Pool
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


def create_hash(file_path: str) -> Tuple[str, str]:
    """Create hash from file bytes using the chunk method, return hash as a string if found."""
    try:
        chunk_size = 4096
        file_size = os.path.getsize(file_path)

        if file_size > 1_000_000_000:  # If file size around 1 Gb or larger
            chunk_size = 8192

        hasher = hashlib.sha256()

        with open(file_path, 'rb') as file:
            while True:
                chunk = file.read(chunk_size)
                if not chunk:
                    break
                hasher.update(chunk)

        file_hash = hasher.hexdigest()
        return file_path, file_hash
    except BaseException as error:
        print(f"Failed to create hash! | {error}\nReplacing hash with '?'")
        return file_path, '?'


def create_hash_db(directory_path: str, data_save_path: str) -> int:
    if os.path.exists(data_save_path):
        print(f"\nHash database already exists at '{data_save_path}'\nDelete it? (y/n)\n")
        delete_database = input('Enter option: ')
        if delete_database.casefold() == 'y':
            os.remove(data_save_path)
        else:
            print('Canceled')
            sys.exit()

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
                        path TEXT
                    )''')
    # Insert working directory into the table
    cursor.execute('INSERT OR REPLACE INTO attributes (working_directory) VALUES (?)', (directory_path,))

    # Batch size for parameterized queries
    batch_size = 1000
    batch_data = []

    print('\nCreating Hashes...\n')

    with Pool() as pool:
        for root, _, files in os.walk(directory_path):
            file_paths = [os.path.join(root, file) for file in files]
            results = pool.map(create_hash, file_paths)
            batch_data.extend(results)

            if len(batch_data) >= batch_size:  # If batch size is reached, insert data into the database
                cursor.executemany('INSERT OR REPLACE INTO hashes (file_path, calculated_hash) VALUES (?, ?)',
                                   batch_data)
                batch_data = []
                print(f"Processed {len(results)} files")

        if batch_data:  # If there are any remaining files to be inserted
            cursor.executemany('INSERT OR REPLACE INTO hashes (file_path, calculated_hash) VALUES (?, ?)', batch_data)
            print(f"Processed {len(batch_data)} files")

    connection.commit()
    connection.close()

    connection = sqlite3.connect(data_save_path)
    cursor = connection.cursor()
    cursor.execute('SELECT COUNT(*) FROM hashes')
    num_files = cursor.fetchone()[0]
    connection.close()

    return num_files


def check_data_integrity_db(directory_path: str, data_save_path: str) -> dict:
    """Utilizing the hash database, check data integrity of files in a directory and subdirectories,
    and return a summary of the results."""
    connection = sqlite3.connect(data_save_path)
    cursor = connection.cursor()

    print('\nChecking for Data Integrity...\n')

    number_new_files = 0
    number_deleted_files = 0
    number_bad_files = 0
    number_ok_files = 0
    number_unknown_files = 0

    files_checked = set()
    for row in cursor.execute('SELECT file_path, calculated_hash FROM hashes'):
        files_checked.add(row[0])
        file_path = row[0]
        file_hash = row[1]

        if not os.path.exists(file_path):
            print(f"'{file_path}' -> '{file_hash}' : Deleted")
            number_deleted_files += 1
            continue

        calculated_hash = create_hash(file_path)

        if file_hash == '?':
            print(f"'{file_path}' : ?")
            number_unknown_files += 1
        elif file_hash == calculated_hash:
            print(f"'{file_path}' -> '{file_hash}' : Ok")
            number_ok_files += 1
        else:
            print(f"'{file_path}' -> '{file_hash}' != '{calculated_hash}' : Bad")
            number_bad_files += 1

    print('\nChecking for new files...\n')

    new_files = False
    for root, _, files in os.walk(directory_path):
        for file in files:
            file_path = os.path.join(root, file)
            if file_path not in files_checked:
                new_files = True
                calculated_hash = create_hash(file_path)
                print(f"'{file_path}' -> '{calculated_hash}' : New File")
                number_new_files += 1

    if not files_checked:
        print('No files checked')

    if not new_files:
        print('No new files found')

    connection.close()

    return {
        'number_new_files': number_new_files,
        'number_deleted_files': number_deleted_files,
        'number_bad_files': number_bad_files,
        'number_ok_files': number_ok_files,
        'number_unknown_files': number_unknown_files
    }


def compare_databases(db1_path: str, db2_path: str) -> dict:
    """Compare two hash databases and return a summary of the differences."""
    connection1 = sqlite3.connect(db1_path)
    cursor1 = connection1.cursor()

    connection2 = sqlite3.connect(db2_path)
    cursor2 = connection2.cursor()

    cursor1.execute('SELECT file_path, calculated_hash FROM hashes')
    db1_files = {row[0]: row[1] for row in cursor1.fetchall()}

    cursor2.execute('SELECT file_path, calculated_hash FROM hashes')
    db2_files = {row[0]: row[1] for row in cursor2.fetchall()}

    common_files = set(db1_files.keys()) & set(db2_files.keys())
    unique_files_db1 = set(db1_files.keys()) - set(db2_files.keys())
    unique_files_db2 = set(db2_files.keys()) - set(db1_files.keys())
    ok_files = []
    bad_files = []

    

    print(f"Common files in both databases ({db1_path} and {db2_path}):\n")

    for file_path in common_files:
        hash_db1 = db1_files[file_path]
        hash_db2 = db2_files[file_path]
        if hash_db1 == hash_db2:
            summary['ok_files'].append((file_path, hash_db1))
            print(f"'{file_path}' -> Hash: '{hash_db1}'")
        else:
            summary['bad_files'].append((file_path, hash_db1, hash_db2))
            print(f"'{file_path}' -> Hash in {db1_path}: '{hash_db1}', Hash in {db2_path}: '{hash_db2}'")

    print('\nUnique files in the first database:\n')

    for file_path in unique_files_db1:
        hash_db1 = db1_files[file_path]
        print(f"'{file_path}' -> Hash: '{hash_db1}'")
        summary['unique_files_db1'].append((file_path, hash_db1))

    print('\nUnique files in the second database:\n')

    for file_path in unique_files_db2:
        hash_db2 = db2_files[file_path]
        print(f"'{file_path}' -> Hash: '{hash_db2}'")
        summary['unique_files_db2'].append((file_path, hash_db2))

    connection1.close()
    connection2.close()

    summary = {
        'number_common_files': len(common_files),
        'number_unique_files_db1': len(unique_files_db1),
        'number_unique_files_db2': len(unique_files_db2),
        'number_ok_files': len(ok_files),
        'number_bad_files': len(bad_files),
        'common_files': [],
        'unique_files_db1': [],
        'unique_files_db2': [],
        'ok_files': [],
        'bad_files': []
    }

    return summary


if __name__ == '__main__':
    app = QApplication([])

    print("""
        Options:
        1. Create Hash Database
        2. Check Data Integrity
        3. Compare Databases
    """)

    main_option_selected = input('Enter option: ')

    if main_option_selected == '1':
        print('Select directory to start creating a hash database')
        directory_path = ask_directory('Select a Start Directory')
        print(f'Selected hash directory: {directory_path}')

        print('Select a location to store the hash database')
        data_save_path = ask_directory('Select a Save Directory')
        print(f'Selected save directory: {data_save_path}')

        data_save_path = os.path.join(data_save_path, 'hash_data.sqlite3')
        number_files = create_hash_db(directory_path, data_save_path)

        print(f"DONE!\n{number_files} Files Hashed\nHash database saved to '{data_save_path}'")
    elif main_option_selected == '2':
        print('Select Hash Database')

        data_save_path = ask_filelocation('Select Hash Database', 'SQLite3 (*.sqlite3)')
        print(f'Selected hash database: {data_save_path}')

        # get extension
        _, extension = os.path.splitext(data_save_path)

        if extension == '.sqlite3':
            connection = sqlite3.connect(data_save_path)
            cursor = connection.cursor()
            cursor.execute('SELECT calculated_hash FROM hashes')
            hashes = cursor.fetchall()
            cursor.execute('SELECT working_directory FROM attributes')
            working_directory = cursor.fetchone()[0]
            connection.close()

            data_summary = check_data_integrity_db(working_directory, data_save_path)
        else:
            print('Invalid File Detected')
            sys.exit()

        summary_msg = f"Summary [{working_directory}]"
        print(f"""
        {summary_msg}
        {'-' * len(summary_msg)}
            {len(hashes)} Total Files Checked:

            New: {data_summary['number_new_files']:>5}
            Deleted: {data_summary['number_deleted_files']:>5}
            Bad: {data_summary['number_bad_files']:>5}
            OK: {data_summary['number_ok_files']:>5}
            Unknown: {data_summary['number_unknown_files']:>5}
        """)
    elif main_option_selected == '3':
        print('Select first Hash Database')

        db1_path = ask_filelocation('Select First Hash Database', 'SQLite3 (*.sqlite3)')
        print(f'Selected first hash database: {db1_path}')

        print('Select second Hash Database')

        db2_path = ask_filelocation('Select Second Hash Database', 'SQLite3 (*.sqlite3)')
        print(f'Selected second hash database: {db2_path}')

        summary = compare_databases(db1_path, db2_path)

        summary_msg = f"Summary [{db1_path} and {db2_path}]"
        print(f"""
        {summary_msg}
        {'-' * len(summary_msg)}
            Totals:
            Common Files: {summary['number_common_files']:>5}
            Unique Files in {db1_path}: {summary['number_unique_files_db1']:>5}
            Unique Files in {db2_path}: {summary['number_unique_files_db2']:>5}
            Ok Files in Common: {summary['number_ok_files']:>5}
            Bad Files in Common: {summary['number_bad_files']:>5}

            Files:
            Unique Files in {db1_path}: {summary['unique_files_db1'][0]}
            Unique Files in {db2_path}: {summary['unique_files_db2'][0]}
            # Ok Files in Common: {summary['ok_files']}
            Bad Files in Common: {summary['bad_files']}
        """)
    else:
        print('Invalid Option Selected')
