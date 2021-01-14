# File: Exercise1Task8.py
# Author: Alex Porri
# Description: A game of rock-paper-scissors

import random

# global point variables
PLAYER_WIN_COUNT = 0
CPU_WIN_COUNT = 0
DICTIONARY = {1:"Rock", 2:"Paper", 3:"Scissors" }

# Game function, using Else-If gives points depending on who wins the round, calculates total points and
# stops function call when either the player or computer wins.

def rock_paper_scissors():
    global PLAYER_WIN_COUNT
    global CPU_WIN_COUNT
    if CPU_WIN_COUNT == 3:
        print("CPU wins!")
        exit()
    if PLAYER_WIN_COUNT == 3:
        print("You win!")
        exit()
    print("==================================")
    print("You: " + str(PLAYER_WIN_COUNT), "CPU: " + str(CPU_WIN_COUNT), sep="\n")
    print("1) Rock", "2) Paper", "3) Scissors", sep="\n")
    PLAYER_CHOICE = input("Choose: ")
    CPU_CHOICE = random.randint(1,3)
    print("You: " + DICTIONARY[int(PLAYER_CHOICE)], "CPU: " + DICTIONARY[int(CPU_CHOICE)], sep="\n")

    if int(PLAYER_CHOICE) == int(CPU_CHOICE):
        print("Draw")
        rock_paper_scissors()
    if int(PLAYER_CHOICE) == 1 and int(CPU_CHOICE) == 2:
        print("CPU gets a point.")
        CPU_WIN_COUNT += 1
        rock_paper_scissors()
    else:
        print("You get a point.")
        PLAYER_WIN_COUNT += 1
        rock_paper_scissors()
    if int(PLAYER_CHOICE) == 2 and int(CPU_CHOICE) == 3:
        print("CPU gets a point.")
        CPU_WIN_COUNT += 1
        rock_paper_scissors()
    else:
        print("You get a point.")
        PLAYER_WIN_COUNT += 1
        rock_paper_scissors()
    if int(PLAYER_CHOICE) == 3 and int(CPU_CHOICE) == 1:
        print("CPU gets a point.")
        CPU_WIN_COUNT += 1
        rock_paper_scissors()
    else:
        print("You get a point.")
        PLAYER_WIN_COUNT += 1
        rock_paper_scissors()

rock_paper_scissors()