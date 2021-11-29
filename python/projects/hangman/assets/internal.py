from yaml import safe_load


def config(key):
    """Process yaml and output requested variable"""
    with open('config.yaml', 'r') as file:
        data = safe_load(file)

    options = ['default', 'multiplier', 'decrease', 'allowed_attempts', 'high_score']
    config_variable = None
    if key not in options:
        return config_variable
    elif key == 'default':
        config_variable = data['score']['default']
    elif key == 'multiplier':
        config_variable = data['score']['multiplier']
    elif key == 'decrease':
        config_variable = data['score']['decrease']
    elif key == 'allowed_attempts':
        config_variable = data['player']['allowed_attempts']
    elif key == 'high_score':
        config_variable = data['player']['high_score']

    return config_variable


class Game:
    looped_words = []


class Player:
    score = config('default')
    multiplier = config('multiplier')
    decrease = config('decrease')
    high_score = 0
    used_chars = ['u']
