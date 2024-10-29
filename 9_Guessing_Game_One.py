#!/usr/bin/python


import random


target = random.randint(1,9)


guess_count = 0
while True:
    user_guess = int(input("Please take a guess of a number between 1 and 9: "))
    guess_count += 1

    if user_guess == target:
        print(f'Guessed it exactly!')
        print(f'You took {guess_count} guesses to get there.')
        break
    elif user_guess < target:
        print("A little too low")
    else:
        print("A little too high")