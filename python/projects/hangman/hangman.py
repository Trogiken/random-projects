from assets import *
import os

used_words = []


def get_word():
    """Generates a random non-repeating word"""
    #  TODO Efficiency Problem: Loops through until it gets a new word
    while True:
        word = random_word()
        if word not in used_words:
            used_words.append(word)
            break
        elif int(len(used_words)) == len(fetch_words()):
            used_words.clear()
            print("ALL WORDS USED - Reset List\n")
            continue
        else:
            continue

    return word


def main():
    os.system(get_os(3))
    print(f"Word = {get_word()}")
    print(f"All Words: {fetch_words()}")
    print(f"Old Words: {used_words}")


while __name__ == '__main__':
    input()
    main()
