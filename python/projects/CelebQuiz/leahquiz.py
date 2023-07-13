"""Leahness"""

score = {
    'harry': 0,
    'taylor': 0,
}

questions_quiz = {
    'question_one_answers': ["charismatic", "funny", "sweet", "generous"], # CORRECT
    # question_two_answers = "sleep, read, meditate, dance",  
    # question_three_answers = "hamster, cat, dog, goldfish",
    # question_four_answers = "blue, yellow, green, purple",
}


def question_one():
    """Func for q1"""
    q1 = questions_quiz.get('question_one_answers')

    print("How would your friends describe you?\n")
    for index, option in enumerate(q1):
        index += 1
        print(f"{index}. {option}")

    answer = input('> ')

    if answer in ['1', '2']:
        print('One point for Harry')
        score['harry'] += 1
    else:
        print('One point for Taylor')
        score['taylor'] += 1


# def question_two(input())
# return('What is your favorite thing to do at home?')


# if question_two == question_two_answers[2]:
#     print('One point for Harry')
# else:
#     print('One point for Taylor')




# def question_three(input())
# return('Which is your favorite animal?')


# if question_three == question_three_answers([2], [3]):
#     print('One point for Harry')
# else:
#     print('One point for Taylor')


# question_four = input()


if __name__ == '__main__':
    print("Find which celebrity you are!\n")
    
    question_one()
    question_two()
    question_three()
    question_four()

    # use score to compare what celeb the user is
