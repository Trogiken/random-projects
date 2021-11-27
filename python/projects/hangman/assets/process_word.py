from os import getcwd
from .os_prop import get_os


def fetch_words():
    cwd = getcwd()
    # Gather words
    with open(cwd + f"{get_os(1)}words", 'r') as f:
        words = f.read().splitlines()

    return words
