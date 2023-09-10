"""Celeb Quiz Program"""


quiz_data = {
    'score': {
            'harry': 0,
            'taylor': 0,
        },
    'questions': [("How would your friends describe you?", ["charismatic", "funny", "sweet", "generous"]),
                  ("What is your favorite thing to do at home?", ["sleep", "read", "meditate", "dance"]),
                  ("Which is your favorite animal?", ["hamster", "cat", "dog", "goldfish"]),
                  ("What is your favorite color?", ["purple", "blue", "yellow", "green"])],
    'persons': {
        'harry': ['charismatic', 'funny', 'meditate', 'dance', 'dog', 'goldfish', 'blue', 'green'],
        'taylor': ['sweet', 'generous', 'sleep', 'read', 'hamster', 'cat', 'purple', 'yellow'],
    }
}


def question_prompt(question_index: int) -> None:
    """Question prompt for user to input"""

    print(quiz_data['questions'][question_index][0])
    for index, option in enumerate(quiz_data['questions'][question_index][1]):
        index += 1
        print(f"{index}. {option}")

    while True:
        try:
            answer = int(input('> '))
            answer -= 1
            answer = quiz_data['questions'][question_index][1][answer]
            break
        except (ValueError, IndexError):
            print('Please enter a valid number')
            continue
            
    if answer in quiz_data['persons']['harry']:
        quiz_data['score']['harry'] += 1
    else:
        quiz_data['score']['taylor'] += 1


if __name__ == '__main__':
    print("Welcome to the Leah's Celeb Quiz!\n")

    for index, _ in enumerate(quiz_data['questions']):
        question_prompt(index)

    print("\nThe celebrity you are is...")
    if quiz_data['score']['harry'] == quiz_data['score']['taylor']:
        print("It's a tie!")
    elif quiz_data['score']['harry'] > quiz_data['score']['taylor']:
        print("Harry Styles!")
    else:
        print("Taylor Swift!")
