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
        self.__number_up = random.randint(1, 6)
        self.__translucent_or_opaque = SOLIDNESS[random.randint(0, 1)]
        self.player_number = 0

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


# Created players as global variables so that passing data would be easier

first_player = Dice()
second_player = Dice()
third_player = Dice()

# Main function for calling the first round of dice rolling, passing the global variables

def main():
    first_round(first_player, second_player, third_player)

# First round of dice rolling

def first_round(first, second, third):

    # "Naming" the players

    first.player_number = 1
    second.player_number = 2
    third.player_number = 3

    # Rolling the dice

    first.roll_dice()
    second.roll_dice()
    third.roll_dice()

    # Getting the rolled dice values

    first_value = first.get_side_up()
    second_value = second.get_side_up()
    third_value = third.get_side_up()

    # Printing out the first round dice values and the players

    print("Round number 1:", "Player number 1 rolled: " + str(first_value), "Player number 2 rolled: " +
          str(second_value), "Player number 3 rolled: " + str(third_value), sep="\n")

    # If-else to check who gets into the second round, if tied the first round is called again.
    # winner data is passed to the second round

    if first_value == second_value == third_value:
        print("TIED!")
        first_round(first, second, third)
    if first_value < second_value and third_value:
        print("Player number 1 dropped off!")
        second_round(second, third)
    elif second_value < first_value and third_value:
        print("Player number 2 dropped off!")
        second_round(first, third)
    else:
        print("Player number 3 dropped off!")
        second_round(first, second)


# The second round function

def second_round(first_player_2nd_round, second_player_2nd_round):

    # Passed objects are used to make new variables within the second round function

    first_player_2nd_round = first_player_2nd_round
    second_player_2nd_round = second_player_2nd_round

    # The dice are rolled, again.

    first_player_2nd_round.roll_dice()
    second_player_2nd_round.roll_dice()

    # Getting the new rolled values for both dice

    first_player_new_dice_value = first_player_2nd_round.get_side_up()
    second_player_new_dice_value = second_player_2nd_round.get_side_up()

    # Printing out the player numbers of the round and the values they rolled

    print("Round number 2:", "Player number " + str(first_player_2nd_round.player_number) +
          " rolled: " + str(first_player_new_dice_value),
          "Player number " + str(second_player_2nd_round.player_number) + " rolled: " +
          str(second_player_new_dice_value), sep="\n")

    # Checking with if-else who won the game. If it's tied, the function is called again.

    if second_player_new_dice_value == first_player_new_dice_value:
        print("TIED! Rolling again!")
        second_round(first_player_2nd_round, second_player_2nd_round)
    elif first_player_new_dice_value > second_player_new_dice_value:
        print("Player number " + str(first_player_2nd_round.player_number) + " wins!")
    else:
        print("Player number " + str(second_player_2nd_round.player_number) + " wins!")


# Calling the main function

main()
