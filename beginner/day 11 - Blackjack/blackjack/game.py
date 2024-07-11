from .art import logo
from .utils import *
from .constants import *

def blackjack():
    
    continue_playing = input("Do you want to play a game of Blackjack? Type 'y' or 'n': ") == "y"
    
    while continue_playing:
        
        clear()
        print(logo)
        
        player_deck = []
        player_deck.append(random_card())

        computer_deck = []
        computer_deck.append(random_card())
        
        another_card = True
        
        while another_card:
            player_deck.append(random_card())
            verify_ace(player_deck)
            
            print(f"Your cards: {player_deck}, current score: {sum(player_deck)}")
            print(f"Computer's first card: {computer_deck[0]}")
            
            another_card = False
            if score_smaller(player_deck, BLACKJACK): 
                another_card = input("Type 'y' to get another card, type 'n' to pass: ") == "y"
        
        while score_smaller(computer_deck, COMPUTER_SCORE_LIMIT) and score_smaller(player_deck, BLACKJACK):
            computer_deck.append(random_card())
            verify_ace(computer_deck)

        print(f"Your final hand: {player_deck}, final score: {sum(player_deck)}")
        print(f"Computer's final hand: {computer_deck}, final score: {sum(computer_deck)}")

        if score_greater(computer_deck, BLACKJACK):
            print("YOU WIN")
        elif score_greater(player_deck, BLACKJACK):
            print("YOU LOSE")
        elif sum(player_deck) == sum(computer_deck):
            print("DRAW")
        elif player_score_closest_blackjack(player_deck, computer_deck):
            print("YOU WIN")
        else:
            print("YOU LOSE")
            
        continue_playing = input("Do you want to play a game of Blackjack? Type 'y' or 'n': ") == "y"
    
    print("Goodbye")   