#!/usr/bin/python


class CreateBoard:
    """Class to create a board of x and y directions"""


    def __init__(self, x, y, board):
        """Initial dimensions"""
        self.x = x
        self.y = y
        self.board = board


    def print_horizontal(self):
        """Prints a horizontal row"""
        for i in range(self.x):
            print(' ---', end='')


    def print_vertical(self, row):
        """Prints a vertical row"""
        for i in range(self.x):
            print(f'| {self.board[row][i]} ', end='')
        print('|')


    def print_board(self):
        """Create a board"""
        for i in range(self.y):
            self.print_horizontal()
            print()
            self.print_vertical(i)
        self.print_horizontal()
        print()


def mark_pos(player):
    """Function for marking position"""
    user_input = input(f"\n{player} please enter the coordinate in the format 'x, y' where x and y are in the range 1 to 3: ").split(",")
    return user_input

def initial_board():
    """Create a blank board"""
    return [["0" for i in range(3)] for j in range(3)]


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
        return "0"


    return -1

def win_draw_action(draw_win):
    """What to do when there is a draw or a win"""
    end_game = True
    

    if draw_win == "X":
        print("Player 1 wins")
    elif draw_win == "O":
        print("Player 2 wins")
    elif draw_win == "0":
        print("It was a draw")
    else:
        # Game goes on
        end_game = False
    return end_game, draw_win


def core_game():


    players = {True : "Player 1", False : "Player 2"}
    current_player = True
    board = initial_board()


    for i in range(9):
        while True:
            coordinates = mark_pos(players[current_player])
            board_x = int(coordinates[0]) - 1
            board_y = int(coordinates[1]) - 1
            board_pos_val = board[board_x][board_y]
            if board_pos_val == "0" and current_player:
                board[board_x][board_y] = "X"
                drawboard = CreateBoard(3, 3, board)
                drawboard.print_board()
                end_game, result = win_draw_action(check_win(board))
                if end_game:
                    return result
                else:    
                    break
            elif board_pos_val == "0" and not current_player:
                board[board_x][board_y] = "O"
                drawboard = CreateBoard(3, 3, board)
                drawboard.print_board()
                end_game, result = win_draw_action(check_win(board))
                if end_game:
                    return result
                else:    
                    break
            else:
                # Slot already occupied
                print("Slot occupied please try again.")
                drawboard = CreateBoard(3, 3, board)
                drawboard.print_board()
        current_player = not current_player


score_board = {"X":0, "O":0, "0":0}


while True:


    score_board[core_game()] += 1
    print(f'\nCurrent tally is, player 1\'s win count is {score_board["X"]}, player 2\'s wind count is {score_board["O"]} and the draw count is {score_board["0"]}\n')
    keep_playing = input("Would you like to keep playing?").lower()[0]
    
    
    if keep_playing == "n":
        break
