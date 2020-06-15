from Deck import Deck
from Player import Player
from Board import Board

def main():
    values = [1] * 3 + list(range(2,11))
    colors = ['y', 'w', 'b', 'g', 'r']

    deck = setup_deck(values, colors)

    print()
    print(deck)

    player1 = Player("Player 1", colors)
    player2 = Player("Player 2", colors)

    print()
    print(player1)
    print(player2)
    
    deck.deal(player1, 8)
    deck.deal(player2, 8)

    print()
    print(deck)
    print(deck.count())
    print(player1)
    print(player2)


def setup_deck(values, colors):
    deck = Deck(values, colors)
    deck.shuffle()

    return deck

main()