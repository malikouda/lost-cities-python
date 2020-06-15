from Stack import Stack

class Board():
    def __init__(self, column_names):
        self.discards = {k: Stack() for k in column_names}

    def __repr__(self):
        return str(self.discards)