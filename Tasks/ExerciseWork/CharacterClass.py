# File name: CharacterClass
# Author: Alex Porri
# Description: Class for creating the character.

# Importing the player class

from PlayerClass import Player


class Character(Player):

    def __init__(self, name, age, experience):
        super().__init__(name, age, experience)
        self.__race = "None"
        self.__character_class = "None"
        self.__character_name = "None"
        self.__intellect = "None"
        self.__strength = "None"
        self.__dexterity = "None"
        self.__constitution = "None"

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

    #def get_age(self):
        #return self.get_age()

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

    # Added a function for printing out all of the data

    def get_all(self):
        return f"===========PLAYER INFO==========="\
               f"\nPlayer name: {self.get_name()}" \
               f"\nPlayer age: {self.get_age()}" \
               f"\nPlayer experience: {self.get_experience()}" \
               f"\n===========D&D CHARACTER INFO===========" \
               f"\nCharacter name: {self.__character_name}" \
               f"\nCharacter  race: {self.__race}" \
               f"\nCharacter class: {self.__character_class}" \
               f"\nIntellect: {self.__intellect}" \
               f"\nStrength: {self.__strength}" \
               f"\nDexterity: {self.__dexterity}" \
               f"\nConstitution: {self.__constitution}"

    # str function.

    def __str__(self):
        return self.get_name()

