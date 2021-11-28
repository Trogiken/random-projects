from os import getcwd
from random import randint
from .os_info import *
from .internal import *


def fetch_words():
    """Read all words in words.txt and return in list format"""
    cwd = getcwd()
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
            input("Words list Empty!\nPress Enter to Exit")
            exit()


def get_word():
    """Generates a random non-repeating word"""
    #  TODO Efficiency Problem: Loops through until it gets a new word
    while True:
        all_words = fetch_words()
        list_length = len(all_words)
        index = randint(0, list_length - 1)
        word = all_words[index]
        if word not in Game.used_words:
            Game.used_words.append(word)
            break
        elif int(len(Game.used_words)) == len(fetch_words()):
            Game.used_words.clear()
            # All words used. Reset used_words
            continue
        else:
            continue

    return word


if __name__ == '__main__':
    exit()
