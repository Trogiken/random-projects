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
        elif int(len(used_words)) == len(fetch_words()):
            print("ALL WORDS USED - Resetting List\n")
            used_words.clear()
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
