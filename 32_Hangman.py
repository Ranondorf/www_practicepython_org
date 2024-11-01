#!/usr/bin/python


import random as r


def guess_letter(target, current):
    """Guess the letter"""
    error = False
    letter = input("Please guess a letter: ").upper()
    if letter in current:
        print("Already there, try again.")
        guess_letter(target, current)
    elif letter in target:
        for i in range(0, len(target)):
            if target[i] == letter:
                current[i] = letter
        print("Good guess.")
    else:
        # Bad guess
        print(f"Bad guess")
        error = True
    return current, error


def core_game():
    """Core of the game"""
    

    word_list = []


    with open('30_sowpods.txt', 'r') as word_file:
        line = word_file.readline().rstrip()
        word_list.append(line)
        while line:
            line = word_file.readline().rstrip()
            word_list.append(line)


    word = r.choice(word_list)
    current_progress = ["_" for letter in word]
    error_count = 0


    print("Welcome to Hangman")
    while word != "".join(current_progress) and error_count < 6:
        current_progress, error = guess_letter(word, current_progress)
        

        if error:
            error_count += 1
            print(f'Only {6 - error_count} incorrect attempts left')


        print(current_progress)
        


play_again = True


while True:
    core_game()
    print("\nGame over")
    play_again = input("\nWould you like to play again?").lower()[0]
    if play_again == 'False':
        break