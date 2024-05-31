import source as src
import pathlib
import traceback
import sys
import os
import tkinter
import tkinter.filedialog
from time import sleep

# TODO: Make the program pull from different paths for different files (mods, resources, textures)
# TODO: Then have custom file path checks on each of them

PROGRAM_NAME = "Hominum Modpack Updater"
VERSION = "1.2"
PATH_URL = r"https://raw.githubusercontent.com/Eclik1/Hominum-Updates/main/path.txt"
GITHUB_CONTENTS_BASE = r"https://api.github.com/repos/Eclik1/Hominum-Updates/contents"

# create the application path depending on if the script is an executable or not
if getattr(sys, 'frozen', False):
    APPLICATION_PATH = pathlib.Path(sys.executable).parent
else:
    APPLICATION_PATH = pathlib.Path(__file__).parent


class CustomTk(tkinter.Tk):
    def report_callback_exception(self, exc, val, tb):
        error_file = APPLICATION_PATH / "error.txt"
        with open(error_file, "w") as f:
            f.write("".join(traceback.format_exception(exc, val, tb)))
        print("Error occurred, check error.txt for more information")
        print("For help send this file to Creme Fraiche on discord")

    def destroy(self):
        self.quit()
        self.update()
        super().destroy()


def get_path() -> str:
    """Returns a relative path from the PATH_URL"""
    resp = src.get_request(PATH_URL)
    path = resp.text.split("\n")[0].strip()
    return path


def get_urls() -> list:
    """Returns a list of file download urls"""
    rel_path = get_path()
    
    urls = []
    url = f"{GITHUB_CONTENTS_BASE}/{rel_path}"
    resp = src.get_request(url)
    for file in resp.json():
        urls.append(file["download_url"])

    return urls


def is_valid_mod_path(path: str) -> bool:
    """Returns True if the entered path exists and all files in the directory are jars."""
    if not os.path.exists(path):
        return False

    if all(file.endswith('.jar') for file in os.listdir(path)):
        return True
    else:
        return False


def get_mods_path() -> str:
    """Returns the path to the mods folder"""
    user_profile = os.getenv("USERPROFILE")
    base_path = os.path.join(user_profile, "curseforge", "minecraft", "Instances")
    server_pack_names = [
        "Serverstienpack",
        "Serverstienpack1",
        "Serverstienpack1.1",
        "Serverstienpack1.1(fixed)",
        "Serverstienpack-1.1",
        "Serverstienpack-1.1(fixed)",
        "serverstienpack",
        "serverstienpack1",
        "serverstienpack1.1",
        "serverstienpack1.1(fixed)",
        "serverstienpack-1.1",
        "serverstienpack-1.1(fixed)",
    ]

    paths_to_try = [os.path.join(base_path, pack_name, "mods") for pack_name in server_pack_names]

    for mods_path in paths_to_try:
        if is_valid_mod_path(mods_path):
            return mods_path

    return ""


def get_path_tk() -> str:
    """Return path using tk file dialog"""
    while True:
        root = tkinter.Tk()
        root.withdraw()
        path = tkinter.filedialog.askdirectory(title="Select the mods folder")
        if not path:
            print("Operation cancelled.")
            return ""
        if is_valid_mod_path(path):
            return path
        else:
            print("Invalid mod path, please select again.")


def main():
    """GUI part of the program"""
    root = CustomTk()
    root.title(PROGRAM_NAME)

    WINDOW_WIDTH = 400
    WINDOW_HEIGHT = 150
    root.geometry(f"{WINDOW_WIDTH}x{WINDOW_HEIGHT}")
    root.resizable(False, False)

    # Title label
    title = tkinter.Label(root, text=PROGRAM_NAME, font=("Arial", 16))
    title.pack(pady=5)
    ########################

    # Mods path label
    mods_path = get_mods_path()
    PADDING = 20 # padding for the label
    MAX_LEN = 100 # max length of the path to display
    mods_path_label = tkinter.Label(root, font=("Arial", 12), wraplength=WINDOW_WIDTH - PADDING, justify="left")
    mods_path_label.pack(pady=5)
    if not mods_path:
        print("Mods folder not found, open it manually\nSee modpack-installation channel for info")
        mods_path_label.config(text="Unkown Mods Path")
        mods_path = get_path_tk()
        if mods_path:
            print(f"Updated mods path to {mods_path}")
        else:
            print("No valid mods path provided. Exiting...")
            sleep(3)
            return
    mods_path_text = mods_path
    if len(mods_path_text) > MAX_LEN:
        mods_path_text = mods_path_text[:MAX_LEN] + "..."
    mods_path_label.config(text=mods_path_text)
    ########################

    # create update button
    button = tkinter.Button(
        root,
        text="Update Modpack",
        font=("Arial", 12),
        height=1,
        width=15,
        command=lambda: src.download_files(get_urls(), mods_path)
    )
    button.pack(pady=1)
    ########################

    # create version label
    version_label = tkinter.Label(root, text=f"v{VERSION}", font=("Arial", 10))
    version_label.pack(side="bottom", anchor="se")
    ########################

    # run the mainloop
    root.mainloop()


if __name__ == '__main__':
    main()
