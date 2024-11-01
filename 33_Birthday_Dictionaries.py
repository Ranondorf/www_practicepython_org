#!/usr/bin/python


def welcome(database):
    print("Welcome to the birthday. We know the birthdays of:")
    print(*database.keys(), sep='\n')
    lookup = input("Whose birthday do you want to look up?")
    print(f'{lookup}\'s birthday is {database[lookup]}')

database = {'Benjamin Franklin' : '17/01/1706', 'Thomas Jefferson' :  '13/04/1743', 'George Washington' : '22/02/1732', 'Paul Revere' : '21/12/1734'}


welcome(database)