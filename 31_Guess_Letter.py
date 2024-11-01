#!/usr/bin/python


def guess_letter(target, current):
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
        print("Bad guess.")
    return current

word = "EVAPORATE"
current_progress = ["_" for letter in word]

print("Welcome to Hangman")
while word != "".join(current_progress):
    print(guess_letter(word, current_progress))