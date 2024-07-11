import os

def clear():
    return os.system('clear')

def format(instagram):
    return f"{instagram['name']}, a {instagram['description']}, from {instagram['country']}."
    
def check_answer(guess, a_followers, b_followers):
    """Take the user guess and follower counts and return if they got it right."""
    if a_followers > b_followers:
        return guess == "a"
    else:
        return guess == "b"    