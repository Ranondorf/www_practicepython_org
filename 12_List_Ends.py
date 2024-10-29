#!/usr/bin/python


import random


def _generate_list():
    """Generate a list of random length and random numbers, with min length being 2"""
    return [random.randint(1, 10) for num in range(0, random.randint(2, 50))]


def final_list():
    input_list = _generate_list()
    print(input_list)
    return [input_list[0], input_list[len(input_list) - 1]]


print(final_list())