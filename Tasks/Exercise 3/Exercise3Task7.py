# File name: Exercise3Task7.py
# Author: Alex Porri
# Description: Dice class for rolling, three-way game of dice


import random


# Creating the dice class
class Dice:

    def __init__(self):
        # List of colors and the dice's tanslucency

        LIST_OF_COLORS = ("Blue", "Green", "Cyan", "Red")
        SOLIDNESS = ("Opaque", "Translucent")

        # See-through, color and the eye value are selected at random. All attributes are private.

        self.__color = LIST_OF_COLORS[random.randint(0, 3)]
        self.__Number_up = random.randint(1, 6)
        self.__translucent_or_opaque = SOLIDNESS[random.randint(0, 1)]
        self.player_number = 0

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


# Created players as global variables so that passing data would be easier

FIRST_PLAYER = Dice()
SECOND_PLAYER = Dice()
THIRD_PLAYER = Dice()

# Main function for calling the first round of dice rolling, passing the global variables

def main():
    first_round(FIRST_PLAYER, SECOND_PLAYER, THIRD_PLAYER)

# First round of dice rolling

def first_round(FIRST, SECOND, THIRD):

    # "Naming" the players

    FIRST.player_number = 1
    SECOND.player_number = 2
    THIRD.player_number = 3

    # Rolling the dice

    FIRST.roll_dice()
    SECOND.roll_dice()
    THIRD.roll_dice()

    # Getting the rolled dice values

    FIRST_VALUE = FIRST.get_side_up()
    SECOND_VALUE = SECOND.get_side_up()
    THIRD_VAlUE = THIRD.get_side_up()

    # Printing out the first round dice values and the players

    print("Round number 1:", "Player number 1 rolled: " + str(FIRST_VALUE), "Player number 2 rolled: " +
          str(SECOND_VALUE), "Player number 3 rolled: " + str(THIRD_VAlUE), sep="\n")

    # If-else to check who gets into the second round, if tied the first round is called again.
    # winner data is passed to the second round

    if FIRST_VALUE == SECOND_VALUE == THIRD_VAlUE:
        print("TIED!")
        first_round(FIRST, SECOND, THIRD)
    if FIRST_VALUE < SECOND_VALUE and THIRD_VAlUE:
        print("Player number 1 dropped off!")
        second_round(SECOND, THIRD)
    elif SECOND_VALUE < FIRST_VALUE and THIRD_VAlUE:
        print("Player number 2 dropped off!")
        second_round(FIRST, THIRD)
    else:
        print("Player number 3 dropped off!")
        second_round(FIRST, SECOND)


# The second round function

def second_round(FIRST_PLAYER, SECOND_PLAYER):

    # Passed objects are used to make new variables within the second round function

    FIRST_PLAYER = FIRST_PLAYER
    SECOND_PLAYER = SECOND_PLAYER

    # The dice are rolled, again.

    FIRST_PLAYER.roll_dice()
    SECOND_PLAYER.roll_dice()

    # Getting the new rolled values for both dice

    FIRST_PLAYER_NEW_DICE_VALUE = FIRST_PLAYER.get_side_up()
    SECOND_PLAYER_NEW_DICE_VALUE = SECOND_PLAYER.get_side_up()

    # Printing out the player numbers of the round and the values they rolled

    print("Round number 2:", "Player number " + str(FIRST_PLAYER.player_number) +
          " rolled: " + str(FIRST_PLAYER_NEW_DICE_VALUE),
          "Player number " + str(SECOND_PLAYER.player_number) + " rolled: " +
          str(SECOND_PLAYER_NEW_DICE_VALUE), sep="\n")

    # Checking with if-else who won the game. If it's tied, the function is called again.

    if SECOND_PLAYER_NEW_DICE_VALUE == FIRST_PLAYER_NEW_DICE_VALUE:
        print("TIED! Rolling again!")
        second_round(FIRST_PLAYER, SECOND_PLAYER)
    elif FIRST_PLAYER_NEW_DICE_VALUE > SECOND_PLAYER_NEW_DICE_VALUE:
        print("Player number " + str(FIRST_PLAYER.player_number) + " wins!")
    else:
        print("Player number " + str(SECOND_PLAYER.player_number) + " wins!")


# Calling the main function

main()
