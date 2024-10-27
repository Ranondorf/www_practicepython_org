#!/usr/bin/python


number = int(input("Please provide a number as input: "))

if number == 0:
    output = "neither odd or even"
elif number % 2 == 0:
    output = "even"
else:
    output = "odd"

print(f'Your number is {output}')