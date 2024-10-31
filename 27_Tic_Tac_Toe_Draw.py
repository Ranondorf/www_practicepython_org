#!/usr/bin/python


def mark_pos(player):
    """Function for marking position"""
    user_input = input(f"{player} please enter the coordinate in the format 'x, y' where x and y are in the range 1 to 3: ").split(",")
    return user_input

def initial_board():
    """Create a blank board"""
    return [[0 for i in range(3)] for j in range(3)]


players = {True : "Player1", False : "Player2"}
current_player = True
board = initial_board()


for i in range(9):
    while True:
        coordinates = mark_pos(players[current_player])
        board_x = int(coordinates[0]) - 1
        board_y = int(coordinates[1]) - 1
        board_pos_val = board[board_x][board_y]
        if board_pos_val == 0 and current_player:
            board[board_x][board_y] = "X"
            break
        elif board_pos_val == 0 and not current_player:
            board[board_x][board_y] = "O"
            break
        else:
            # Slot already occupied
            print("Slot occupied please try again.")
            print(*(row for row in board), sep='\n')
    current_player = not current_player
    print(*(row for row in board), sep='\n')
                                          