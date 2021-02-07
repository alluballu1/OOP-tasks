# File name: Exercise4Task8.py
# Author: Alex Porri
# Description: Checks if the animal objects fit in the car and match the rolled ID

import MammalClass
import DiceClass
import CarClass as Car


# init_species, init_name, init_width, init_height, init_length, init_weight


# Creating the animal, dice and car objects

first_animal = MammalClass.Mammal("Dog", "Kake", 0.2, 0.3, 0.5, 10)
second_animal = MammalClass.Mammal("Cat", "Peter", 0.2, 0.3, 0.5, 6)
third_animal = MammalClass.Mammal("Crocodile", "Snappy", 0.5, 0.3, 2.5, 150)
fourth_animal = MammalClass.Mammal("Elephant", "Dumbo", 2, 4, 5, 7000)
new_dice = DiceClass.Dice()
my_car = Car.Car("Opel", "Cadet", 100000, 35000, "Red", 100, 1)

# Creating a list of the animals
animals = [first_animal, second_animal, third_animal, fourth_animal]

# Creating the main function

def main():

    # Rolling the dice
    new_dice.roll_dice()

    # Using if-else to find out if any of the animals have matching ID's

    for animal in animals:
        if animal.get_id() == new_dice.get_side_up():
            print(str(animal.get_name()) + "'s ID matches to the dice roll!")

            if animal.get_size() <= my_car.get_trunk_size():
                print("The animal fits!")

                if animal.get_weight() >= my_car.get_max_load():
                    print(str(animal.get_name()) + " fits but is too heavy.")

                else:
                    print(animal)
                    # Function stops at the first animal that has matching ID, size and weight.
                    exit()

            else:
                print(str(animal.get_name())+ " does not fit in the trunk.")

    print("None fit or match the ID.")


main()


