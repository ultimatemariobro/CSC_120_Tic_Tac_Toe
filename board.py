# This file contains the stages required to build a 2 player Tic Tac Toe game
# By Mario Ramirez-Alvarenga
actualBoard = [['-', '-', '-'],  # row [0]
                ['-', '-', '-'], # row [1]
                ['-', '-', '-']] # row [2]   
# Definining Functions

def print_board(board):
    for i in range(3):
        print(board[i])
        
# prototype !!! DELETE this when working properly 
def place_mark(row, col, player_id):
    for row in range(3):
        for col in range(3):
            if actualBoard[row][col] == '-' and player_id == 1:
                playerSymbolplace = 'X'          # places symbol 
                actualBoard[row][col] = playerSymbolplace
            elif actualBoard[row][col] == '-' and player_id == 2:
                playerSymbolplace = 'O'
                actualBoard[row][col] = playerSymbolplace
                 
              
def check_mark(row, col):
    if actualBoard[row][col] == '-':
        return True
    return False

def check_win(row, col, player_id):
    if player_id == 1:
        char = 'X'
    elif player_id == 2:
        char = 'O'
    else:
        print("Invalid!!! BUG!!!")

    gameWon = False
    
    # Check horizontally 
    for i in range(0, 3):
        if (actualBoard[i][0] and actualBoard[i][1] and actualBoard[i][2] in char)  and (actualBoard[i][0] == actualBoard[i][1] == actualBoard[i][2]):
            gameWon = True
            break
    # Check Vertically 
    if (actualBoard[0][0] and actualBoard[1][0] and actualBoard[2][0] in char) and (actualBoard[0][0] == actualBoard[1][0] == actualBoard[2][0]):
        gameWon = True
    elif (actualBoard[0][1] and actualBoard[1][1] and actualBoard[2][1] in char) and (actualBoard[0][1] == actualBoard[1][1] == actualBoard[2][1]):
            gameWon = True
    elif (actualBoard[0][2] and actualBoard[1][2] and actualBoard[2][2] in char) and (actualBoard[0][2] == actualBoard[1][2] == actualBoard[2][2]):
            gameWon = True
    else:
        break
   
   # Check diagonally 
    if (char in actualBoard[0[0] or char in actualBoard[1][1] or char in actualBoard[2][2]) and (actualBoard[0][0] == actualBoard[1][1] == actualBoard[2][2]):
            gameWon = True
    elif (char in actualBoard[2][0] or char in actualBoard[1][1] or char in actualBoard[0][2]) and (actualBoard[2][0] == actualBoard[1][1] == actualBoard[0][2]):
            gameWon = True
    else: 
        gameWon = False
        break
    
    return gameWon


def ifTie(actualBoard):
    counter = 0
    symbols = ['X', 'O']
    for i in actualBoard:
        for j in range(0,3):
            counter += 1
    if counter == 9:
        tie = True
        return tie

def mainFunctionRun(actualBoard):
    row = 0
    col = 0
    player_id = 0
    mainFunction(row, col, player_id)

def mainFunction(row, col, player_id):
    print("Welcome to Tic-Tac_Toe in Command Line Python!")
    print("Players must take turns until a winner is declared.")
    print("Here's the empty board that will be updated each turn pass.")
    print("Printing board...")        
    print_board(actualBoard)
    print("Good Luck!")
    print("------------------------------------------")
    print("Player 1, make your move: ")
    row = int(input("Enter row number 0-2: "))
    col = int(input("Enter column number 0-2: "))
    player_id = 1
    place_mark(row, col, player_id)
    while check_mark(row, col) == True:
        player_id = 2
        print("Player 2, make your move: ")
        row = int(input("Enter row number 0-2: "))
        col = int(input("Enter column number 0-2: "))
        place_mark(row, col, player_id)  
        print(actualBoard)
        player_id = 1 
        print("Player 1, make your move: ")
        row = int(input("Enter row number 0-2: "))
        col = int(input("Enter column number 0-2: "))
        place_mark(row, col, player_id)
        print(actualBoard)
    else:
        print("Invalid input. Index out of range.")
        print('\n')
        print("Close program and try again.")
        break
    
    if check_win(row, col, player_id) == True:
        player = player_id
        print(f"Player {player} has won this match. Thanks for playing!") 
        answer = input(print("Care to play again? Y for yes / N for no"))    
        if (answer == 'Y' or answer == 'y'):
            mainFunctionRun(actualBoard)
        elif (answer == 'N' or answer == 'n')
            break
        else:
            print("Invalid Input. Close program and try again.")
    
    elif ifTie(row, col) == True:
        print("Its a draw. Thank you for playing.")


mainFunctionRun