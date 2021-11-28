import sys

# Python 3.8+ Version Check
major = sys.version_info.major
minor = sys.version_info.minor
micro = sys.version_info.micro
current = f"{major}.{minor}.{micro}"
if major >= 3 and minor >= 8:
    print("Pass")
    pass
else:
    print(f"[Incorrect Python Version]\n"
          f"Requires: Python 3.8+ (Current - {current})")


def get_os(opt):
    """Gather OS dependant information"""
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
