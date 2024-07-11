import random
from .utils import *

def guess_the_number():    
    clear()
    print(logo)
    
    print("Welcome to the Number Guessing Game!")
    print("I'm thinking of a number between 1 and 100.")
    
    game_stats = {
        "number" : random.randint(1, 100),
        "attempts" : ask_difficulty(),
        "found" : False
    }
    
    while continue_game(game_stats):
        
        print(f"You have {game_stats['attempts']} remaining to guess the number.")
        guess = int(input("Make a guess: "))
        
        check_guess(game_stats, guess)