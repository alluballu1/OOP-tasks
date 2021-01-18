

# File name: Exercise2task5.py
# Author: Alex Porri
# Description: Calculate the average of 5 student's grades.

LIST_OF_NAMES = []
LIST_OF_GRADES = []

def average_calculator():

    # Not needed, helps tracking how many inputs there are

    LOOPCOUNT = 1
    while len(LIST_OF_GRADES) < 5:
        NEW_STUDENT_NAME = input(str(LOOPCOUNT) + ". Input student's name: ")
        NEW_STUDENT_GRADE = int(input(str(LOOPCOUNT) + ". Input studen's grade: "))

        # Just for a better visualization on the console line.
        print("=======================================")
        LIST_OF_NAMES.append(NEW_STUDENT_NAME)
        LIST_OF_GRADES.append(NEW_STUDENT_GRADE)
        LOOPCOUNT += 1


    return sum(LIST_OF_GRADES)/len(LIST_OF_GRADES)

print(average_calculator())

