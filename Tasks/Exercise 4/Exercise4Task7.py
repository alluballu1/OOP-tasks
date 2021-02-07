# File name: Exercise4Task7.py
# Author: Alex Porri
# Description: Testing the car class


import CarClass as Car

# Creating the car object
my_car = Car.Car("Opel", "Cadet", 100000, 35000, "Red", 1500, 50)

# Test printing the default values
print(my_car)

# Testing the mutator functions
my_car.set_manufact()
my_car.set_model()

# Printing the object with changed values
print(my_car)

