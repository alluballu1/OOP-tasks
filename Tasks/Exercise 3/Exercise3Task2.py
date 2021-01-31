# File name: Exercise3Task2.py
# Author: Alex Porri
# Description: Coin class (for flipping), added a randomly picked currency for the coin

import random


class coin:
    # The __init__ method initializes the sideup data attribute with "heads"

    def __init__(self):

        # list of coin types to be picked for the used currency

        LIST_OF_COINS = ("Euro", "Pound", "Dollar", "Ruble", "Yen")
        self.sideup = "Untossed: Heads"

        # the coin's currency picked at random
        self.currency = LIST_OF_COINS[random.randint(0, 4)]

    # The toss method generate a random number
    # int the range of 0 to 1. If the number
    # 0 = "heads", otherwise "tails"

    def toss(self):
        TOSS_VALUE = random.randint(0, 3)
        if TOSS_VALUE == 0:
            self.sideup = "Heads"
        elif TOSS_VALUE == 1:
            self.sideup = "Tails"
        elif TOSS_VALUE == 2:
            self.sideup = "It landed on it's side!"
        else:
            self.sideup = "Uhh... I think it fell into a rabbit hole. Somehow."

    # the get_sideup method returns the value referenced by sideup.

    def get_sideup(self):
        return self.sideup

    # returns the coins currency type

    def get_currency(self):
        return self.currency


# The main function

def main():
    # Create an object from the coin class

    my_coin = coin()
    # Toss the coin
    print("Tossing the coin...")
    my_coin.toss()

    # Display the side

    print("Landed on: " + my_coin.get_sideup(), "Type of coin: " + my_coin.get_currency(), sep="\n")


main()
