"""
This script reads the "subscriptions.csv" created by takeout.google.com to
resubscribe to all the channels using oAuth2 credentials.

---------------------------------------------------------------

Prerequisites:
1. Create a Project and Enable the YouTube Data API:
    * Go to the https://console.developers.google.com.
    * Create a new project or select an existing one.
    * Select Enable APIs and services and search for "YouTube Data API"
    * Enable it for your project.

2. Obtain API Credentials:
    * Click on "Credentials" in the left-hand menu.
    * Click on the "Create Credentials" button and select "OAuth client ID."
    * Select External and click on the "Create" button.
    * Fill out the form with information (can be anything)
    * Save and Continue
    * Enable all scopes related to the YouTube Data API
    * Finish the setup
    * Publish the app
    * Go back to the Credentials page and create a new OAuth client ID as a Desktop app.
    * Download the JSON file.
"""

import google_auth_oauthlib.flow
import requests
import csv
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


def get_credentials():
    """Performs OAuth2 authorization and returns credentials"""
    print("Select the 'client_secrets.json' file")
    file_path = filedialog.askopenfilename()

    if not path.exists(file_path):
        print("File not found!")
        return False

    try:
        flow = google_auth_oauthlib.flow.InstalledAppFlow.from_client_secrets_file(
            client_secrets_file=file_path,
            scopes=["https://www.googleapis.com/auth/youtube.force-ssl"]
        )
        credentials = flow.run_local_server(port=8080)
        return credentials
    except BaseException as err:
        print(f"\nError getting credentials:\n{err}")
        return False


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


def subscribe_request(request_body, access_token):
    """Sends a POST request to the YouTube Data API"""
    headers = {
        "Authorization": f"Bearer {access_token}",
        "Accept": "application/json",
        "Content-Type": "application/json"
    }
    try:
        response = requests.post(
            "https://www.googleapis.com/youtube/v3/subscriptions?part=snippet",
            json=request_body,
            headers=headers
        )
        return response
    except BaseException as err:
        print(f"\nError sending request:\n{err}")
        return False


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
        response = subscribe_request(request_body, credentials.token)
        if not response: # skip to next channel if error
            continue

        if response.ok:
            print(f"\nSubscribed to {channel['Channel Title']} successfully\n")
        else:
            print(f"\nError subscribing to {channel['Channel Title']}:\n{response.json()['error']['errors']}")
