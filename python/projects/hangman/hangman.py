from assets import *
import os


def output(word):
    out = \
        f"""
    High Score: {Player.high_score}
    Score: {Player.score}
    
            {word}
     
    Used {Player.used_chars}
    Tries Left: 
        """

    return out


def main():
    os.system(get_os(3))
    word = get_word()
    print(output(word))


while __name__ == '__main__':
    input()
    main()
