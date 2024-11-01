#!/usr/bin/python


import random as r


word_list = []


with open('30_sowpods.txt', 'r') as word_file:
    line = word_file.readline().rstrip()
    word_list.append(line)
    while line:
        line = word_file.readline().rstrip()
        word_list.append(line)


print(r.choice(word_list))