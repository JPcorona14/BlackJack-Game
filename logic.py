import random
from card_book import Card, Deck
from characters import Player
from actions import deal, game_on, dealer_on


# GAME STARTS HERE
# Draw_Card = Deck()
# Draw_Card.shuffle()

Player1 = Player(input("Enter you Name:"))
Dealer1 = Player('Dealer')
Losing = False

# player_turn = game_on(Player1)
# dealer_turn = Dealer1.current_hand[0].value + Dealer1.current_hand[1].value

while True:
    game_turns = 0
    if game_turns == 0:
        Current_Bank = Player1.bank(
            int(input("How much will you be playing with today?\n")))
        player_bank = Player1.bank
        print(f"{Player1.name} is entering the game with ${Player1.bank}\n")
        print(deal(Player1, Dealer1))
    while True:
        bett = int(input("What is your bet for this hand?\n"))
        player_turn = game_on(Player1)
        dealer_turn = dealer_on(Dealer1)
        if player_turn == "Bust!":
            print(f'{Player1.name} Bust! \nDealer Wins!')
            break
        elif player_turn == "BlackJack!":
            print(f'{Player1.name} Wins with BlackJack!')
            break
        elif player_turn > dealer_turn:
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
    continue_playing = input("Would you like to play again? (Y/N)\n").lower
    if continue_playing == "y":
        game_turns += 1
    else:
        break
