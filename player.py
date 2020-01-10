class Player:
    def __init__(self, name):
        self.name = name
        self.hand = []

    def __repr__(self):
        return self.name

    def get_cards(self, *cards:list[Card]):
        for card in cards:
            self.hand.append(card)
    
    def clear_hand(self):
        self.hand.clear()
    