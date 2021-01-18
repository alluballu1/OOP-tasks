# File: Exercise1Task6.py
# Author: Alex Porri
"""Description: Looping function that takes in integers, adds them to a list and prints out negative numbers of negative
integers, in addition it calculates the amount of even integers and the sum of numbers that can be divided by 3"""

AMOUNT_OF_EVEN_INTEGERS = 0
SUM_OF_NUMBERS_DIVISIBLE_BY_THREE = 0
LIST_OF_NUMBERS = []


# Function that loops itself if the inputted value is an integer and isn't 0, calculates the amount of even
# integers, calculates the sum of numbers that are divisible by 3

def number_reading_function():
    global AMOUNT_OF_EVEN_INTEGERS
    global SUM_OF_NUMBERS_DIVISIBLE_BY_THREE
    NUMBER = input("Input an integer: ")
    if int(NUMBER) == 0:
        print(LIST_OF_NUMBERS)
        print(AMOUNT_OF_EVEN_INTEGERS)
        print(SUM_OF_NUMBERS_DIVISIBLE_BY_THREE)
    else:
        if int(NUMBER) < 0:
            print(NUMBER[1::])
        if int(NUMBER) % 2 == 0:
            AMOUNT_OF_EVEN_INTEGERS += 1
        if int(NUMBER) % 3 == 0:
            SUM_OF_NUMBERS_DIVISIBLE_BY_THREE += int(NUMBER)
        LIST_OF_NUMBERS.append(NUMBER)
        number_reading_function()


number_reading_function()
