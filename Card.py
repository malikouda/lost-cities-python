class Card():
    def __init__(self, value: int, color: str):
        self.color = color
        self.value = value
    
    def __repr__(self):
        return (str(self.value) + self.color)

    def __eq__(self, other):
        return self.color == other.color and self.value == other.value

    def __lt__(self, other):
        return self.value < other.value