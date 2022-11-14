# solution 1

import random

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

game_images = [rock, paper, scissors]

user_choice = int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors.\n"))
print(game_images[user_choice])

computer_choice = random.randint(0, 2)
print("Computer chose:")
print(game_images[computer_choice])

if user_choice >= 3 or user_choice < 0:
  print("You typed an invalid number, you lose!")
elif user_choice == 0 and computer_choice == 2:
  print("You win!")
elif computer_choice == 0 and user_choice == 2:
  print("You lose")
elif computer_choice > user_choice:
  print("You lose")
elif user_choice > computer_choice:
  print("You win!")
elif computer_choice == user_choice:
  print("It's a draw")



# solution 2

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

my_choice = int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors.\n"))

comp_choice = random.randint(0,2)

if my_choice >= 3 or my_choice<0:
    print("Invalid choice, you lose!")

if my_choice == 0:
    print(rock)
elif my_choice == 1:
    print(paper)
elif my_choice == 2:
    print(scissors)

print("Computer chose:")
if comp_choice == 0:
    print(rock)
elif comp_choice == 1:
    print(paper)
elif comp_choice == 2:
    print(scissors)

if my_choice == 0 and comp_choice == 0:
    print("Tie")
if my_choice == 0 and comp_choice == 1:
    print("You lose")
if my_choice == 0 and comp_choice == 2:
    print("You win")
if my_choice == 1 and comp_choice == 0:
    print("You win")
if my_choice == 1 and comp_choice == 1:
    print("Tie")
if my_choice == 1 and comp_choice == 2:
    print("You lose")
if my_choice == 2 and comp_choice == 0:
    print("You lose")
if my_choice == 2 and comp_choice == 1:
    print("You win")
if my_choice == 2 and comp_choice == 2:
    print("Tie")