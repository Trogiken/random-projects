import random

tools = {
    '1': {
        'name': 'Paper',
        'wins': '2',
        'fails': '3',
    },
    '2': {
        'name': 'Rock',
        'wins': '3',
        'fails': '1',
    },
    '3': {
        'name': 'Scissors',
        'wins': '1',
        'fails': '2'
    }
}

while True:
    print("""
    Rock Paper Scissors

    1. Paper
    2. Rock
    3. Scissors
    """)
    player = input('> ')
    ai_player = str(random.randint(1, 3))
    print()

    if not player in tools:
        print('Invalid Option')
        continue

    print(f"Player: {tools[player].get('name')}")
    print(f"AI: {tools[ai_player].get('name')}")

    if player == ai_player:
        print('Tie!')
        continue
    if tools[player].get('wins') != tools[ai_player].get('fails'):
        print('Player Wins!')
    else:
        print('AI Wins!')
