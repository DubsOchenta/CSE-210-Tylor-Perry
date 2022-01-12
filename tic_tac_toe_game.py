"""========================================================================================
Author(s): Tylor Perry (per11034@byui.edu)
Created: 01/10/2022
File: tic-tac-toe-game.py
==========================================================================================="""
from termcolor import colored

create_board = {'7': ' ' , '8': ' ' , '9': ' ' ,
        '4': ' ' , '5': ' ' , '6': ' ' ,
        '1': ' ' , '2': ' ' , '3': ' ' }
board_keys = []
for key in create_board:
    board_keys.append(key)

#Main Function
def main():
    X = colored("X", "blue", attrs=["bold"])
    O = colored("O", "red", attrs=["bold"])
    turn = X
    count = 0
    example_board(X,O)
    for i in range(10):
        print()
        display_board(create_board)
        print()
        move = input(f"It's your turn, {turn}. What is your move? ")        

        if create_board[move] == ' ':
            create_board[move] = turn
            count += 1
        else:
            error_message = colored("That place is already filled, try again.", "cyan", attrs=["bold"])
            print(error_message)
            continue

        # For every move over 5 moves the program will check for a win. 
        if count >= 5:
            if create_board['7'] == create_board['8'] == create_board['9'] != ' ': # across the top
                display_board(create_board)
                print("\nGame Over.\n")                
                print(f"**** Player {turn} won. ****")                
                break
            elif create_board['4'] == create_board['5'] == create_board['6'] != ' ': # across the middle
                display_board(create_board)
                print("\nGame Over.\n")                
                print(f"**** Player {turn} won. ****")
                break
            elif create_board['1'] == create_board['2'] == create_board['3'] != ' ': # across the bottom
                display_board(create_board)
                print("\nGame Over.\n")                
                print(f"**** Player {turn} won. ****")
                break
            elif create_board['1'] == create_board['4'] == create_board['7'] != ' ': # down the left side
                display_board(create_board)
                print("\nGame Over.\n")                
                print(f"**** Player {turn} won. ****")
                break
            elif create_board['2'] == create_board['5'] == create_board['8'] != ' ': # down the middle
                display_board(create_board)
                print("\nGame Over.\n")                
                print(f"**** Player {turn} won. ****")                
                break
            elif create_board['3'] == create_board['6'] == create_board['9'] != ' ': # down the right side
                display_board(create_board)
                print("\nGame Over.\n")                
                print(f"**** Player {turn} won. ****")
                break 
            elif create_board['7'] == create_board['5'] == create_board['3'] != ' ': # diagonal
                display_board(create_board)
                print("\nGame Over.\n")                
                print(f"**** Player {turn} won. ****")
                break
            elif create_board['1'] == create_board['5'] == create_board['9'] != ' ': # diagonal
                display_board(create_board)
                print("\nGame Over.\n")                
                print(f"**** Player {turn} won. ****")
                break 

        # If neither X nor O wins and the board is full, we'll declare the result as 'tie'.
        if count >= 9:
            print("\nGame Over.\n")                
            tie = colored("It's a Tie!!!", "magenta", attrs=["bold"])
            print(tie)
            break
        # How to change the player after every move.
        if turn == X:
            turn = O
        else:
            turn = X

def display_board(board):
    print(f"{board['7']}|{board['8']}|{board['9']}")
    print('-+-+-')
    print(f"{board['4']}|{board['5']}|{board['6']}")
    print('-+-+-')
    print(f"{board['1']}|{board['2']}|{board['3']}")

def example_board(X,O):
    print("\n7|8|9")
    print("-+-+-")
    print("4|5|6")
    print("-+-+-")
    print("1|2|3\n")
    print(f"Best played on a Number Pad.\n(Spots you choose to place {X} and {O} match how the example looks.)")
#Call to main function "if" statment for testing purposes.
if __name__ == "__main__":
    main()