import logging
import sys
import os

logging.basicConfig(filename='log.log', level=logging.INFO,
                    format='%(levelname)s:%(module)s:%(message)s')


if sys.platform == "win32":
    path_form = "\\"
    system = "Windows"
else:
    path_form = "/"
    system = "Linux Based"

raw_cwd = os.getcwd()
cwd = raw_cwd.replace("/", path_form)

# TODO FIX THIS
termcolor = cwd + "/assets/packages/termcolor"
sys.path.insert(0, termcolor)
