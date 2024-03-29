# File name: Exercise2Task8.py
# Author: Alex Porri
# Description: Coin class (for flipping)

import random


class coin:
    # The __init__ method initializes the sideup data attribute with "heads"

    def __init__(self):

        self.SIDEUP = "Untossed: Heads"

    # The toss method generate a random number
    # int the range of 0 to 1. If the number
    # 0 = "heads", otherwise "tails"

    def toss(self):
        TOSS_VALUE = random.randint(0, 3)
        if TOSS_VALUE == 0:
            self.SIDEUP = "Heads"
        elif TOSS_VALUE == 1:
            self.SIDEUP = "Tails"
        elif TOSS_VALUE == 2:
            self.SIDEUP = "It landed on it's side!"
        else:
            self.SIDEUP = "Uhh... I think it fell into a rabbit hole. Somehow."

    # the get_sideup method returns the value referenced by sideup.

    def get_sideup(self):
        return self.SIDEUP


# The main function

def main():
    # Create an object from the coin class

    MY_COIN = coin()
    # Toss the coin
    print("Tossing the coin...")
    MY_COIN.toss()

    # Display the side

    print("Landed on: " + MY_COIN.get_sideup(), sep="\n")


main()
