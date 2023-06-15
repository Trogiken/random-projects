import pickle

class Animal:
    def __init__(self, legs=None, colors=None):
        self.legs = legs
        self.colors = colors

    def save(self, filename):
        with open(filename, 'wb') as f:
            pickle.dump(self, f)

    @staticmethod
    def load(filename):
        with open(filename, 'rb') as f:
            return pickle.load(f)


class Cow(Animal):
    def __init__(self, legs=None, colors=None):
        default_legs = 4
        default_colors = ['Brown', 'White', 'Spotted']
        super().__init__(legs or default_legs, colors or default_colors)


class Pig(Animal):
    def __init__(self, legs=None, colors=None):
        default_legs = 4
        default_colors = ['Pink', 'Black', 'Spotted']
        super().__init__(legs or default_legs, colors or default_colors)


class Chicken(Animal):
    def __init__(self, legs=None, colors=None):
        default_legs = 2
        default_colors = ['White']
        super().__init__(legs or default_legs, colors or default_colors)


def calculate_total_legs(animals):
    total_legs = 0
    for animal in animals:
        if animal.legs is not None:
            total_legs += animal.legs
    return total_legs


# Create instances of the animals with custom attributes
cow = Cow(legs=4, colors=['Brown', 'White'])
pig = Pig(colors=['Pink', 'Black'])
chicken = Chicken(legs=2)

# Save each animal instance
cow.save('cow.pkl')
pig.save('pig.pkl')
chicken.save('chicken.pkl')

# Load the animal instances
loaded_cow = Cow.load('cow.pkl')
loaded_pig = Pig.load('pig.pkl')
loaded_chicken = Chicken.load('chicken.pkl')

print("loaded_cow legs:", loaded_cow.legs)
print("loaded_pig legs:", loaded_pig.legs)
print("loaded_chicken legs:", loaded_chicken.legs)

# Calculate the total number of legs
animals = [loaded_cow, loaded_pig, loaded_chicken]
total_legs = calculate_total_legs(animals)
print("Total number of legs:", total_legs)
