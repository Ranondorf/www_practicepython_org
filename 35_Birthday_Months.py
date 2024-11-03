#!/usr/bin/python


import json


def birthday_months(filename):
    """Calculate birthday months"""
    month_int = {1 : 0, 2 : 0, 3 : 0, 4 : 0, 5 : 0, 6 : 0, 7 : 0, 8 : 0, 9 : 0, 10 : 0, 11 : 0, 12 : 0}
    month_name = ["January", "February", "March", "April", "May", "June", "July", "August", "September", "October", "November", "December"]
    return_dict = {}


    with open(filename, 'r', encoding='utf-8') as open_file:
        database = json.load(open_file)
    
    
    for value in database.values():
        if int(value.split("/")[1]) in month_int.keys():
            month_int[int(value.split("/")[1])] += 1
    

    for i in range(12):
        return_dict[month_name[i]] = month_int[i + 1]

    

    return return_dict


print(json.dumps(birthday_months("34_Database.json"), indent=4))