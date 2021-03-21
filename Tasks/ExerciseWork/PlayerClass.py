# File name: PlayerClass
# Author: Alex Porri
# Description: Class for creating the player.

class Player:

    def __init__(self, name, age, experience):
        self.__name = name
        self.__age = age
        self.__experience = experience

    # Mutators functions

    def set_name(self, name):
        self.__name = name

    def set_age(self, age):
        self.__age = age

    def set_experience(self, experience):
        self.__experience = experience

    # Accessor functions

    def get_name(self):
        return self.__name

    def get_age(self):
        return self.__age

    def get_experience(self):
        return self.__experience

    # Str function

    def __str__(self):
        return f"Name: {self.__name}" \
        f"\nAge: {str(self.__age)}" \
        f"\nExperience: {self.__experience}"

