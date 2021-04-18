# File name: AnimalClass.py
# Author: Alex Porri
# Description: Class for creating Animal objects,

class Animal:

    def __init__(self, init_species, init_name):

        self.__species = init_species
        self.__name = init_name

    # Creating the accessor functions

    def get_species(self):
        return self.__species

    def get_name(self):
        return self.__name

    # Creating the mutator functions

    def set_species(self):
        self.__species = input("Set a new species: ")

    def set_name(self):
        self.__name = input("Set a new name: ")

    # Creating the string method

    def __str__(self):
        return f"""The data of the animal you've given: 
Name: {self.__name}
Species: {self.__species}
"""
