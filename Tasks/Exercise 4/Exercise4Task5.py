# File name: Exercise4Task5.py
# Author: Alex Porri
# Description: Main function using an imported phone class. Multiple objects with changed info via mutators

import CellPhoneClass as CellPhone

# Main function

def main():

    # creating new objects with all initial data being the same

    first_phone = CellPhone.CellPhone("Nokia", "3310", 100)
    second_phone = CellPhone.CellPhone("Nokia", "3310", 100)
    third_phone = CellPhone.CellPhone("Nokia", "3310", 100)

    # Changing the second phone data via mutators
    print("Changing the second phone's info: ")
    second_phone.set_manufact()
    second_phone.set_model()
    second_phone.set_retailprice()

    # Changing the third phone data via mutators
    print("Changing the third phone's info: ")
    third_phone.set_manufact()
    third_phone.set_model()
    third_phone.set_retailprice()


    # Printing out the new data

    print("Firs device:",first_phone, "Second device:", second_phone,"Third device", third_phone, sep="\n")

# Calling the main function

main()