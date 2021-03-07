# File name: exercise7task4.py
# Author: Alex Porri
# Description: Game of cards where 3 players pull from a deck and the highest value wins.
import DeckClass

# Creating the objects

deck = DeckClass.Deck()
deck.shuffle()
card = deck.drawCard()
card2 = deck.drawCard()
card3 = deck.drawCard()

# Main function

def main(deck,first, second, third ):
    print("Players 1 to 3 in order drew:")
    first.show()
    second.show()
    third.show()

    if first == second == third:
        print("TIED, drawing again")
        first = deck.drawCard()
        second = deck.drawCard()
        third = deck.drawCard()
        main(deck, first, second, third)

    if first.value > second.value and first.value > third.value:
        print("Player 1 won!")
    if second.value > first.value and second.value > third.value:
        print("Player 2 won!")
    if third.value > first.value and third.value > second.value:
        print("Player 3 won!")

# Calling the main function

main(deck,card,card2,card3)