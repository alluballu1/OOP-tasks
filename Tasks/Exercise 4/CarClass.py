# File name: CarClass.py
# Author: Alex Porri
# Description: A car class

class Car:

    def __init__(self, init_manufact, init_model, init_mileage, init_price, init_color, init_max_load, init_trunksize):
        self.__manufact = init_manufact
        self.__model = init_model
        self.__mileage = init_mileage
        self.__price = init_price
        self.__color = init_color
        self.__max_load = init_max_load
        self.__trunk_size = init_trunksize

    # Creating accessor functions for each attribute

    def get_manufact(self):
        return self.__manufact

    def get_model(self):
        return self.__model

    def get_mileage(self):
        return self.__mileage

    def get_price(self):
        return self.__price

    def get_color(self):
        return self.__color

    def get_max_load(self):
        return self.__max_load

    def get_trunk_size(self):
        return self.__trunk_size

    # Creating mutator functions for each attribute

    def set_manufact(self):
        self.__manufact = input("Set new manufacturer: ")

    def set_model(self):
        self.__model = input("Set new model: ")

    def set_mileage(self):
        self.__mileage = float(input("Set new mileage"))

    def set_price(self):
        self.__price = float(input("Set new price: "))

    def set_color(self):
        self.__color = input("Set new color: ")

    def set_max_load(self):
        self.__max_load = float(input("Set new max load: "))

    def set_trunk_size(self):
        self.__trunk_size = float(input("Set new trunk size: "))

    # Creating the __str__ method

    def __str__(self):
        return f"""The information of the car you provided are such:
Manufacturer: {self.__manufact}
Model: {self.__model}
Mileage: {str(self.__mileage)}
Price: {str(self.__price)}
Color: {self.__color}
Max load: {str(self.__max_load)}
Trunk size: {str(self.__trunk_size)}"""
