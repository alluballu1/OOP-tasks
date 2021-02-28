#File name: exercise6task7.py
#Author: Alex Porri
#Description: Create and print out student and teacher class objects

import OOPClass


# Create main function that has the student and teacher objects
def main():
    student = OOPClass.Student("Alex", "Porri", 1803335, 3)
    teacher = OOPClass.Teacher("Hugh", "Jackson", 10, "Math")
    print(student, " ", teacher, sep="\n")

main()
