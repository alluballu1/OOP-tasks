# File: Exercise1Task5.py
# Author: Alex Porri
"""Description: Looping function that takes in integers, adds them to a list and prints out negative numbers of negative
integers, in addition it calculates the amount of even integers"""

AMOUNT_OF_EVEN_INTEGERS = 0
LIST_OF_NUMBERS = []

# Function that loops itself if the inputted value is an integer and isn't 0, calculates the amount of even
# integers

def number_reading_function():
    global AMOUNT_OF_EVEN_INTEGERS
    NUMBER = input("Input an integer: ")
    if int(NUMBER) == 0:
        print(LIST_OF_NUMBERS)
        print(AMOUNT_OF_EVEN_INTEGERS)
    else:
        if int(NUMBER) < 0:
            print(NUMBER[1::])
        if (int(NUMBER)%2) == 0:
            AMOUNT_OF_EVEN_INTEGERS+=1
        LIST_OF_NUMBERS.append(NUMBER)
        number_reading_function()

number_reading_function()
