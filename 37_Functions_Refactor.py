#!/usr/bin/python


def draw_vertline(number):
    """Draw vertical line"""
    for i in range(number):
        print(" ---", end="")
    print()


def draw_horiline(number):
    """Draw horizontal line"""
    for i in range(number):
        print("|   ", end="")
    print("|")


def draw_grid(number):
    """Draw a grid"""
    for i in range(number):
        draw_vertline(number)
        draw_horiline(number)
    draw_vertline(number)


draw_grid(5)