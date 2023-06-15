class Animals:
    class Cow:
        legs = 4
        colors = ['Brown', 'White', 'Spotted']

    class Pig:
        legs = 4

    class Chicken:
        legs = 2
          

def calclegs(chickens, cows, pigs):
	chickenlegs = chickens * Animals.Chicken.legs
	cowlegs = cows * Animals.Cow.legs
	piglegs = pigs * Animals.Pig.legs
	return chickenlegs + cowlegs + piglegs



print(calclegs(2, 4, 10))
print(Animals.Cow.colors)