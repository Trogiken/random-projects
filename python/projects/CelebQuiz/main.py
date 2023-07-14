"""
print theme

create a LIST of options for each question
Use a for loop to print all the questions under the question - OPTIONAL
store the user's answer in a variable for each question

    print all the questions under the theme in sequence:
        Question 1
        for loop for question 1 options:

use if statements to determine what celebrity the user is
"""

score = {
    'harry': 0,
    'taylor': 0,
}

questions_quiz = {
    'question_one_answers': ["charismatic", "funny", "sweet", "generous"],
    'question_two_answers': ["sleep", "read", "meditate", "dance"],  
    'question_three_answers': ["hamster", "cat", "dog", "goldfish"],
    'question_four_answers': ["blue", "yellow", "green", "purple"],
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


def question_two():
    """Function for q2"""
q2 = questions_quiz.get('question_two_answers')

print("What is your favorite thing to do at home?\n")
for index, option in enumerate(q2):
    index += 1
    print(f"{index}, {option}")

answer = input('> ')

if answer in ['3', '4']:
    print('One point for Harry')
    score['harry'] += 1
else:
    print('One point for Taylor')
    score['taylor'] += 1


def question_three():
    """Function for q3"""
q3 = questions_quiz.get('question_three_answers')

print("Which is your favorite animal?\n")
for index, option in enumerate(q3):
    index += 1
    print(f"{index}, {option}")

answer = input('> ')

if answer in ['3', '4']:
    print('One point for Harry')
    score['harry'] += 1
else:
    print('One point for Taylor')
    score['taylor'] += 1


def question_four():
    """Function for q4"""
q4 = questions_quiz.get('question_four_answers')

print("What is your favorite color?\n")
for index, option in enumerate(q4):
    index += 1
    print(f"{index}, {option}")

answer = input('> ')

if answer in ['1', '3']:
    print('One point for Harry')
    score['harry'] += 1
else:
    print('One point for Taylor')
    score['taylor'] += 1


if __name__ == '__main__':
    print("The celebrity you are is...\n")

    question_one()
    question_two()
    question_three()
    question_four()

if score['harry'] == score['taylor']:
    print('It was a tie!')


elif score['harry'] >= score['taylor']:
    print('You are Harry Styles!')
else:
    print('You are Taylor Swift!')