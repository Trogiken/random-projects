import sys
import os

if sys.platform == "win32":
    path_form = "\\"
else:
    path_form = "/"
raw_cwd = os.getcwd()
cwd = raw_cwd.replace("/", path_form)
termcolor = cwd + "/assets/packages/termcolor"
sys.path.insert(0, termcolor)

from termcolor import colored, cprint

text = colored('Hello, World!', 'red', attrs=['reverse', 'blink'])
print(text)
cprint('Hello, World!', 'green', 'on_red')


def print_red_on_cyan(x):
    cprint(x, 'red', 'on_cyan')


print_red_on_cyan('Hello, World!')
print_red_on_cyan('Hello, Universe!')

for i in range(10):
    cprint(i, 'magenta', end=' ')

cprint("Attention!", 'red', attrs=['bold'])
