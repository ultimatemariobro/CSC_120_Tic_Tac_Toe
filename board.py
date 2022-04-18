# This file contains the stages required to build a 2 player Tic Tac Toe game
# By Mario Ramirez-Alvarenga
# Defining functions 
def print_board(boardVar):
    for i in range(3):
        print(boardVar[i])

# Printing the board
actualBoard = [['-', '-', '-'], ['-', '-', '-'], ['-', '-', '-']]
print("Printing board...")
print_board(actualBoard)


