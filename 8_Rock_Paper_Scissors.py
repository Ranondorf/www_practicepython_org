#!/usr/bin/python


def chart(input1, input2):
    if input1 == input2:
        winner = 'draw'
    elif input1 == "rock" and input2 == "scissors":
        winner = 'player 1'
    elif input2 == "rock" and input1 == "scissors":
        winner = 'player 2'
    elif input1 == "scissors" and input2 == "paper":
        winner = 'player 1'
    elif input2 == "scissors" and input1 == "paper":
        winner = 'player 2'
    elif input1 == "paper" and input2 == "rock":
        winner = 'player 1'
    elif input2 == "paper" and input1 == "rock":
        winner = 'player 2'
    else:
        print("Shouldn't get here")
    return winner


play = True


while play:
    player1 = input("Player 1 please enter your choice of rock, paper and scissors: ").lower()
    player2 = input("Player 2 please enter your choice of rock, paper and scissors: ").lower()
    result = chart(player1, player2)
    print(f'The winner is {result}')
    play_again = input("Would you like to play again: Y or N?").lower()


    if play_again == "n":
        break