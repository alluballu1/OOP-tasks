# File name: Exercise5Task5.py
# Author: Alex Porri
""" Description: Creating a list of players and a dictionary that uses player id's as keys. Printing out
dice values before and after rolling"""

# Importing the classes

import PlayerClass
import DiceClass


# Creating the function that creates the list of players

def create_players():
    list_of_players = []
    player_count = int(input("Player count: "))
    for each_player in range(player_count):
        player_first_name = input("Player number " + str(each_player + 1) + "' first name: ")
        player_last_name = input("Player number " + str(each_player + 1) + "' last name: ")
        new_player = PlayerClass.PlayerClass(player_first_name, player_last_name, each_player)
        list_of_players.append(new_player)
    return list_of_players


# Creating the function that creates the dictionary based on the list of players

def create_dictionary(players):
    dictionary = {}
    for each_player in players:
        new_dice = DiceClass.Dice()
        dictionary[each_player.get_player_id()] = new_dice
    return dictionary


# Main function that contains the list and the dictionary. List is printed out and the player id is used to find the
# correct dice to roll and print the values of it

def main():
    new_list = create_players()
    dictionary = create_dictionary(new_list)
    for each in new_list:
        print()
        print("Player: " + each.get_first_name() + " " + each.get_last_name() + " with ID: " + str(each.get_player_id())
              + " rolled a value number: " + str(dictionary[each.get_player_id()]), "Re-rolling!", sep="\n")
        dictionary[each.get_player_id()].roll_dice()
        print("New info: ",
              "Player: " + each.get_first_name() + " " + each.get_last_name() + " with ID: " + str(each.get_player_id())
              + " rolled a value number: " + str(dictionary[each.get_player_id()]), sep="\n")


# Calling main function
main()
