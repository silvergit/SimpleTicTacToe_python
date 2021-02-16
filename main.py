# Created by Alireza Pazhouhesh
# Copyright: GPL v3
# feb, 16, 2021

def clearBoard():
    newBoard = [" ", " ", " ", " ", " ", " ", " ", " ", " "]
    return newBoard

def printBoard(board):
    print()
    print(board[0], " |", board[1], "| ", board[2])
    print("---+---+---")
    print(board[3], " |", board[4], "| ", board[5])
    print("---+---+---")
    print(board[6], " |", board[7], "| ", board[8])
    print()

def checkWin(board, turn):
    if((board[0] == turn and board[0] == board[1] and board[0] == board[2]) or
        (board[3] == turn and board[3] == board[4] and board[3] == board[5]) or
        (board[6] == turn and board[6] == board[7] and board[6] == board[8]) or 
        (board[0] == turn and board[0] == board[3] and board[0] == board[6]) or
        (board[1] == turn and board[1] == board[4] and board[1] == board[7]) or
        (board[2] == turn and board[2] == board[5] and board[2] == board[8]) or
        (board[0] == turn and board[0] == board[4] and board[0] == board[8]) or
        (board[2] == turn and board[2] == board[4] and board[2] == board[6])):
        return "yes"
    return "no"

def checkForEmptyCell(board):
    for i in board:
        if(i == " "):
            return "yes"
    return "no"

def canFill(board, row, column):
    if(board[3 * row + column] == " "):
        return "yes"
    return "no"

def changeTurn(turn):
    if turn == "X":
        return "O"
    else:
        return "X"

board = [" ", "O", "X", 
         "O", "X", "O", 
         "X", "O", "X"]

turn = "X"
board = clearBoard()

while(1):
    printBoard(board)
    print("Turn = ", turn) 

    if(checkForEmptyCell(board) == "no"):
        print("The board is full.")
        playAgain = input("Do you want to play again?(Y/N): ")
        if(playAgain == "N"):
            break
        else:
            board = clearBoard()
            turn = "X"
        
    else:
        while(1):
            r = int(input("Input row: "))
            c = int(input("Input column: "))
            if(r>2 or c>2):
                print("Enter 0 or 1 or 2")
            elif canFill(board, r, c) == "yes":
                board[3 * r + c] = turn
                break
            else:
                print("The row ", r, " and the column ", c, " is full, Enter new row and column")

        if(checkWin(board, turn) == "yes"):
            printBoard(board)
            print("Game Over")
            print("The winner is ", turn)
            playAgain = input("Do you want to play again?(Y/N): ")
            if(playAgain == "N"):
                break
            else:
                board = clearBoard()
                turn = "X"

        turn = changeTurn(turn)




