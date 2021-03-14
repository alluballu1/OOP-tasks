# File name: CookieClass.py
# Author: Alex Porri
# Description: A class for a single cookie.

class Cookie:
    def __init__(self, flavor):

        self.__frosting = None
        self.__flavor = flavor

    # Creating the fetching functions

    def get_frosting(self):
        return self.__frosting

    def get_flavor(self):
        return self.__flavor

    # Creating the mutator for the frosting.

    def set_frosting(self, frosting):
        self.__frosting = frosting



