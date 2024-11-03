#!/usr/bin/python


import datetime


name = input("Please enter your name: ")
age = input("Please enter your age: ")
multiplier = int(input("How many times do you want to repeat the messages: "))


for i in range(0, multiplier):
    print(f'\nYour name is {name}')
    print(f'\nYour will turn 100 in the year {datetime.datetime.now().year + 100}')