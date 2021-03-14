# File name: HouseClass.py
# Author: Alex Porri
# Description: a class for a house

# creating the class
class House:

    def __init__(self, floors, windows, bed, surfaces, fridge, toilet_paper):
        self.__floors = floors
        self.__windows = windows
        self.__bed = bed
        self.__surfaces = surfaces
        self.__fridge = fridge
        self.__toilet_paper = toilet_paper

    # creating the fetching functions

    def get_floors(self):
        return self.__floors

    def get_windows(self):
        return self.__windows

    def get_bed(self):
        return self.__bed

    def get_surfaces(self):
        return self.__surfaces

    def get_fridge(self):
        return self.__fridge

    def get_toilet_paper(self):
        return self.__toilet_paper

    # Creating the mutator functions

    def set_floors(self):
        self.__floors = self.__floors - 1

    def set_windows(self):
        self.__windows = self.__windows -1

    def set_bed(self):
        self.__bed = self.__bed - 1

    def set_surfaces(self):
        self.__surfaces = self.__surfaces - 1

    def set_fridge(self):
        self.__fridge = self.__fridge -1

    def set_toilet_paper(self):
        self.__toilet_paper = self.__toilet_paper + 1

    # Creating a str function

    def __str__(self):
        return f"Amount of dirty floors: {self.__floors}" \
               f"\nAmount of dirty windows: {self.__windows}" \
               f"\nAmount of unmade beds: {self.__bed}" \
               f"\nAmount of dirty surfaces: {self.__surfaces}" \
               f"\nAmount of empty fridges: {self.__fridge}" \
               f"\nAmount of toilet paper: {self.__toilet_paper}"



