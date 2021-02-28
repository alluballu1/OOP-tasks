# File name: exercise6task8.py
# Author: Alex Porri
# Description: Student and teacher class objects with two animals each, all printed out.

import MammalClass
import OOPClass

# Create a main function that has the student + teacher class objects in addition to the 4 animals (2 for each)
# Added the teacher, students and the animals into a dictionary then printed them out

def main():
    student = OOPClass.Student("Alex", "Porri", 1803335, 3)
    teacher = OOPClass.Teacher("Hugh", "Jackson", 10, "Math")

    student_domestic_animal = MammalClass.DomesticAnimal("Dog", "Kake", 0.2, 0.5, 0.6, 10, "Barks", "Dog food",
                                                         "Ball")
    student_wild_animal = MammalClass.WildAnimal("Wolf", "Fang", 0.8, 1, 1.5, 60, "Howls", "Deer", "Mountains")

    teacher_domestic_animal = MammalClass.DomesticAnimal("Cat", "", 0.2, 0.5, 0.6, 3, "Meows", "Cat food",
                                                         "shoebox")
    teacher_wild_animal = MammalClass.WildAnimal("Deer", "Bambi", 0.8, 1, 1.5, 60, "Yaps", "Deer", "Forests")

    dictionary = {student: [student_wild_animal, student_domestic_animal],
                  teacher: [teacher_wild_animal, teacher_domestic_animal]}

    for x in dictionary:
        print("=====================================")
        print(x, "", dictionary[x][0], "", dictionary[x][1], sep="\n")

main()
