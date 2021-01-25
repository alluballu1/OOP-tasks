# File name: Exercise3Task3.py
# Author: Alex Porri
# Description: Coin class (for flipping), added a method (function) for changing the coin type

import random


class coin:
    # The __init__ method initializes the sideup data attribute with "heads"

    def __init__(self):
        self.SIDEUP = "Untossed: Heads"
        self.typeof_coin = "Euro"

    # The toss method generate a random number
    # int the range of 0 to 1. If the number
    # 0 = "heads", otherwise "tails"

    def coin_type(self):
        global list_of_coins
        list_of_coins = ("Euro", "Pound", "Dollar", "Ruble", "Yen")
        self.typeof_coin = list_of_coins[random.randint(0, 4)]

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
    # returns the coin's currency type

    def get_cointype(self):
        return self.typeof_coin


# The main function

def main():
    # Create an object from the coin class

    MY_COIN = coin()
    print("Currency BEFORE changing it: " + MY_COIN.get_cointype())

    # Calls the coin's currency conversion function
    MY_COIN.coin_type()


    # Toss the coin
    print("Tossing the coin...")
    MY_COIN.toss()

    # Display the side

    print("Landed on: "+MY_COIN.get_sideup(), "Type of coin AFTER tossing: "+MY_COIN.get_cointype(), sep="\n")


main()
