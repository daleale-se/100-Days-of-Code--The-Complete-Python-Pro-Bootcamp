import random

def select_random(words):
    return random.choice(words)

def generate_hidden_word(word: str):
    hidden_word = []
    for _ in word:
        hidden_word.append("_")
    return hidden_word

def guessed_word(hidden_word):
    for elem in hidden_word:
        if elem == "_":
            return False
    return True
    
def guess_positions(word, guess):
    positions = []
    for i in range(0, len(word)):
        if word[i] == guess:
            positions.append(i) 
    return positions
    
def reveal_letter(hidden_word, guess, positions):
    for pos in positions:
        hidden_word[pos] = guess

def show_stats(lifes, hidden_word):
    print()
    print(f"lifes: {lifes}")
    word = " ".join(hidden_word).upper()
    print(f"{word}")
    print()
