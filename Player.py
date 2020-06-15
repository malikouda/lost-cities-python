from Stack import Stack

class Player():
    def __init__(self, name, column_names):
        self.name = name
        self.hand = []
        self.columns = {k: Stack() for k in column_names}
        self.score = 0

    def __repr__(self):
        return "Player: " + self.name + "\nHand: " + str(self.hand) + "\nColumns: " + str(self.columns)