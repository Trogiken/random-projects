"""
This script reads the "subscriptions.csv" created by takeout.google.com and
inserts the subscriptions into the new account.
"""

import csv
import source.api as api
from tkinter import filedialog
from os import path


def get_file_data():
    """Asks for a file path and return list of dict's"""
    print("Select the 'subscriptions.csv' file from takeout.google.com")
    file_path = filedialog.askopenfilename()

    if not path.exists(file_path):
        print("File not found!")
        return False
    
    with open(file_path, newline='') as csvfile:
        try:
            reader = csv.DictReader(csvfile)
        except csv.Error:
            print("Error reading file!")
            return False

        if reader.fieldnames != ['Channel Id', 'Channel Url', 'Channel Title']:
            print("Invalid file. Please make sure you selected the correct file.")
            return False
        
        try:
            reader.__next__()
        except StopIteration:
            print("File is empty!")
            return False

        return list(reader)


def subscribe_prompt(channel_data):
    """Prints the channel names and asks for confirmation"""
    channel_count = len(channel_data)
    print() # newline
    for channel in channel_data:
        print(channel["Channel Title"])
    print(f"\nSubscribe to {channel_count} channels?")

    while True:
        answer = input("Y/N: ").lower()
        if answer == "y":
            return True
        elif answer == "n":
            return False
        else:
            print("Invalid input. Try again.")


def subscribe_to_channels(channel_data, credentials):
    """Subscribes to all the channels in the list"""
    for channel in channel_data:
        request_body = {
            "snippet": {
                "resourceId": {
                    "kind": "youtube#channel",
                    "channelId": channel["Channel Id"]
                }
            }
        }
        response = api.post_request("https://www.googleapis.com/youtube/v3/subscriptions?part=snippet", request_body, credentials.token)
        if not response: # skip to next channel if error
            continue

        if response.ok:
            print(f"\nSubscribed to {channel['Channel Title']} successfully\n")
        else:
            print(f"\nError subscribing to {channel['Channel Title']}:\n{response.json()['error']['errors']}")
