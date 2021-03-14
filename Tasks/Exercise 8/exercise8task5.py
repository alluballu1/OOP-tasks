# File name: exercise8task5.py
# Author: Alex Porri
# Description: A quiz that asks 10 different countries' capitals and gives out a score with an option to quiz countries
# based on capitals as well.

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

def capital_quiz(dictionary, numbers):
    score = 0
    for each in numbers:
        print("")
        answer = input("What country's capital is: " + list(dictionary.values())[each] + "?: ")
        if answer == list(dictionary.keys())[each]:
            score += 1
            print("Correct!")
        else:
            print("Incorrect! The right answer was: " + list(dictionary.keys())[each])
    return score


def main():
    dictionary = create_dictionary()
    quiz_numbers = get_quiz_numbers(dictionary)
    capitals_or_countries = input("Do you want to play a quiz asking the countries or capitals?: ")
    if capitals_or_countries == "capitals":
        score = quiz(dictionary, quiz_numbers)
        print("Your total score was: " + str(score))
    elif capitals_or_countries == "countries":
        score = capital_quiz(dictionary, quiz_numbers)
        print("Your total score was: " + str(score))
    elif capitals_or_countries == "no" or "No":
        print("Okay.")
    else:
        main()


main()


