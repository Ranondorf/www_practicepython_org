#!/usr/bin/python


import json


def write_to_json(database, json_file_name):
    """Write JSON into a file"""
    with open(json_file_name, 'w', encoding='utf-8') as open_file:
        open_file.write(json.dumps(database))


def add_to_json(add, json_file_name):
    """Add a dictionary into an existing structure on file"""
    database = read_json(json_file_name)
    database.update(add)
    write_to_json(database, json_file_name)


def read_json(json_file_name):
    """Load JSON from file into a Python dictionary"""
    with open(json_file_name, 'r', encoding='utf-8') as open_file:
        database = json.load(open_file)
        return database


def query_user_for_president(json_file_name):
    name = input("Please enter a president's name in FIRSTNAME LASTNAME: ")
    date = input("Please enter the birthdate in DD/MM/YYYY: ")
    add_to_json({name : date}, '34_Database.json')

def welcome(database):
    """Main query program that takes user inputs"""
    print("Welcome to the birthday. We know the birthdays of:")
    print(*database.keys(), sep='\n')
    lookup = input("Whose birthday do you want to look up?")
    print(f'{lookup}\'s birthday is {database[lookup]}')





database = {'Benjamin Franklin' : '17/01/1706', 'Thomas Jefferson' :  '13/04/1743', 'George Washington' : '22/02/1732', 'Paul Revere' : '21/12/1734'}

write_to_json(database, '34_Database.json')
query_user_for_president('34_Database.json')


