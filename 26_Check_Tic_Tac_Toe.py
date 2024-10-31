#!/usr/bin/python


import random


def generate_game():
    """Generates a random game result"""
    game = [[random.randint(0,2) for i in range(0, 3)] for j in range(0, 3)]
    print(*(item for item in game), sep='\n')
    return game


def check_win(game):
    """Check win condition of a game"""


    # Check horizontal win
    for row in game:
        if len(set(row)) == 1 and row[0] != 0:
            return row[0]
        

    # Check vertical win
    for i in range(3):
        if game[0][i] == game[1][i] == game[2][i] and game[0][i] != 0:
            return game[0][i]
        

    # Check diagonal win
    if (game[0][0] == game[1][1] == game[2][2] or game[0][2] == game[1][1] == game[2][0]) and game[1][1] != 0:
        return game[1][1]
    

    # Check for a draw
    list_elems = []
    for i in range(3):
        for j in range(3):
            list_elems.append(game[i][j])
    if len(set(list_elems)) == 2:
        return 0


    return -1


game = generate_game()
print(check_win(game))
