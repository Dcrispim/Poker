class Card:
    def __init__(self, value, suit):
        self.value = str(value).upper()
        self.suit = suit.upper()
        self.player = None

    def __repr__(self):
        return f'{self.value} {self.suit}'

    def set_card(self, player):
        if self.player == None:
            self.player=player
            return self
        else:
            return False
