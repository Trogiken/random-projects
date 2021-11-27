import sys


def get_os(x):
    if sys.platform == "win32":
        path_form = "\\"
        system = "Windows"
    else:
        path_form = r"/"
        system = "Linux Based"

    if x == 1:
        return path_form
    elif x == 2:
        return system
    else:
        return None
