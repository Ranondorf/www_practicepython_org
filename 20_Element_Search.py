#!/usr/bin/python


import random


ordered_list = sorted(list(set([random.randint(1, 25) for num in range(0,random.randint(1, 20))])))
number = int(input("Please enter the number you would like to search in a random ordered list of numbers: "))


print(ordered_list)
print(number)


def binary_search(sub_list, number):
    """Binary search of the ordered list"""
    if sub_list[len(sub_list) // 2] == number :
        return "Found it"
    elif sub_list[len(sub_list) // 2] > number and len(sub_list) != 1:
        sub_list = sub_list[0:len(sub_list) // 2]
        return binary_search(sub_list, number)
    elif sub_list[len(sub_list) // 2] < number and len(sub_list) != 1:
        sub_list = sub_list[len(sub_list) // 2:]
        return binary_search(sub_list, number)
    else:
        return "Doesn't exist"


print(binary_search(ordered_list, number))