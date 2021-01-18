# File: Exercise1Task4.py
# Author: Alex Porri
"""Description: Looping function that takes in integers, adds them to a list and prints out negative numbers of negative
integers"""

LIST_OF_NUMBERS = []

# Function that loops itself if the inputted value is an integer and isn't 0

def number_reading_function():
    NUMBER = input("Input an integer: ")
    if int(NUMBER) == 0:
        print(LIST_OF_NUMBERS)
    else:
        if int(NUMBER) < 0:
            print(NUMBER[1::])
        LIST_OF_NUMBERS.append(NUMBER)
        number_reading_function()

number_reading_function()
