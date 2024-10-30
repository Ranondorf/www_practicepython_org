#!/usr/bin/python


class CreateBoard:
    """Class to create a board of x and y directions"""


    def __init__(self, x, y):
        """Initial dimensions"""
        self.x = x
        self.y = y


    def print_horizontal(self):
        """Prints a horizontal row"""
        for i in range(self.x):
            print(' ---', end='')


    def print_vertical(self):
        """Prints a vertical row"""
        for i in range(self.x):
            print('|   ', end='')
        print('|')


    def print_board(self):
        """Create a board"""
        for i in range(self.y):
            self.print_horizontal()
            print()
            self.print_vertical()
        self.print_horizontal()
        print()

x = int(input("Please enter the width of the board: "))
y = int(input("Please enter the height of the board: "))


a = CreateBoard(x, y)
a.print_board()