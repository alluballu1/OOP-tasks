# File name: Exercise5Task6.py
# Author: Alex Porri
# Description: Creating a list of objects and a dictionary based on the said list that uses the student ID's as keys.

import StudentClass
import MammalClass

# Creating a function that makes and returns a list of objects that consists of students and their pets

def create_list_of_objects():
    list_of_objects = []
    amount_of_objects = int(input("How many students with pets: "))
    for list_object in range(amount_of_objects):
        student_first_name = input("Student first name: ")
        student_last_name = input("Student last name: ")
        student_pet_name = input("Student's pet's name: ")
        student_pet_species = input("Student's pet's species: ")
        student_pet_weight = float(input("Student's pet's weight: "))
        student_pet_width = float(input("Student's pet's width: "))
        student_pet_height = float(input("Student's pet's height: "))
        student_pet_length = float(input("Student's pet's length: "))
        new_student = StudentClass.Student(student_first_name, student_last_name, list_object)

        #init_species, init_name, init_width, init_height, init_length, init_weight
        new_pet = MammalClass.Mammal(student_pet_species, student_pet_name, student_pet_width, student_pet_height,
                                     student_pet_length, student_pet_weight)
        list_of_objects.append([new_student, new_pet])
    return list_of_objects

# Creating a function that makes and returns the dictionary and the keys for it based on the student ID

def create_dictionary(list):
    dictionary = {}

    for each in list:
        key = each[0].get_student_id()
        dictionary[key] = each

    return dictionary


# Creating a function that prints out all the students and their pets from a dictionary
def dictionary_search_function(dictionary, object_list):

    for each in object_list:
        print()
        print(dictionary[each[0].get_student_id()][0],
              dictionary[each[0].get_student_id()][1], sep="\n")
        print()


# Creating the main function that calls all of the previous functions.


def main():
    list_of_students_and_pets = create_list_of_objects()
    pet_dictionary = create_dictionary(list_of_students_and_pets)
    dictionary_search_function(pet_dictionary, list_of_students_and_pets)


#Calling the main function

main()