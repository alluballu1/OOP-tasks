# File name: MammalClass.py
# Author: Alex Porri
# Description: Class for creating mammal objects,

import random


class Mammal:

    def __init__(self, init_species, init_name, init_width, init_height, init_length, init_weight):
        # Creating the attributes. Size is just height multiplied by width (all animals are box/cube shaped)

        self.__species = init_species
        self.__name = init_name
        self.__weight = init_weight
        self.__width = init_width
        self.__height = init_height
        self.__length = init_length
        self.__size = self.__height * self.__width * self.__length
        self.__id = random.randint(1, 6)

    # Creating the accessor functions

    def get_species(self):
        return self.__species

    def get_name(self):
        return self.__name

    def get_weight(self):
        return self.__weight

    def get_width(self):
        return self.__width

    def get_height(self):
        return self.__height

    def get_length(self):
        return self.__length

    def get_size(self):
        return self.__size

    def get_id(self):
        return self.__id

    # Creating the mutator functions

    def set_species(self):
        self.__species = input("Set a new species: ")

    def set_name(self):
        self.__name = input("Set a new name: ")

    def set_weight(self):
        self.__weight = float(input("Set a new weight: "))

    def set_width(self):
        self.__width = float(input("Set a new width: "))

    def set_height(self):
        self.__height = float(input("Set a new height: "))

    def set_length(self):
        self.__length = float(input("Set a new length: "))

    def set_id(self):
        self.__id = random.randint(1, 6)
        print("New randomly chosen ID number set!")

    # Creating the string method

    def __str__(self):
        return f"""The data of the animal you've given: 
Name: {self.__name}
Species: {self.__species}
Weight: {str(self.__weight)}kg
Height: {str(self.__height)}m
Length: {str(self.__length)}m
Width: {str(self.__width)}m
Size: {str(self.__size)}m^3
ID: {str(self.__id)}"""
