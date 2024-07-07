rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

#Write your code below this line 👇

import random

choice_images = [rock, paper, scissors]
choice = int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors. \n"))
computer_choice = random.choice([0, 1, 2])

if not (0 < choice < 3):
    print("Incorrect choice")

print("Your chose: ")
print(choice_images[choice])

print("Computer chose: ")
print(choice_images[computer_choice])

if choice == 0:
    if computer_choice == 0:
        print("DRAW!")
    elif computer_choice == 1:
        print("YOU LOSE!")
    else:
        print("YOU WIN!")
elif choice == 1:
    if computer_choice == 0:
        print("YOU WIN!")
    elif computer_choice == 1:
        print("DRAW!")
    else:
        print("YOU LOSE!")
else: 
    if computer_choice == 0:
        print("YOU LOSE!")
    elif computer_choice == 1:
        print("YOU WIN!")
    else:
        print("DRAW!")