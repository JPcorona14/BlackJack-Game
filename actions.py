from card_book import Card, Deck

Draw_Card = Deck()
Draw_Card.shuffle()


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
                if len(player.current_hand) >= 2:
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
