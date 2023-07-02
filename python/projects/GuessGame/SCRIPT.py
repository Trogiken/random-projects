import random

category_list = {
    "Trips": ['camper', 'drive', 'night', 'snacks', 'tent', 'bike', 'fire'],
    "Body": ['arm', 'leg', 'finger', 'nose', 'head', 'eye', 'ear'],
    "Summer": ['sun', 'sand', 'water', 'shades', 'swim', 'hot', 'beach'],
    "Animals": ['dog', 'cat', 'bird', 'fish', 'horse', 'snake', 'turtle'],
    }


def shuffle(lst: list, x: int):
    iterator = 1
    while iterator < x:
        random.shuffle(lst)
        iterator += 1


while __name__ == '__main__':
    categorys = list(category_list.keys())  # Makle list of keys
    shuffle(categorys, 5)  # Shuffle keys
    rdm_category = random.sample(population=categorys, k=1)[0]  # Get random key
    word_list = category_list.get(rdm_category)  # Get list from key
    shuffle(word_list, 5)  # Shuffle list
    rdm_word = word_list[random.randint(0, len(word_list)-1)]  # Get random word from list by index
    
    wrong_letters_guessed = []
    correct_letters_guessed = {}
    current_word_state = ['_' for _ in rdm_word]
    max_tries = 2 * len(rdm_word)

    while True:
        display_word = ''
        for letter in current_word_state:
            display_word += letter + ' '

        print(f"""
        Tries Left: {max_tries}
        Category: {rdm_category.capitalize()}

        {display_word.capitalize()}
        """)

        if max_tries == 0:
            print('You Lost!')
            break
        if [letter for letter in rdm_word] == current_word_state:
            print('You Won!')
            break

        letter_selected = input('> ')

        if not letter_selected.casefold() in rdm_word.casefold():
            wrong_letters_guessed.append(letter_selected)
            max_tries -= 1
        else:
            for index, letter in enumerate(rdm_word):
                if letter_selected == letter:
                    current_word_state[index] = letter_selected

    play_again = input('Play Again? (y/n): ').casefold()
    if not play_again == 'y':
        break
