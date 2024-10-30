#!/usr/bin/python


def read_file(filename):
    f = open(filename, 'r')
    line = f.readline()
    result = set()
    while line:
        result.add(int(line.rstrip('\n')))
        line = f.readline()
    return result


print(sorted(list(read_file('23_primenumbers.txt').intersection(read_file('23_happynumbers.txt')))))
