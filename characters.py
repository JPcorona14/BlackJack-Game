class Player:
    def __init__(self, name):
        self.name = name
        self.current_hand = []

    def add_card(self, card):
        self.current_hand.append(card)

    # def bank(self, amount):
    #    self.amount = int(amount)

    def __str__(self):
        return str(self.current_hand)
