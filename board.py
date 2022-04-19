# This file contains the stages required to build a 2 player Tic Tac Toe game
# By Mario Ramirez-Alvarenga
# Empty board 
actualBoard = [['-', '-', '-'], ['-', '-', '-'], ['-', '-', '-']]
# Definining Functions
def print_board(board):
    for i in range(3):
        print(board[i])
        
print("Printing board...")        
print_board(actualBoard)


def place_mark(row, col, player_id):
    if player_id == 1:
        playerSymbol = 'X'
    else:
        playerSymbol = 'O'
    actualBoard[row][col] = playerSymbol

def check_mark(row, col):
    if actualBoard[row][col] == '-':
        return True
    return False

def check_win(player_id):
    if player_id == 1:
        char = 'X'
    elif player_id == 2:
        char = 'O'
    
    targetSlot = [char for i in range(3)]
    gameWon = False
    for row in range(3):
        if targetSlot == actualBoard[row]:
            gameWon = True
        col = [actualBoard[i][row] for i in range(3)]
        if targetSlot == col:
            gameWon = True

    check_diagonally = [actualBoard[i][i] for i in range(3)]
    if targetSlot == check_diagonally:
        gameWon = True
    check_diagonally = [actualBoard[0][2], actualBoard[1][1], actualBoard[2][0]]
    if targetSlot == check_diagonally:
        gameWon = True
    
    return gameWon

def mainFunction(row, col, player_id):
    print("Player 1, make your move: ")
    row = int(input("Enter row number 0-2: "))
    col = int(input("Enter column number 0-2: "))

    while check_mark(row, col) == True:
        print("Player 2, make your move: ")
        row = int(input("Enter row number 0-2: "))
        col = int(input("Enter column number 0-2: "))
        actualBoard.append(row)
        actualBoard.append(col)
        print(actualBoard)

        print("Player 1, make your move: ")
        row = int(input("Enter row number 0-2: "))
        col = int(input("Enter column number 0-2: "))
        actualBoard.append(row)
        actualBoard.append(col)
        print(actualBoard)
    else:
        print("Invalid input. Index out of range.")
        print('\n')
        print("Close program and try again.")
    place_mark(row, col, player_id)
    if check_win(player_id) == True:
        print("Player has won this match. Thanks for playing!")
        print("Care to play again? Y for yes / N for no")
    #elif 
        #set up tie or draw code

row = 0
col = 0
player_id = 0 
mainFunction(row, col, player_id)