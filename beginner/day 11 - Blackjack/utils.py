import os
import random

BLACKJACK = 21
COMPUTER_SCORE_LIMIT = 18

def clear():
    return os.system('clear')

def random_card():
    cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
    return random.choice(cards)

def verify_ace(deck:list):
    if 11 in deck and sum(deck) > BLACKJACK:
        deck.remove(11)
        deck.append(1)

def player_score_closest_blackjack(deck1:list, deck2:list):
    diff1 = BLACKJACK - sum(deck1)
    diff2 = BLACKJACK - sum(deck2)
    return min(diff1, diff2) == diff1

def score_smaller_blackjack(deck:list):
    return sum(deck) < BLACKJACK

def score_smaller_limit(deck:list):
    return sum(deck) < COMPUTER_SCORE_LIMIT

def score_greater_blackjack(deck:list):
    return sum(deck) > BLACKJACK