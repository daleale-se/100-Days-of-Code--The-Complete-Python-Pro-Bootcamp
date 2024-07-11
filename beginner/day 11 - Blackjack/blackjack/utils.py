import os
import random
from .constants import BLACKJACK

def clear():
    return os.system('clear')

def random_card():
    cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
    return random.choice(cards)

def verify_ace(deck:list):
    if deck[-1] == 11 and sum(deck) > BLACKJACK:
        deck.remove(11)
        deck.append(1)

def player_score_closest_blackjack(deck1:list, deck2:list):
    diff1 = BLACKJACK - sum(deck1)
    diff2 = BLACKJACK - sum(deck2)
    return min(diff1, diff2) == diff1

def score_smaller(deck:list, num:int):
    return sum(deck) < num

def score_greater(deck:list, num:int):
    return sum(deck) > num

def result(player_deck, computer_deck):
    if score_greater(computer_deck, BLACKJACK):
        return "Opponent went over. You win"
    elif score_greater(player_deck, BLACKJACK):
        return "You went over. You lose"
    elif sum(player_deck) == sum(computer_deck):
        return "Draw"
    elif sum(player_deck) == 21:
        return "Win with Blackjack"
    elif sum(computer_deck) == 21:
        return "Lose, opponent has Blackjack"
    elif player_score_closest_blackjack(player_deck, computer_deck):
        return "You win"
    else:
        return "You lose"