import math
myFavFoods = {"rice", "chicken", "pizza"}
yourFavFoods = set()

ordinalNumbers = ["st","rd", "th"]

def getordinalNumber(value: int):
    if len(ordinalNumbers) > value:
        return ordinalNumbers[value]
    else:
       return ordinalNumbers[-1]

for i in range(5):
    yourFavFood = input(f'Whats your {i}{getordinalNumber(i + 1)} favorite food? ')
    yourFavFoods.add(yourFavFood.lower())

print(yourFavFoods.intersection(myFavFoods))