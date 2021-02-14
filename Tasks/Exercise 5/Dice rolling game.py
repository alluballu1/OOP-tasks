# File: Dice rolling game.py
# Author: Alex Porri
# Description: Demonstrating objects as attributes (return values and objects as a list)

import DiceClass

def roll_one_dice(demo_dice):
    demo_dice.roll_dice()
    return demo_dice

def make_list():
    dice_list = []

    for number in range(1,4):
        print("Dice num: ", number)
        my_dice = DiceClass.Dice()
        dice_list.append(my_dice)
    return dice_list

def main():
    for x in make_list():
        print(x.get_color(), x)
        x.roll_dice()
        print(x, "rolled")
    my_dice = DiceClass.Dice()
    roll_one_dice(my_dice)
    print(my_dice.get_color(), my_dice.get_side_up())
    my_dice = roll_one_dice(my_dice)
    print(my_dice.get_color(), my_dice.get_side_up())

main()