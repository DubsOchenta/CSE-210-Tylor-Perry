"""========================================================================================
Author(s): Tylor Perry (per11034@byui.edu)
Created: 01/10/2022
File: tic-tac-toe-game.py
==========================================================================================="""
from termcolor import colored

board = [ " ", " ", " ",
        " ", " ", " ",
        " ", " ", " "]
X = colored("X", "blue", attrs=["bold"])
O = colored("O", "red", attrs=["bold"])
current_player = X
winner = None
game_running = True

#Main function to bring the whole batch of functions together to create a program.
def main():
    while game_running:
        # print_board(board)
        player_input(board)
        print_board(board)
        check_win(board)
        check_tie(board)
        switch_player()
    print_board(board)
#Print the game board
def print_board(board):
    print(f"\n{board[0]}|{board[1]}|{board[2]}")
    print("-+-+-")
    print(f"{board[3]}|{board[4]}|{board[5]}")
    print("-+-+-")
    print(f"{board[6]}|{board[7]}|{board[8]}\n")
print_board(board)
#Take the player input
def player_input(board):
    global current_player
    player = int(input("Enter a number 1-9 to choose a square: "))
    if player >= 1 and player <= 9 and board[player - 1] == " ":
        board[player - 1] = current_player
    else:
        print("\nOops, someone is already in that spot. You forfeit your turn.\nChoose better next time")
#Check for win or tie
def check_horizontal(board):
    global winner
    if board[0] == board[1] == board[2] and board[1] != " ":
        winner = board[0]
        return True
    elif board[3] == board [4] == board[5] and board[3] != " ":
        winner = board[3]
        return True
    elif board[6] == board [7] == board[7] and board[6] != " ":
        winner = board[6]
        return True

def check_vertical(board):
    global winner
    if board[0] == board[3] == board[6] and board[0] != " ":
        winner = board[0]
        return True
    elif board[1] == board[4] == board[7] and board[1] != " ":
        winner = board[0]
        return True
    elif board[3] == board[5] == board[8] and board[3] != " ":
        winner = board[0]
        return True

def check_diagonal(board):
    global winner
    if board[0] == board[4] == board[8] and board[0] != " ":
        winner = board[0]
        return True
    elif board[2] == board[4] == board[6] and board[2] != " ":
        winner = board[2]
        return True
    
def check_tie(board):
    global game_running
    if " " not in board:
        print_board(board)
        print("The game was a tie!")
        print("*****GAME-OVER*****")
        game_running = False

def check_win(board):
    global game_running
    if check_diagonal(board) or check_horizontal(board) or check_vertical(board):
        print(f"The winner is player {winner}!")
        print("*****GAME-OVER*****")
        game_running = False

#Switch the player
def switch_player():
    global current_player
    if current_player == X:
        current_player = O
    else:
        current_player = X

#Call to main function "if" statment for testing purposes.
if __name__ == "__main__":
    main()