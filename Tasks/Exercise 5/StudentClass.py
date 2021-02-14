# File name: StudentClass.py
# Author: Alex Porri
# Description: Player class


# Creating the student class
class Student:

    # Creating the initialization function and it's attributes
    def __init__(self, init_first_name, init_last_name, init_student_id):
        self.__first_name = init_first_name
        self.__last_name = init_last_name
        self.__student_id = init_student_id

    # Creating the get functions for returning wanted values
    def get_first_name(self):
        return self.__first_name

    def get_last_name(self):
        return self.__last_name

    def get_student_id(self):
        return self.__student_id

    # Creating the mutator functions to changes wanted values
    def set_first_name(self):
        new_first_name = input("New first name: ")
        self.__first_name = new_first_name

    def set_last_name(self):
        new_last_name = input("New last name: ")
        self.__last_name = new_last_name

    def set_student_id(self):
        new_student_id = input("New first name: ")
        self.__student_id = new_student_id

    # Creating the string function for returning the object info when printed out
    def __str__(self):
        return "The student's information is such: " + \
               "\nFirst name: " + format(self.__first_name) + \
               "\nLast name: " + format(self.__last_name) + \
               "\nStudent ID: " + format(self.__student_id)
