import sys


def get_os(opt):
    if sys.platform == "win32":
        path_form = "\\"
        system = "Windows"
        clear_form = "cls"
    else:
        path_form = "/"
        system = "Linux Based"
        clear_form = "clear"

    if opt == 1:
        return path_form
    elif opt == 2:
        return system
    elif opt == 3:
        return clear_form
    else:
        return None
