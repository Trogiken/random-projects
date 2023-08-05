import subscribe as subs


def paused_exit(code=0):
    """Exits the program after user input"""
    input("\nPress Enter to exit")
    exit(code)


if __name__ == "__main__":
    channel_data = subs.get_file_data()
    if not channel_data:
        paused_exit(1)
    credentials = subs.get_credentials()
    if not credentials:
        paused_exit(1)
    
    if subs.subscribe_prompt(channel_data):
        subs.subscribe_to_channels(channel_data, credentials)

    paused_exit()
