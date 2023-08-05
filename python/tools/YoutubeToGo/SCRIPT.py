"""
This script reads the csv file created by takeout.google.com to
resubscribe to all the channels.

The csv file selected should be the "subscriptions.csv" file.
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
    * You'll be shown your client ID and client secret. Keep these safe.
"""

from tkinter import filedialog
import requests
import csv


def get_file_data():
    """Asks for a file path and return list of dict's"""
    file_path = filedialog.askopenfilename()
    with open(file_path, newline='') as csvfile:
        return list(csv.DictReader(csvfile))


def get_api_key():
    """Asks for a API key and returns it"""
    return input("Enter API key: ")


def subscribe_prompt(channel_data):
    """Prints the channel names and asks for confirmation"""
    channel_count = len(channel_data)
    for channel in channel_data:
        print(channel["Channel Title"])
    print(f"\nSubscribe to {channel_count} channels?\n")

    while True:
        answer = input("Y/N: ").lower()
        if answer == "y":
            return True
        elif answer == "n":
            return False
        else:
            print("Invalid input. Try again.")


def subscribe_request(request_body, params):
    """Sends a POST request to the YouTube Data API"""
    try:
        response = requests.post(
            "https://www.googleapis.com/youtube/v3/subscriptions",
            json=request_body,
            params=params
        )
        response.raise_for_status()
        return response
    except requests.exceptions.HTTPError as err:
        print(err)
        print(response.json())
        return response


def subscribe_to_channels(channel_data, api_key):
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
        params = {
            "part": "snippet",
            "key": api_key
        }
        response = subscribe_request(request_body, params)

        if response.status_code == 204:
            print(f"\nSubscribed to {channel['Channel Title']}\n")
        else:
            print(f"Error subscribing to {channel['Channel Title']}\nResponse: {response.json()}\n")


if __name__ == '__main__':
    channel_data = get_file_data()
    api_key = get_api_key()

    if subscribe_prompt(channel_data):
        subscribe_to_channels(channel_data, api_key)
