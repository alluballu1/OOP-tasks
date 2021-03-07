# File name: exercise7task6.py
# Author: Alex Porri
# Description: A quiz that asks 10 different countries' capitals and gives out a score

import random

def create_dictionary():

    dictionary = {}

    with open("dict.txt") as file:
        for line in file:
            (key, value) = line.split()
            dictionary[key] = value

    return dictionary


def get_quiz_numbers(dictionary):
    all_numbers = []

    for each in range(len(dictionary)):
        all_numbers.append(each)
    quiz_numbers = random.sample(all_numbers, 10)

    return quiz_numbers

def quiz(dictionary, numbers):
    score = 0
    for each in numbers:
        print("")
        answer = input("What is the capital of " + list(dictionary.keys())[each] + "?: ")
        if answer == list(dictionary.values())[each]:
            score += 1
            print("Correct!")
        else:
            print("Incorrect! The right answer was: " + list(dictionary.values())[each])
    return score


def main():
    dictionary = create_dictionary()
    quiz_numbers = get_quiz_numbers(dictionary)
    score = quiz(dictionary, quiz_numbers)
    print("Your total score was: " + str(score))

main()