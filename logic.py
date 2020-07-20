import random
from card_book import Card, Deck
from characters import Player
from actions import deal, game_on, dealer_on
from actions import bank

# GAME LOGIC STARTS HERE

Player1 = Player(input("Enter you Name:\n"))
Dealer1 = Player('Dealer')
champ = True

# player_turn = game_on(Player1)
# dealer_turn = Dealer1.current_hand[0].value + Dealer1.current_hand[1].value

game_turns = 0
while True:
    if game_turns == 0:
        Current_Bank = bank(int(input("How much would you like to play with? \n")))
        print(f"{Player1.name} is entering the game with ${Current_Bank}\n")

    while True:
        print(deal(Player1, Dealer1))
        bet = int(input("What is your bet for this hand?\n"))
        if bet > Current_Bank:
            print("Insufficient Amount, Please enter new amount to bet!")
            bet = int(input("What is your bet for this hand?\n"))
        player_turn = game_on(Player1, Dealer1)
        dealer_hand = Dealer1.current_hand[0].value + Dealer1.current_hand[1].value

        if player_turn == "Bust!":
            print(f'{Player1.name} Bust! \nDealer Wins!')
            champ = False
            break
        elif player_turn == "BlackJack!":
            print(f'{Player1.name} Wins with BlackJack!')
            champ = True
            break
        elif player_turn >= dealer_hand:
            dealer_turn = dealer_on(Dealer1, player_turn)
            if dealer_turn == "Bust!":
                print(f"{Player1.name} Wins! Dealer Bust!")
                champ = True
                break
            elif dealer_turn == "BlackJack!":
                print(f"{Dealer1.name} Wins with BlackJack!")
                champ = False
                break
            elif player_turn < dealer_hand:
                print(f"Dealer wins with a total of {dealer_hand}!")
                champ = False
                break
        elif player_turn < dealer_hand:
            print(f"Dealer wins with a total of {dealer_hand}!")
            champ = False
            break
        else:
            print("Other outcome not specified!")
    if champ:
        Current_Bank += bet
    else:
        Current_Bank -= bet
        if Current_Bank <= 0:
            print('Game Over: No more funds')
            break
    print(f"Your current bank is:{Current_Bank}")
    continue_playing = input("Would you like to play again? (Y/N)\n").lower()
    #    print(continue_playing)
    while True:
        if continue_playing == "y" or continue_playing == "n":
            break
        print("Please enter a proper selection: Y for yes or N for no")
        continue_playing = input("Would you like to play again? (Y/N)\n").lower()
    if continue_playing == "y":
        Player1.current_hand = []
        Dealer1.current_hand = []
        game_turns += 1
    elif continue_playing == "n":
        print("Thank you for Playing!")
        break
