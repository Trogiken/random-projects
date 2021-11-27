from assets import *
import os

used_words = []


def get_word():
    """Generate a random non-repeating word"""
    while True:
        word = random_word()
        if word not in used_words:
            used_words.append(word)
            break
        elif len(used_words) == len(fetch_words()):
            print("ALL WORDS USED - Resetting List\n")
            used_words.clear()
            continue
        else:
            continue

    return word


def main():
    print(get_word())


while __name__ == '__main__':
    input()
    os.system(get_os(3))
    main()
    print(f"All Words: {fetch_words()}")
    print(f"Old Words: {used_words}")
