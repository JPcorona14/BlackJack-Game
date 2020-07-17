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
Losing = False

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
    print(f"\n{p2.name} has a {p2.current_hand[0]}")
    return '\n'


def game_on(player):
    hand = 0

    while True:
        start = True
        hand = 0
        while start:
            for card in player.current_hand:
                if len(player.current_hand) == 2:
                    pass
                else:
                    print(f"{player.name} has a {card}")
                hand += card.value
                if card.rank == 'Ace' and hand > 21:
                    hand -= 10
            start = False
            print(f"{player.name}'s Total: {hand}\n")
        if hand > 21:
            return "Bust!"
            break
        elif hand == 21:
            return "BlackJack!"
            break
        hit_or_stay = input('Would you like another card? (Y/N)\n').lower()
        if hit_or_stay == 'y':
            player.add_card(Draw_Card.deal_one())
        else:
            break
    return hand


def dealer_on(player):
    start = True
    hand = 0
    player.add_card(Draw_Card.deal_one())
    while start:
        for card in player.current_hand:
            print(f"{player.name} has a {card}")
            hand += card.value
            if card.rank == 'Ace' and hand > 21:
                hand -= 10
        start = False
        print(f"{player.name}'s Total: {hand}\n")
    if hand > 21:
        return "Bust!"
    elif hand == 21:
        return "BlackJack!"
    return hand


print(deal(Player1, Dealer1))

player_turn = game_on(Player1)
dealer_turn = Dealer1.current_hand[0].value + Dealer1.current_hand[1].value

while True:
    if player_turn == "Bust!":
        print(f'{Player1.name} Bust! \nDealer Wins!')
        break
    elif player_turn == "BlackJack!":
        print(f'{Player1.name} Wins with BlackJack!')
        break
    elif player_turn > dealer_turn:
        dealer_turn = dealer_on(Dealer1)
        while True:
            if dealer_turn == "Bust!":
                print(f"{Player1.name} Wins!")
                break
            elif dealer_turn == "BlackJack!":
                print(f"{Dealer1.name} Wins with BlackJack!")
                break
            else:
                print(dealer_on(Dealer1))
        break

    if dealer_turn == "Bust!":
        print(f"{Player1.name} Wins!")
    elif dealer_turn == "BlackJack!":
        print(f"{Dealer1.name} Wins with BlackJack!")
    else:
        print(
            f"{Dealer1.name} Wins with {Dealer1.current_hand[0]} & {Dealer1.current_hand[1]}")
