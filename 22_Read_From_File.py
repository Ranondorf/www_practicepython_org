#!/usr/bin/python


categories = {}


with open('22_Input_File.txt', 'r') as open_file:
    line = open_file.readline()
    while line:
        category = line.split('/')[2]
        print(category)
        if categories.get(category) is None:
            categories[category] = 1
        else:
            categories[category] += 1
        line = open_file.readline()


print(categories)
    