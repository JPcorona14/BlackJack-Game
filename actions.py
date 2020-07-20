from card_book import Card, Deck

Draw_Card = Deck()
Draw_Card.shuffle()


def deal(p1, p2):
    p1.add_card(Draw_Card.deal_one())
    p2.add_card(Draw_Card.deal_one())
    p1.add_card(Draw_Card.deal_one())
    p2.add_card(Draw_Card.deal_one())
    hand = 0
    #    for card in p1.current_hand:
    #        print(f"{p1.name} has a {card}")
    #        hand += card.value
    #   print(f"\n{p2.name} has a {p2.current_hand[0]}")
    return '\n'


def draw(p1):
    p1.add_card(Draw_Card.deal_one())


def game_on(player, dealer_name):
    hand = 0
    while True:
        start = True
        hand = 0
        while start:
            for card in player.current_hand:
                print(f"{player.name} has a {card}")
                hand += card.value
            if any('Ace' in card.rank for card in player.current_hand) and hand > 21:
                hand -= 10
            start = False
            print(f"{player.name}'s Total: {hand}\n")
            print(f"\n{dealer_name.name} has a {dealer_name.current_hand[0]}")
        if hand > 21:
            hand = "Bust!"
            break
        elif hand == 21:
            hand = "BlackJack!"
            break
        hit_or_stay = input('Would you like another card? (Y/N)\n').lower()
        if hit_or_stay == 'y':
            player.add_card(Draw_Card.deal_one())
        else:
            break
    return hand


def bank(cash):
    return cash


def dealer_on(player, opponent):
    turn = 0
    while True:
        hand = 0
        player.add_card(Draw_Card.deal_one())
        last_card = player.current_hand[-1]
        for card in player.current_hand:
            print(f"{player.name} has a {card}")
            hand += card.value
            turn += 1
            if any('Ace' in card.rank for card in player.current_hand) and hand > 21:
                hand -= 10
        print(f"{player.name}'s Total: {hand}\n")
        if hand > 21:
            hand = "Bust!"
            break
        elif hand == 21:
            hand = "BlackJack!"
            break
        elif hand > opponent:
            break
    return hand
