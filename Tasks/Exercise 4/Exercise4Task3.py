# File name: Exercise4Task3.py
# Author: Alex Porri
# Description: Main function using an imported phone class


import CellPhoneClass as CellPhone

# Main function

def main():

    # creating a new object

    new_phone = CellPhone.CellPhone("2323", "sdfsdf", 100)

    # calling the class functions to change the cellphone info

    new_phone.set_manufact()
    new_phone.set_model()
    new_phone.set_retailprice()

    # Printing out the new data

    print(new_phone)

# Calling the main function

main()
