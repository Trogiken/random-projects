"""
REQUIREMENTS
Store a modifiable list of words to be used
Windows and Linux terminal compatibility
Save Scores and Display before each game

RULES
* A number of times a user can get the incorrect letter and display tries left
* Display correct and incorrect letters separately
"""

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
