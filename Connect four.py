from copy import deepcopy
import random

 
HEIGHT = 6
WIDTH = 7
 
def initialize():
    ''' Sets up the empty board. '''
    board = []
    for i in range(HEIGHT):
        board.append(["O"] * WIDTH)
    return board
   
def print_board(board):
    ''' Prints out a correct formatted board. '''
    print("")
    print("1 2 3 4 5 6 7")
    print("_" * 13)
    for row in board:
        print("|".join(row))
       
def get_move(board, player):
    '''  Takes the board and the player as parameter.  Asks the player to input a
    column and checks if the entry is valid. '''
    col = int(input("Player {} enter a column: ".format(player)))
    if col > WIDTH or col < 1:
        print("Invalid input. Enter a number between 1 and 7.")
        col = get_move(board, player)
   
    col = col - 1
   
    col_full = True
    for i in range(HEIGHT):
        if board[i][col] == "O":
            col_full = False
            break
    if col_full:
        print("That column is full. Try again.")
        col = get_move(board, player)
    return col
   
def get_comp_move(board):
    for col in range(WIDTH):
        temp_board = deepcopy(board)
        temp_board = make_move(temp_board, "B", col)
        if check_win(temp_board) == "B":
            return col
       
    for col in range(WIDTH):
        temp_board = deepcopy(board)
        temp_board = make_move(temp_board, "A", col)
        if check_win(temp_board) == "A":
            return col
   
    return random.randint(0, WIDTH - 1)
   
   
def make_move(board, player, col):
    ''' Takes the board, the player, and the player's entry and makes the move based
    on the board configuration and the entry. '''
    row = 0
    for i in range(HEIGHT):
        if board[i][col] == "O":
            row = i
        else:
            break
       
    board[row][col] = player
    return board
 
def check_win(board):
    ''' This function takes the board as a parameter and checks if someone has won
    the game.  If so, it returns the player that has won.  Otherwise, it returns
    an empty string. '''
    for row in range(HEIGHT):
        for col in range(WIDTH - 3):
            if (board[row][col] == board[row][col+1] == board[row][col+2] == board[row][col+3]) and board[row][col] != "O":
                return board[row][col]
   
    for col in range(WIDTH):
        for row in range(HEIGHT - 3):
            if (board[row][col] == board[row+1][col] == board[row+2][col] == board[row+3][col]) and board[row][col] != "O":
                return board[row][col]
               
    for row in range(HEIGHT - 3):
        for col in range(WIDTH - 3):
            if (board[row][col] == board[row+1][col+1] == board[row+2][col+2] == board[row+3][col+3]) and board[row][col] != "O":
                return board[row][col]
   
    for row in range(HEIGHT - 1, HEIGHT - 3, -1):
        for col in range(WIDTH - 3):
            if (board[row][col] == board[row-1][col+1] == board[row-2][col+2] == board[row-3][col+3]) and board[row][col] != "O":
                return board[row][col]
   
    full = True
    for row in range(HEIGHT):
        for col in range(WIDTH):
            if board[row][col] == "O":
                full = False
                break
    if full:
        return "Tie"
   
    return ""
 
def main():
    ''' Sets up the game and runs the game loop until the game is over. '''
    board = initialize()
    player = "A"
    winner = ""
   
    while winner == "":
        print_board(board)
        if player == "A":
            col = get_move(board, player)
            board = make_move(board, player, col)
            winner = check_win(board)
        else: 
            col = get_comp_move(board)
            board = make_move(board, player, col)
        winner =  check_win(board)
        player = "B" if player == "A" else "A"
   
    print_board(board)
    if winner == "Tie":
        print("Tie.")
    else:
        print("Player {} wins".format(winner))
 
if __name__ == "__main__":
    main()