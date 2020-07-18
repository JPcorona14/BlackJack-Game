import random

suits = ('Hearts', 'Spades', 'Clubs', 'Diamonds')
ranks = ('2', '3', '4', '5', '6', '7', '8', '9',
         '10', 'Jack', 'Queen', 'King', 'Ace')
values = {'2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9, '10': 10,
          'Jack': 10,
          'Queen': 10, 'King': 10, 'Ace': 11}


class Card:
    """
    This Class helps set the deck class up to create the entire deck list
    """

    def __init__(self, suit, rank):
        self.suit = suit
        self.rank = rank
        self.value = values[rank]

    def __str__(self):
        return self.rank + " of " + self.suit


class Deck:
    # This class creates the deck that will be used during the game
    def __init__(self):
        self.all_card = []
        for suited in suits:
            for ranked in ranks:
                created_card = Card(suited, ranked)
                self.all_card.append(created_card)

    def shuffle(self):
        random.shuffle(self.all_card)

    def deal_one(self):
        return self.all_card.pop()
