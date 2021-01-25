

# File name: exercise2task3.py
# Author: Alex Porri
# Description: Function that takes the amount of accepted exercises and outputs a grade

def grading_function():

    # User inputs the amount of accepted exercises.

    accepted_exercises = int(input("Input the amount of accepted exercises: "))

    if accepted_exercises < 9:
        return "Failed"
    elif accepted_exercises >= 9 and accepted_exercises < 10:
        return 1
    elif accepted_exercises >= 10 and accepted_exercises < 11:
        return 2
    elif accepted_exercises >= 11 and accepted_exercises < 12:
        return 3
    elif accepted_exercises >= 12 and accepted_exercises < 13:
        return 4
    else:
        return 5

# Prints out the returned value

print("Your grade: " + str(grading_function()))
