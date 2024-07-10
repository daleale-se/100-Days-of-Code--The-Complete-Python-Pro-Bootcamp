import os
from art import logo

clear = lambda: os.system('clear')

def select_winner(bidders):
    highest_amount = 0
    winner_name = ""
    for name in bidders:
        if highest_amount < bidders[name]:
            highest_amount = bidders[name]
            winner_name = name
    
    print(f"The winner is {winner_name} with a bid of ${highest_amount}")

def main():
    
    print(logo)
        
    should_continue = True
    bidders = {}
    
    while should_continue:
                
        name = input("What is your name?: ")
        bid = int(input("What is your bid?: $"))
        bidders[name] = bid
        
        result = input("Are there any other bidders? Type 'yes' or 'no'. \n")
        if result == "no":
            should_continue = False
            select_winner(bidders)
    
        clear()

main()