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


class Player:
    def __init__(self, name):
        self.name = name
        self.current_hand = []

    def add_card(self, card):
        self.current_hand.append(card)

    def __str__(self):
        return str(self.current_hand)


Draw_Card = Deck()
Draw_Card.shuffle()

Player1 = Player('Corona')
Dealer1 = Player('Dealer')


# Player1.current_hand.append(Draw_Card.deal_one())
# Player1.add_card(Draw_Card.deal_one())
# Player1.add_card(Draw_Card.deal_one())

def deal(p1, p2):
    p1.add_card(Draw_Card.deal_one())
    p2.add_card(Draw_Card.deal_one())
    p1.add_card(Draw_Card.deal_one())
    p2.add_card(Draw_Card.deal_one())
    hand = 0
    for card in p1.current_hand:
        print(f"{p1.name} has a {card}")
        hand += card.value
    print(f"{p2.name} has a {p2.current_hand[0]}")
    return f'\n{p1.name} total is currently at {hand}\n'


def game_on(player):
    hand = 0

    while True:
        start = True
        hand = 0
        while start:
            for card in player.current_hand:
                print(f"{player.name} has a {card}")
                hand += card.value
                if card.rank == 'Ace' and hand > 21:
                    hand -= 10
            start = False
            print(f"{player.name}'s Total: {hand}\n")
        if hand > 21:
            print("Bust!")
            break
        elif hand == 21:
            print("BlackJack!")
            break
        hit_or_stay = input('Would you like another card? (Y/N)\n').lower()
        if hit_or_stay == 'y':
            player.add_card(Draw_Card.deal_one())
        else:
            break
    return hand


print(deal(Player1, Dealer1))
print(game_on(Player1))
print(game_on(Dealer1))


# Need a Dealer to Hold Entire Deck and Draw from
# This could also be the table?


# Need a Player to receive cards

# Need a trash bin to send used cards (Extra)
