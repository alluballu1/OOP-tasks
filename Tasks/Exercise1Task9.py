# File: Exercise1Task9.py
# Author: Alex Porri
# Description: Function that returns a randomly generated number and then print it separately

# importing the random library
import random

# function that generates a random number between 1 and 6 and then returns it

def random_number_generator():
    RANDOM_NUMBER = random.randint(1,6)
    return RANDOM_NUMBER

print(random_number_generator())