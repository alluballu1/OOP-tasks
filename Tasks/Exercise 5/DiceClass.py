# File name: DiceClass.py
# Author: Alex Porri
# Description: Dice class for rolling

import random
# Creating the dice class
class Dice:

    def __init__(self):

        # List of colors and the dice's see-throughness

        LIST_OF_COLORS = ("Blue", "Green", "Cyan", "Red")
        SOLIDNESS = ("Opaque", "Translucent")

        # See-through, color and the eye value are selected at random. All attributes are private.

        self.__color = LIST_OF_COLORS[random.randint(0, 3)]
        self.__number_up = random.randint(1, 6)
        self.__translucent_or_opaque = SOLIDNESS[random.randint(0, 1)]

    # Function for rolling the dice

    def roll_dice(self):
        self.__number_up = random.randint(1, 6)

    # get functions for returning wanted values

    def get_color(self):
        return self.__color

    def get_side_up(self):
        return self.__number_up

    def get_solidness(self):
        return self.__translucent_or_opaque

    def __str__(self):
        return str(self.__number_up)

