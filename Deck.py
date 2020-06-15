from Card import Card
from Player import Player
import random

class Deck():
    def __init__(self, values, colors):
        self.contents = [Card(value, color) for color in colors for value in values]
        self.contents.sort()

    def __repr__(self):
        return str(self.contents)
    
    def count(self):
        return len(self.contents)

    def shuffle(self):
        random.shuffle(self.contents)

    def deal(self, player, number_of_cards):
        player.hand.append(self.contents[-number_of_cards:])
        del self.contents[-number_of_cards:]
    
    def deal_one(self, player):
        player.hand.append(self.contents.pop())