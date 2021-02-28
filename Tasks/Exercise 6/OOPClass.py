# File name: OOPClass.py
# Author: Alex Porri
# Description: OOP class

# Creating the OOP class
class OOP:

    # Creating the initialization function and it's attributes
    def __init__(self, init_first_name, init_last_name):
        self.__first_name = init_first_name
        self.__last_name = init_last_name

    # Creating the get functions for returning wanted values
    def get_first_name(self):
        return self.__first_name

    def get_last_name(self):
        return self.__last_name

    # Creating the mutator functions to changes wanted values
    def set_first_name(self):
        new_first_name = input("New first name: ")
        self.__first_name = new_first_name

    def set_last_name(self):
        new_last_name = input("New last name: ")
        self.__last_name = new_last_name

    # Creating the string function for returning the object info when printed out
    def __str__(self):
        return "The OOP class participant's information is such: " + \
               "\nFirst name: " + format(self.__first_name) + \
               "\nLast name: " + format(self.__last_name)


# Creating the student class
class Student(OOP):

    # Creating the initialization function and it's attributes
    def __init__(self, init_first_name, init_last_name, init_student_id, init_student_year):
        super().__init__(init_first_name, init_last_name)
        self.__student_id = init_student_id
        self.__student_year = init_student_year

    # Creating the get functions for returning wanted values

    def get_student_id(self):
        return self.__student_id

    def get_student_year(self):
        return self.__student_year

    # Creating the mutator functions to changes wanted values

    def set_student_id(self):
        new_student_id = int(input("New student ID: "))
        self.__student_id = new_student_id

    def set_student_year(self):
        new_student_year = int(input("New student year: "))
        self.__student_year = new_student_year

    # Creating the string function for returning the object info when printed out
    def __str__(self):
        return "The student's information is such: " + \
               "\nFirst name: " + format(self.get_first_name()) + \
               "\nLast name: " + format(self.get_last_name()) + \
               "\nStudent ID: " + format(self.__student_id) + \
               "\nStudent's year: " + format(self.__student_year)

# Creating the teacher class
class Teacher(OOP):

    # Creating the initialization function and it's attributes
    def __init__(self, init_first_name, init_last_name, init_years_taught, init_taught_subjects):
        super().__init__(init_first_name, init_last_name)
        self.__years_taught = init_years_taught
        self.__taught_subjects = init_taught_subjects

    # Creating the get functions for returning wanted values

    def get_years_taught(self):
        return self.__years_taught

    def get_taught_subjects(self):
        return self.__taught_subjects

    # Creating the mutator functions to changes wanted values

    def set_student_id(self):
        years_taught = int(input("Years taught: "))
        self.__years_taught = years_taught

    def set_student_id(self):
        taught_subjects = input("Taught subjects: ")
        self.__taught_subjects = taught_subjects

    # Creating the string function for returning the object info when printed out
    def __str__(self):
        return "The teacher's information is such: " + \
               "\nFirst name: " + format(self.get_first_name()) + \
               "\nLast name: " + format(self.get_last_name()) + \
               "\nYears taught: " + format(self.__years_taught) + \
               "\nTaught subjects: " + format(self.__taught_subjects)

