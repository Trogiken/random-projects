import pickle
import os
import hashlib


class Animal:
    """A class representing an animal"""
    def __init__(self, legs=None, colors=None):
        """Initialize the Animal instance"""
        self.legs = legs
        self.colors = colors

    def __str__(self):
        """Return a string representation of the instance"""
        return f"legs: {self.legs}, colors: {self.colors}"

    def __repr__(self):
        """Return a string representation of the instance"""
        return f"Animal(legs={self.legs}, colors={self.colors})"


class Cow(Animal):
    """A class representing a cow"""
    def __init__(self, legs=None, colors=None):
        """Initialize the Cow instance"""
        default_legs = 4
        default_colors = ['Brown', 'White', 'Spotted']
        super().__init__(legs or default_legs, colors or default_colors)


class Pig(Animal):
    """A class representing a pig"""
    def __init__(self, legs=None, colors=None):
        """Initialize the Pig instance"""
        default_legs = 4
        default_colors = ['Pink', 'Black', 'Spotted']
        super().__init__(legs or default_legs, colors or default_colors)


class Chicken(Animal):
    """A class representing a chicken"""
    def __init__(self, legs=None, colors=None):
        """Initialize the Chicken instance"""
        default_legs = 2
        default_colors = ['White']
        super().__init__(legs or default_legs, colors or default_colors)


def save_animals(filename, **animals):
    """Save all animal instances into a single file"""
    animal_data = {}
    for name, animal in animals.items():
        # Store the animal instance in the dictionary with the name as the key
        animal_data[name] = animal
    with open(filename, 'wb') as f:
        pickle.dump(animal_data, f)

    # Calculate the hash of the serialized data
    serialized_data = pickle.dumps(animal_data)
    hash_value = hashlib.sha256(serialized_data).hexdigest()
    # Store the hash value in the dictionary
    animal_data['__hash__'] = hash_value
    # Save the animal data again with the hash
    with open(filename, 'wb') as f:
        pickle.dump(animal_data, f)


def load_animals(filename):
    """Load all animal instances from a single file"""
    with open(filename, 'rb') as f:
        loaded_data = pickle.load(f)

    # Retrieve the hash value and remove it from the dictionary
    hash_value = loaded_data.pop('__hash__', None)
    # Calculate the hash of the serialized data by loading the data again
    serialized_data = pickle.dumps(loaded_data)
    calculated_hash = hashlib.sha256(serialized_data).hexdigest()

    print('Saved Hash:', hash_value)
    print('Calculated Hash:', calculated_hash)

    # This verifies if data is tampered, not the authenticity of the class code itself!
    if hash_value != calculated_hash:
        print('Data has been tampered with!')
    else:
        print('Data is intact!')

    return loaded_data


def calculate_total_legs(animals):
    """Calculate the total number of legs"""
    total_legs = 0
    for animal in animals:
        total_legs += animal.legs
    return total_legs


# Create instances of the animals with custom attributes
cow = Cow()
pig = Pig()
chicken = Chicken()

print()

# Save all animal instances into a single file with the file being in the same directory as this file
save_animals(os.path.join(os.path.dirname(__file__), 'animal_data.pkl'), cow=cow, pig=pig, chicken=chicken)
# Load the animal instances from the file
loaded_animals = load_animals(os.path.join(os.path.dirname(__file__), 'animal_data.pkl'))

# Access the loaded animal instances by their names
loaded_cow = loaded_animals['cow']
loaded_pig = loaded_animals['pig']
loaded_chicken = loaded_animals['chicken']

# Example of using __str__ and __repr__
print('loaded_cow:', loaded_cow)
# Example of using __eq__ and __ne__
print('loaded_cow == loaded_pig:', loaded_cow is loaded_pig)

print()

# Example of using __getattr__
print('loaded_cow legs:', loaded_cow.legs)
print('loaded_pig legs:', loaded_pig.legs)
print('loaded_chicken legs:', loaded_chicken.legs)
print('-' * 25)

# Calculate the total number of legs
animals = [loaded_cow, loaded_pig, loaded_chicken]
total_legs = calculate_total_legs(animals)
print("Total number of legs:", total_legs, '\n')
