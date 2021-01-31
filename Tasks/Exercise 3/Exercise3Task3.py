# File name: Exercise3Task3.py
# Author: Alex Porri
# Description: Coin class (for flipping), added a method (function) for changing the coin type

import random


class coin:
    # The __init__ method initializes the sideup data attribute with "heads"

    def __init__(self):
        self.sideup = "Untossed: Heads"
        self.typeof_coin = "Euro"

    # The toss method generate a random number
    # int the range of 0 to 1. If the number
    # 0 = "heads", otherwise "tails"

    def coin_type(self):
        LIST_OF_COINS = ("Euro", "Pound", "Dollar", "Ruble", "Yen")
        self.typeof_coin = LIST_OF_COINS[random.randint(0, 4)]

    def toss(self):
        toss_value = random.randint(0, 3)
        if toss_value == 0:
            self.sideup = "Heads"
        elif toss_value == 1:
            self.sideup = "Tails"
        elif toss_value == 2:
            self.sideup = "It landed on it's side!"
        else:
            self.sideup = "Uhh... I think it fell into a rabbit hole. Somehow."

    # the get_sideup method returns the value referenced by sideup.

    def get_sideup(self):
        return self.sideup
    # returns the coin's currency type

    def get_cointype(self):
        return self.typeof_coin


# The main function

def main():
    # Create an object from the coin class

    my_coin = coin()
    print("Currency BEFORE changing it: " + my_coin.get_cointype())

    # Calls the coin's currency conversion function
    my_coin.coin_type()


    # Toss the coin
    print("Tossing the coin...")
    my_coin.toss()

    # Display the side

    print("Landed on: "+my_coin.get_sideup(), "Type of coin AFTER tossing: "+my_coin.get_cointype(), sep="\n")


main()
