# File name: CharacterClass
# Author: Alex Porri
# Description: Class for creating the character.

# Importing the player class

from PlayerClass import Player


class Character(Player):

    def __init__(self, name, age, experience, race, character_class, character_name):
        super().__init__(name, age, experience)
        self.__race = race
        self.__character_class = character_class
        self.__character_name = character_name
        self.__intellect = None
        self.__strength = None
        self.__dexterity = None
        self.__constitution = None

    # Mutator functions

    def set_race(self, race):
        self.__race = race

    def set_character_class(self, character_class):
        self.__character_class = character_class

    def set_character_name(self, character_name):
        self.__character_name = character_name

    def set_intellect(self, int):
        self.__intellect = int

    def set_strength(self, str):
        self.__strength = str

    def set_dexterity(self, dex):
        self.__dexterity = dex

    def set_constitution(self, const):
        self.__constitution = const

    # Accessor functions

    def get_race(self):
        return self.__race

    def get_character_class(self):
        return self.__character_class

    def get_character_name(self):
        return self.__character_name

    def get_intellect(self):
        return self.__intellect

    def get_strength(self):
        return self.__strength

    def get_dexterity(self):
        return self.__dexterity

    def get_constitution(self):
        return self.__constitution

    # str function.

    def __str__(self):
        return f"Player name: {self.get_name()}" \
               f"\nPlayer age: {str(self.get_age())}"\
               f"\nPlayer experience with D&D: {self.get_experience()}" \
               f"\nPlayer's D&D character statistics: "\
             f"\nCharName: {self.__character_name}" \
             f"\nRace: {self.__race}" \
             f"\nClass: {self.__character_class}" \
             f"\nCharacter statistics: " \
             f"\nIntellect: {str(self.__intellect)}" \
             f"\nStrength: {str(self.__strength)}" \
             f"\nDexterity: {str(self.__dexterity)}" \
             f"\nConstitution: {str(self.__constitution)}"

