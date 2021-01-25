# File name: Exercise3Task6.py
# Author: Alex Porri
# Description: Dice class for rolling, two objects, rolling both and getting the sum of them.

import random
# Creating the dice class
class Dice:

    def __init__(self):

        # List of colors and the dice's see-throughness

        LIST_OF_COLORS = ("Blue", "Green", "Cyan", "Red")
        SOLIDNESS = ("Opaque", "Translucent")

        # See-through, color and the eye value are selected at random. All attributes are private.

        self.__color = LIST_OF_COLORS[random.randint(0, 3)]
        self.__Number_up = random.randint(1, 6)
        self.__translucent_or_opaque = SOLIDNESS[random.randint(0, 1)]

    # Function for rolling the dice

    def roll_dice(self):
        self.__Number_up = random.randint(1, 6)

    # get functions for returning wanted values

    def get_color(self):
        return self.__color

    def get_side_up(self):
        return self.__Number_up

    def get_solidness(self):
        return self.__translucent_or_opaque

def main():
    my_dice = Dice()
    your_dice = Dice()

    my_dice.roll_dice()
    your_dice.roll_dice()

    FIRST_VALUE = my_dice.get_side_up()
    SECOND_VALUE = your_dice.get_side_up()
    print("My dice value: " + str(FIRST_VALUE), "Your dice value: " + str(SECOND_VALUE), "Sum of the two values: " +
          str(FIRST_VALUE+SECOND_VALUE), sep="\n")

main()