# File name: exercise8task1.py
# Author: Alex Porri
# Description: Multiple functions for cleaning the house and preparing for the quarantine.

from HouseClass import House


# Function for cleaning floors and dusting surfaces

def clean_floor(house):
    if house.get_floors() > 0:
        print("cleaning floors..")
    while house.get_floors() > 0:
        house.set_floors()
    if house.get_surfaces() > 0:
        print("dusting surfaces..  ")
    while house.get_surfaces() > 0:
        house.set_surfaces()
    if house.get_floors() == 0 and house.get_surfaces() == 0:
        print("All floors are vacuumed and all surfaces dusted.")

# Function for making the bed(s) and washing the windows

def make_bed_wash_windows(house):
    if house.get_bed() > 0:
        print("making bed(s)..")
    while house.get_bed() > 0:
        house.set_bed()
    if house.get_windows() > 0:
        print("washing windows..")
    while house.get_windows() > 0:
        house.set_windows()
    if house.get_windows() == 0 and house.get_bed() == 0:
        print("All beds are made and windows washed.")

# function for grocery and TP shopping

def shopping(house):
    if house.get_fridge() > 0:
        print("buying groceries..")
    while house.get_fridge() > 0:
        house.set_fridge()
    print("buying toilet paper..")
    for each in range(10):
        house.set_toilet_paper()

# main function

def main():
    house = House(5, 10,1, 4,1,1)
    print("State of the house before cleaning:",house, " ", sep="\n")
    print("Starting the quarantine preparations by making beds and washing windows.")
    make_bed_wash_windows(house)
    print("Continuing with vacuuming floors and dusting surfaces.")
    clean_floor(house)
    print("Going for some shopping in preparation.")
    shopping(house)
    print("Just in case the quarantine lasts longer than expected, need to hoard some toilet paper.")
    for each in range(5):
        shopping(house)
    print(" ","State of house after cleaning",house, sep="\n")


main()

