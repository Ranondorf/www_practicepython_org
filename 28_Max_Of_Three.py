#!/usr/bin/python


import random as r


def max_of_3(a, b, c):
    print(f'Inputs are {a}, {b} and {c}.')
    current_max = ''
    if a > b:
        current_max = a
    else:
        current_max = b
    if current_max > c:
        return current_max
    else:
        return c
    

print(max_of_3(r.randint(-10, 10), r.randint(-10, 10), r.randint(-10, 10)))