# File name: Exercise3Task4.py
# Author: Alex Porri
# Description: Coin class (for flipping), SIDEUP attribute made private and trying to change it from the main
# function

import random


class coin:
    # The __init__ method initializes the sideup data attribute with "heads"

    def __init__(self):
        self.__SIDEUP = "Untossed: Heads"
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
            self.__SIDEUP = "Heads"
        elif TOSS_VALUE == 1:
            self.__SIDEUP = "Tails"
        elif TOSS_VALUE == 2:
            self.__SIDEUP = "It landed on it's side!"
        else:
            self.__SIDEUP = "Uhh... I think it fell into a rabbit hole. Somehow."

    # the get_sideup method returns the value referenced by sideup.

    def get_sideup(self):
        return self.__SIDEUP
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

    #Trying to change the coin's side from the main function
    MY_COIN.SIDEUP = "Testing!"

    # Display the side

    print("Landed on: "+MY_COIN.get_sideup(), "Type of coin AFTER tossing: "+MY_COIN.get_cointype(), sep="\n")


main()
