from random import randint
from .internal import *


def fetch_words():
    """Read all words in words.txt and return in list format"""
    words = []
    try:
        with open("words.txt", 'r') as f:
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
    except FileNotFoundError:
        input("Words File Not Found\nPress Enter to Exit")
        exit()


def get_word():
    """Generates a random non-repeating words.txt"""
    while True:
        all_words = fetch_words()
        list_length = len(all_words)
        index = randint(0, list_length - 1)
        word = all_words[index]
        #  TODO Efficiency Problem: Loops through until it gets a new words.txt
        if word not in Game.looped_words:
            Game.looped_words.append(word)
            break
        elif int(len(Game.looped_words)) == len(fetch_words()):
            Game.looped_words.clear()
            continue
        else:
            continue

    return word


if __name__ == '__main__':
    exit()
