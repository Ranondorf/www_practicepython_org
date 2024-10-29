#!/usr/bin/python


def input_num():
    return int(input("Please input a number: "))
    

number = input_num()

if len([divisor for divisor in range(1, number) if number % divisor == 0]) == 1:
    print("It is a prime number")
else:
    print("It is not a prime number")