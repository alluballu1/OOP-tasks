

# File name: exercise2task3.py
# Author: Alex Porri
# Description: Function that takes the amount of accepted exercises and outputs a grade

def grading_function():

    # User inputs the amount of accepted exercises.

    ACCEPTED_EXERCISES = int(input("Input the amount of accepted exercises: "))

    if ACCEPTED_EXERCISES < 9:
        return "Failed"
    elif ACCEPTED_EXERCISES >= 9 and ACCEPTED_EXERCISES < 10:
        return 1
    elif ACCEPTED_EXERCISES >= 10 and ACCEPTED_EXERCISES < 11:
        return 2
    elif ACCEPTED_EXERCISES >= 11 and ACCEPTED_EXERCISES < 12:
        return 3
    elif ACCEPTED_EXERCISES >= 12 and ACCEPTED_EXERCISES < 13:
        return 4
    else:
        return 5

# Prints out the returned value

print(grading_function())
