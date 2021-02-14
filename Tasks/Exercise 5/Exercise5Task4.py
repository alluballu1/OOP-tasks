# File name: Exercise5Task4.py
# Author: Alex Porri
# Description: List of dice objects, simple game where the player with the highest sum of 3 rolls wins

import DiceClass

# Creating the object lists with a custom dice count

def create_list():
    player_list = []
    number_of_dice = input("How many dice are used: ")
    for player in range(int(number_of_dice)):
        new_player = DiceClass.Dice()
        player_list.append(new_player)
    return player_list

# Creating a function for rolling the dice objects, appending the values to a list and then returning the sum

def rolling_and_sum(list_of_dice):
    dice_eye_values = []
    for each_player in list_of_dice:
        each_player.roll_dice()
        dice_eye_values.append(each_player.get_side_up())
    return sum(dice_eye_values)

# The main game function that is called from the main function

def playing_game(first_player, second_player):

    # Rolling both die lists

    first_player_roll = rolling_and_sum(first_player)
    second_player_roll = rolling_and_sum(second_player)
    if first_player_roll > second_player_roll:
        print("You won!", first_player_roll, "VS Computer, who rolled:", second_player_roll)
        print()
    elif first_player_roll < second_player_roll:
        print("Computer won with", second_player_roll, "VS your", first_player_roll)
        print()
    else:
        print("Tie. Rolling again!")
        print()
        playing_game(first_player,second_player)

# Main function that loops indefinitely until the player chooses to sop by typing N or n when prompted.

def main():
    while True:
        play = input("Play a game? Y/N: ")
        if play == "Y" or play == "y":
            list_of_die = create_list()
            playing_game(list_of_die, list_of_die)
        elif play == "N" or play == "n":
            break
        else:
            print("Input error, try again.")
            continue


main()
