from .utils import *

def hangman():    
    
    words = ["chicken", "satan", "house", "pokemon", "apple", "ocean", "banana"]
    word = select_random(words)
    hidden_word = generate_hidden_word(word)
    lifes = 7
    
    while not guessed_word(hidden_word) and lifes > 0:
        show_stats(lifes, hidden_word)
        guess = input("type a letter: ").lower() 
        
        while not guess.isalpha():
            guess = input("type a letter: ").lower()
        
        if guess in word:
            positions = guess_positions(word, guess)
            reveal_letter(hidden_word, guess, positions)
        else:
            lifes -= 1
    
    show_stats(lifes, hidden_word)
    
    if guessed_word(hidden_word):
        print("YOU WIN")
    elif lifes == 0:
        print("GAME OVER")