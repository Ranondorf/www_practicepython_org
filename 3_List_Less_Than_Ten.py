#!/usr/bin/python


a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
print(f'Here is the current list: {a}')
num = int(input("Enter a number and I will create a new list with items below that number: "))
print([i for i in a if i < num])