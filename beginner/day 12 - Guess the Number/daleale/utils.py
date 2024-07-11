import os
from .art import logo

EASY_LEVEL_TURNS = 10
HARD_LEVEL_TURNS = 5

def clear():
    return os.system('clear')

def ask_difficulty():
    attempts = {"easy": EASY_LEVEL_TURNS, "hard": HARD_LEVEL_TURNS}
    level = input("Choose a difficulty. Type 'easy' or 'hard': ")
    return attempts[level]

def check_guess(game_stats, guess):
    if guess > game_stats["number"]:
        print("Too high.")
        game_stats["attempts"] -= 1
    elif guess < game_stats["number"]:
        print("Too low.")
        game_stats["attempts"] -= 1
    elif guess == game_stats["number"]:
        print(f"You got it! The answer was {game_stats['number']}")
        game_stats["found"] = True
    
    if game_stats["attempts"] == 0:
        print(f"The number was {game_stats['number']}.")
        print("You've run out of guesses, you lose.")

def continue_game(game_stats:dict):
    return game_stats["attempts"] > 0 and not game_stats["found"]