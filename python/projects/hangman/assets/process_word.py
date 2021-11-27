import os
import random
from .os_prop import *


def fetch_words():
    """Read all words in words.txt and return in list format"""
    cwd = os.getcwd()
    numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 0]
    words = []
    with open(cwd + f"{get_os(1)}words", 'r') as f:
        raw_words = f.read().splitlines()
        for item in raw_words:
            if item:  # If not empty
                for char in item:
                    if char.isalpha():
                        continue
                    else:
                        input(f"Letters Only! - [{item}]\nPress Enter to Exit")
                        exit()
                words.append(item)
        if words:  # If not empty
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
