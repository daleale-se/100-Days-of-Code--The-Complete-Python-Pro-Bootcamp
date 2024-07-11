from art import logo, vs
from game_data import data
from utils import *
import random


def main():
    
    score = 0
    end_of_game = False # (should_continue = True)
    
    instagram_b = random.choice(data)
    
    while not end_of_game:
        
        clear()
        print(logo)
        
        instagram_a = instagram_b
        
        instagram_b = random.choice(data)
        while instagram_a["name"] == instagram_b["name"]:
            instagram_b = random.choice(data)
        
        print(f"Compare A: {format(instagram_a)}")
        print(vs)
        print(f"Against B: {format(instagram_b)}")
            
        guess = input("Who has more followers? Type 'A' or 'B': ").lower()
        
        if check_answer(guess, instagram_a["follower_count"], instagram_b["follower_count"]):
            score += 1
            print(f"You're right! Current score: {score}")        
        else: 
            end_of_game = True            
            print(f"Sorry, that's wrong. Final score: {score}")
            

main()