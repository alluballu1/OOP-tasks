# File name: Testfile.py
# Author: Alex Porri
# Description: A file for testing the classes that will be used in the main program.

from CharacterClass import Character

def main():
    name = input("Player name: ")
    age = int(input("Player age: "))
    experience = input("Experience with D&D: ")
    char_name = input("Character name: ")
    char_race = input("Character race: ")
    char_class = input("Character class: ")

    test_player = Character(name,age,experience,char_race,char_class,char_name)
    print(" ", test_player, sep="\n")

main()

