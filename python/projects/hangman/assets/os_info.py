import sys


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


if __name__ == '__main__':
    exit()
else:
    # Python 3.8+ Version Check
    major = sys.version_info.major
    minor = sys.version_info.minor
    micro = sys.version_info.micro
    current = f"{major}.{minor}.{micro}"
    if not major >= 3 and minor >= 8:
        print(f"[Incorrect Python Version]\n"
              f"Requires: Python 3.8+ (Current - {current})")
