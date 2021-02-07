# File name: Exercise3Task8.py
# Author: Alex Porri
# Description: Phone class with user input

# Creating the class

class CellPhone:

    # Initialization

    def __init__(self):

        # Creating the attributes, all private

        self.__manufact = "Nokia"
        self.__model = "Nokia 3310"
        self.__retail_price = "250"

    # functions for setting the manufacturer, model and retail price

    def set_manufact(self):
        self.__manufact = input("Enter the manufacturer: ")

    def set_model(self):
        self.__model = input("Enter the model: ")

    def set_retailprice(self):
        self.__retail_price = float(input("Enter the retail price: "))

    # functions for getting and returning the manufacturer, model and retail price

    def get_manufact(self):
        return self.__manufact

    def get_model(self):
        return self.__model

    def get_retailprice(self):
        return self.__retail_price

# Main function

def main():

    # creating a new object

    new_phone = CellPhone()

    # calling the class functions to change the cellphone info

    new_phone.set_manufact()
    new_phone.set_model()
    new_phone.set_retailprice()

    # Printing out the new data

    print(new_phone)

# Calling the main function

main()