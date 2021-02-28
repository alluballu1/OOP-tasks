# File name: exercise6task5.py
# Author: Alex Porri
# Description: Create two mammals using a child class, domesticated and a wild one


import MammalClass


def main():
    domestic_animal = MammalClass.DomesticAnimal("Dog", "Kake", 0.2, 0.5, 0.6, 10, "Barks and yaps", "Dog food",
                                                 "Squeaky ball")

    wild_animal = MammalClass.WildAnimal("Wolf", "Fang", 0.8, 1, 1.5, 60, "Howls and Barks", "Deer and Rabbits",
                                         "Mountains")

    print("First the domestic animal:", domestic_animal, " ", "Now the wild animal: ", " ", wild_animal, sep="\n")


main()
