# File: main.py
# Author: Alex Porri
# Description: Functions that asks for 10 items to be added to a list + randomly listed numbers

import random
LIST_OF_RANDOM_NUMBERS = []
LIST_OF_INTEGERS = []
LIST_OF_STRINGS = []

#Function that appends 10 user inputted integers into a list

def interger_listing_function():
    LOOPCOUNT = 10
    while LOOPCOUNT > 0:
        INTEGER = int(input("Add an integer, " + str(LOOPCOUNT) + " left: "))
        LIST_OF_INTEGERS.append(INTEGER)
        LOOPCOUNT -= 1

#Function that appends 10 user inputted strings into a list

def string_listing_function():
    LOOPCOUNT = 10
    while LOOPCOUNT > 0:
        STRING = input("Add something to the list, " + str(LOOPCOUNT) + " left: ")
        LIST_OF_STRINGS.append(STRING)
        LOOPCOUNT -= 1

#Function that adds 10 random numbers to a list

def random_interger_listing():
    LOOPCOUNT = 10
    while LOOPCOUNT > 0:
        NUMBER = random.random()
        LIST_OF_RANDOM_NUMBERS.append(NUMBER)
        LOOPCOUNT -= 1

interger_listing_function()
string_listing_function()
random_interger_listing()

print(LIST_OF_INTEGERS, LIST_OF_STRINGS, LIST_OF_RANDOM_NUMBERS, sep="\n")