import sys
import os

if sys.platform == "win32":
    path_form = "\\"
else:
    path_form = "/"
raw_cwd = os.getcwd()
cwd = raw_cwd.replace("/", path_form)
assets_dir = cwd + "/assets"
sys.path.insert(0, assets_dir)

try:
    import terminal_ui
except ImportError as IE:
    print(f"Module Load Error: {IE}")


def main():
    pass


if __name__ == '__main__':
    main()
