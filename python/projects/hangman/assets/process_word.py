import os
import random
from .os_prop import *


def fetch_words():
    """Read all words in words.txt and return in list format"""
    cwd = os.getcwd()
    words = []
    with open(cwd + f"{get_os(1)}words", 'r') as f:
        raw_words = f.read().splitlines()
        for item in raw_words:
            if item:
                for char in item:
                    if char.isalpha():
                        continue
                    else:
                        input(f"Letters Only! - [{item}]\nPress Enter to Exit")
                        exit()
                words.append(item)
        if words:
            return words
        else:
            print("Words list Empty!")
            input("Press Enter to Exit"); exit()


def random_word():
    """Return random word from fetch_words()"""
    all_words = fetch_words()
    list_length = len(all_words)
    index = random.randint(0, list_length - 1)
    word = all_words[index]

    return word
