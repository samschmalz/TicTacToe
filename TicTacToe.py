#!/usr/bin/python3

__author__ = "Sam Schmalzried"

board = [["_" for j in range(3)] for i in range(3)]
player = "X"

def PrintBoard():
    for i in range(3):
        row = "| "
	for j in range(3):
            row += (board[i][j] + " | ")
	print(row)

def Move(player):
    valid = False
    row, col = AskMove()
    while not valid:
	if row >= 3 or row < 0 or col >= 3 or col < 0:
	    print ("Not a valid move. Please enter values between 1 and 3.")
	    row, col = AskMove()
	elif board[row][col] != '_':
	    print("That space is already taken.  Please try again.")
	    row, col = AskMove()
	else:
	    board[row][col] = player
	    valid = True

def SwitchPlayers(player):
    if player == "X":
	player = "O"
    elif player == "O":
	player = "X"
    return player

def AskMove():
    row = int(input("Row to play: ")) - 1
    col = int(input("Column to play: ")) - 1
    return row, col

def PrintPlayer(player):
    print("It is player %s 's turn" % player)

def Play(player):
    PrintBoard()
    count = 1
    while count <= 9:
	PrintPlayer(player)
	Move(player)
	PrintBoard()
        if CheckWin():
            print("Player %s wins" % player)
            break
        else:
	    player = SwitchPlayers(player)
	    count += 1

def CheckWin():
    for x in range(3):
        if board[x][0] == board[x][1] == board[x][2] != '_' or board[0][x] == board[1][x] == board[2][x] != '_':
            return True
    if board[0][0] == board[1][1] == board[2][2] != '_' or board[0][2] == board[1][1] == board[2][0] != '_':
        return True
    return False

Play(player)
