import random

category_list = {
    "Trips": ['camper', 'drive', 'night'],
    "Body": ['penis', 'pussy'],
    "Summer": ['sun', 'sand', 'water', 'shades'],
    "Animals": ['dog', 'cat', 'bird', 'fish'],
    }


while __name__ == '__main__':
    rdm_category = random.sample(population=list(category_list.keys()), k=1)[0]
    word_list = category_list.get(rdm_category)
    rdm_word = word_list[random.randint(0, len(word_list)-1)].casefold()
    wrong_letters_guessed = []
    correct_letters_guessed = {}
    current_word_state = ['_' for _ in rdm_word]
    max_tries = 2 * len(rdm_word)

    win = True
    while True:
        display_word = ''
        for letter in current_word_state:
            display_word += letter + ' '

        print(f"""
        Tries Left: {max_tries}
        Category: {rdm_category}

        {display_word}
        """)

        if max_tries == 0:
            win = False
            break
        if [letter for letter in rdm_word] == current_word_state:
            break

        letter_selected = input('> ').casefold()

        if not letter_selected in rdm_word:
            wrong_letters_guessed.append(letter_selected)
            max_tries -= 1
        else:
            for index, letter in enumerate(rdm_word):
                if letter_selected == letter:
                    current_word_state[index] = letter_selected
                
    if win:
        print('You Won!')
    else:
        print('You Lost!')

    play_again = input('Play Again? (y/n): ').casefold()
    if play_again == 'y':
        continue
