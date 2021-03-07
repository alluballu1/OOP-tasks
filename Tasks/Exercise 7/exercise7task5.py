# File name: exercise7task5.py
# Author: Alex Porri
# Description: Function to test out the student class + removing/adding/printing out their pets.

from StudentClass import Student


def main():
    my_student = Student("Alex", "Porri", 10)
    print(my_student)
    for each in range(3):
        my_student.add_pets()
    my_student.print_pets()
    my_student.remove_pet()
    my_student.print_pets()

main()

