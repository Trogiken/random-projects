import logging

logging.basicConfig(filename='log.log', level=logging.INFO,
                    format='%(levelname)s:%(module)s:%(message)s')

try:
    from .sub_pkgs import colored, cprint
except ImportError as IE:
    logging.critical(f'Import Failure: {IE}')
    exit()


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
