#!/usr/bin/python


import random


number = random.randint(1, 9)
number_of_guesses = 0
while True:
	guess = int(input("Guess a number between 1 and 9: "))
	number_of_guesses += 1
	if guess == number:
		break
	elif guess < 1 or guess > 9:
		print("Guess out of range")
		number_of_guesses -= 1


print(f"You needed {number_of_guesses} guesses to guess the number {number}")