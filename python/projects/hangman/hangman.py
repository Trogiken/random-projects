from assets import *
import os


def main():
    # Clear Console
    os.system(get_os(3))
    # Print Random Word
    print(get_word())
    print(config('port'))


while __name__ == '__main__':
    input()
    main()
