
# File name: Exercise2Task7.py
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
            if random.randint(0,1) == 0:
                self.SIDEUP = "Heads"
            else:
                self.SIDEUP = "Tails"

    # the get_sideup method returns the value referenced by sideup.

        def get_sideup(self):
            return self.SIDEUP

# The main function

def main():

    #Create an object from the coin class

    MY_COIN = coin()
    print(MY_COIN.get_sideup())
    #Toss the coin
    print("Tossing the coin...")
    MY_COIN.toss()

    #Display the side

    print(MY_COIN.get_sideup())

main()