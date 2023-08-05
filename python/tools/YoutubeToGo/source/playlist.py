"""
This script reads playlist cvs files from takeout.google.com and 
inserts them into the new account
"""

import csv
import source.api as api
from tkinter import filedialog
from os import path
from misc import incomplete_function


@incomplete_function
def combine_playlists():
    """Asks for a file path and return list of dict's"""
    print("Select the playlist csv file(s)")
    file_path = filedialog.askopenfilename(multiple=True)

    # TODO Add support for multiple files, combine them into one list

    if not path.exists(file_path):
        print("File not found!")
        return False
    
    with open(file_path, newline='') as csvfile:
        try:
            reader = csv.DictReader(csvfile)
        except csv.Error:
            print("Error reading file!")
            return False

        if reader.fieldnames != ['Playlist Title', 'Video Ids']:
            print("Invalid file. Please make sure you selected the correct file.")
            return False
        
        try:
            reader.__next__()
        except StopIteration:
            print("File is empty!")
            return False

        return list(reader)


@incomplete_function
def playlist_prompt(playlist_data):
    """Prints the playlist names and asks for confirmation"""
    # TODO Verify proper format and len() functionality
    playlist_count = len(playlist_data)
    print() # newline
    for playlist in playlist_data:
        print(playlist["Playlist Title"])
    print(f"\nCreate {playlist_count} playlists?")

    while True:
        answer = input("Y/N: ").lower()
        if answer == "y":
            return True
        elif answer == "n":
            return False
        else:
            print("Invalid input. Try again.")


@incomplete_function
def create_playlists(playlist_data, credentials):
    """Creates playlists and adds videos to them, skipping duplicates"""
    pass