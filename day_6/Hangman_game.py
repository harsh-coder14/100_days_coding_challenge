

import random
from hangman_art import *
from hangman_words import *

print(logo)
chosen_word = random.choice(word_list)
print(chosen_word)
display = []
for blank in chosen_word:
    display.append('_')

stage = 6
while "_" in display:
    guess = input("Guess a letter: ").lower()
    n = 0

    for letter in chosen_word:
        if guess in display:
            print(f"You have already entered {guess}")
            break

    for letter in chosen_word:
        if letter == guess:
            display[n] = guess
            # break
        elif guess not in chosen_word:
            print(stages[stage])
            print(f"Lives Reamining: {stage}" )
            stage -= 1
            break

        n += 1

    print(display)
    if "_" not in display:
        print("You Win")

    if stage < 0:
        print("Game over")
        break




