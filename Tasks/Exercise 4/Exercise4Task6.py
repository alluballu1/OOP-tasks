# File Name: Exercise4Task6.py
# Author: Alex Porri
# Description: using two imported classes. Dice is used to roll a number and then printing out the info of the device
# with the same ID as the rolled value

import DiceClass as Dice
import CellPhoneClass as CellPhone


# Creating dice object
my_dice = Dice.Dice()

# Rolling the dice
my_dice.roll_dice()

# Creating 3 objects with set data, all unique
first_phone = CellPhone.CellPhone("Nokia", "3310", 100)
second_phone = CellPhone.CellPhone("Apple", "iPhone", 1500)
third_phone = CellPhone.CellPhone("OnePlus", "Nord", 300)

# Creating a list of the objects for the main function "for-loop"

list_of_devices = (first_phone, second_phone, third_phone)

# Calling the main function

def main():

    print("Rolled dice value is: " + str(my_dice.get_side_up()))
    for device in list_of_devices:
        if device.get_id() == my_dice.get_side_up():
            print(device)
            exit()
    print("No match.")


main()

