# File name: CellPhoneClass.py
# Author: Alex Porri
# Description: Phone class with user input, changed a bit (added ID and parameters into the init function)

# Creating the class
import random

class CellPhone:

    # Initialization

    def __init__(self, init_manufact, init_model, init_retail_price):

        # Creating the attributes, all private

        self.__manufact = init_manufact
        self.__model = init_model
        self.__retail_price = init_retail_price
        self.__id = random.randint(1,6)

    # functions for setting the manufacturer, model and retail price

    def set_manufact(self):
        self.__manufact = input("Enter the manufacturer: ")

    def set_model(self):
        self.__model = input("Enter the model: ")

    def set_retailprice(self):
        self.__retail_price = float(input("Enter the retail price: "))

    def set_id(self):
        self.__id = random.randint(1,6)

    # functions for getting and returning the manufacturer, model and retail price

    def get_manufact(self):
        return self.__manufact

    def get_model(self):
        return self.__model

    def get_retailprice(self):
        return self.__retail_price

    def get_id(self):
        return self.__id

# For some reason the formatting gets messed up on the console lines if I add spaces to the code itself

    def __str__(self):
        return f"""The information you've given:
Manufacturer: {self.__manufact}
Model: {self.__model}
Retail price: {str(self.__retail_price)}
Phone ID: {str(self.__id)}
"""
