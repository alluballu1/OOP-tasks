# File name: Exercise3Task2.py
# Author: Alex Porri
# Description: Coin class (for flipping), added a randomly picked currency for the coin

import random


class coin:
    # The __init__ method initializes the sideup data attribute with "heads"

    def __init__(self):

        # list of coin types to be picked for the used currency

        list_of_coins = ("Euro", "Pound", "Dollar", "Ruble", "Yen")
        self.SIDEUP = "Untossed: Heads"

        # the coin's currency picked at random
        self.currency = list_of_coins[random.randint(0, 4)]

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

    # returns the coins currency type

    def get_currency(self):
        return self.currency


# The main function

def main():
    # Create an object from the coin class

    MY_COIN = coin()
    # Toss the coin
    print("Tossing the coin...")
    MY_COIN.toss()

    # Display the side

    print("Landed on: " + MY_COIN.get_sideup(), "Type of coin: " + MY_COIN.get_currency(), sep="\n")


main()
