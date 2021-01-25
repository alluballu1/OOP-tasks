# File name: Exercise3Task8.py
# Author: Alex Porri
# Description: Phone class with user input

# Creating the class

class CellPhone:

    # Initialization

    def __init__(self):

        # Creating the attributes, all private

        self.__Manufact = "Nokia"
        self.__Model = "Nokia 3310"
        self.__RetailPrice = "250"

    # functions for setting the manufacturer, model and retail price

    def set_manufact(self):
        self.__Manufact = input("Enter the manufacturer: ")

    def set_model(self):
        self.__Model = input("Enter the model: ")

    def set_retailprice(self):
        self.__RetailPrice = float(input("Enter the retail price: "))

    # functions for getting and returning the manufacturer, model and retail price

    def get_manufact(self):
        return self.__Manufact

    def get_model(self):
        return self.__Model

    def get_retailprice(self):
        return self.__RetailPrice

# Main function

def main():

    # creating a new object

    new_phone = CellPhone()

    # calling the class functions to change the cellphone info

    new_phone.set_manufact()
    new_phone.set_model()
    new_phone.set_retailprice()

    # Printing out the new data

    print("Here is the data that you provided: ", "Manufacturer: " + new_phone.get_manufact(),
          "Model number: " + new_phone.get_model(), "Retail price: " + str(new_phone.get_retailprice()), sep="\n")

# Calling the main function

main()