import source as src
import pathlib
import traceback
import sys
import os
import tkinter
import tkinter.filedialog
from time import sleep

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
    mods_path = os.path.join(
        os.getenv("USERPROFILE"),
        "curseforge",
        "minecraft",
        "Instances",
        "Serverstienpack",
        "mods"
    )

    if not is_valid_mod_path(mods_path):
        mods_path = ""

    return mods_path


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

    window_width = 400
    window_height = 150
    root.geometry(f"{window_width}x{window_height}")
    root.resizable(True, True)

    # Title label
    title = tkinter.Label(root, text=PROGRAM_NAME, font=("Arial", 16))
    title.pack(pady=5)

    # Mods path label
    mods_path = get_mods_path()
    padding = 20
    mods_path_label = tkinter.Label(root, text=mods_path, font=("Arial", 12), wraplength=window_width - padding, justify="left")
    mods_path_label.pack(pady=5)
    if not mods_path:
        print("Mods folder not found, open it manually\nSee modpack-installation channel for info")
        mods_path_label.config(text="Unkown Mods Path")
        mods_path = get_path_tk()
        if mods_path:
            mods_path_label.config(text=mods_path)
            print(f"Updated mods path to {mods_path}")
        else:
            print("No valid mods path provided. Exiting...")
            sleep(3)
            return

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

    version_label = tkinter.Label(root, text=f"v{VERSION}", font=("Arial", 10))
    version_label.pack(side="bottom", anchor="se")

    # run the mainloop
    root.mainloop()


if __name__ == '__main__':
    main()
