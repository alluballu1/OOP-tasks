# File: Exercise1Task7.py
# Author: Alex Porri
# Description: Count the sum and the squared sum of a arithmetic progression

import math

# Function that handles the user input of the maximum value, wanted calculation and printing of the sums

def sum_of_arithmetic_progression():
    MAXIMUM_VALUE = input("Add a maximum value for the arithmetic progression: ")
    LIST_OF_NUMBERS = [0]
    NEXT_NUMBER = 0
    SUM_OF_NUMBERS = 0
    SQUARED_SUM_OF_NUMBERS = 0
    while int(LIST_OF_NUMBERS[(len(LIST_OF_NUMBERS)-1)]) < int(MAXIMUM_VALUE):
        NEXT_NUMBER += 2
        LIST_OF_NUMBERS.append(NEXT_NUMBER)
    for EACH in LIST_OF_NUMBERS:
        SUM_OF_NUMBERS += EACH
        SQUARED_SUM_OF_NUMBERS += math.sqrt(EACH)
    print(SUM_OF_NUMBERS, SQUARED_SUM_OF_NUMBERS, sep="\n")

sum_of_arithmetic_progression()