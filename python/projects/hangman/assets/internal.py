from yaml import safe_load


def config(key):
    with open('yaml.yaml', 'r') as file:
        prime_service = safe_load(file)

    options = ['url', 'port', 'prime']
    config_variable = None
    if key not in options:
        return config_variable
    elif key == 'url':
        config_variable = prime_service['rest']['url']
    elif key == 'port':
        config_variable = prime_service['rest']['port']
    elif key == 'prime':
        config_variable = prime_service['prime_numbers']

    return config_variable


class Game:
    used_words = []


class Player:
    pass
