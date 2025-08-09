import random
from colorama import Fore, Style, init

init(autoreset = True)

def display_board(board):
    colored_board = []
    for cell in board:
        if cell == "X":
            colored_board.append(Fore.RED + "X" + Style.RESET_ALL)
        elif cell == "O":
            colored_board.append(Fore.CYAN + "O" + Style.RESET_ALL)
        else:
            colored_board.append(cell)

    print (colored_board[0] + " | " + colored_board[1] + " | " + colored_board[2])
    print("---------")
    print(colored_board[3] + " | " + colored_board[4] + " | " + colored_board[5])
    print("---------")
    print(colored_board[6] + " | " + colored_board[7] + " | " + colored_board[8])

def check_winner(board, player):
    win_positions = [
        [0,1,2], [3,4,5], [6,7,8],
        [0,3,6], [1,4,7], [2,5,8],
        [0,4,8], [2,4,6]
    ]
    return any (all (board [i] == player for i in pos) for pos in win_positions)
    
def computer_move(board):
    available_moves = [i for i, cell in enumerate(board) if cell == " "]
    return random.choice(available_moves)

def tic_tac_toe():
        board =[" "] * 9
        current_player = "X"

        for turn in range(9):
            display_board(board)

            if current_player == "X":
                while True:
                    try:
                        move = int(input(Fore.YELLOW + "Your move (1-9):" + Style.RESET_ALL)) - 1
                    except ValueError:
                        print('\n' + Fore.RED + "Invalid input! Enter a number 1-9.")
                        continue

                    if move < 0 or move > 8 or board[move] != " ":
                        print('\n' + Fore.RED + "Invalid move! Try again.")
                        continue
                    break
            else:
                move = computer_move(board)
                print('\n' + Fore.GREEN + f"Computer chooses position {move+1}")

            board[move] = current_player
            if check_winner(board, current_player):
                display_board(board)
                if current_player == "X":
                    print('\n' + Fore.GREEN + "You win!")
                else:
                    print('\n' + Fore.RED + "Computer wins!")
                return

            current_player = "O" if current_player == "X" else "X"

        display_board(board)
        print('\n' + Fore.MAGENTA + "It's a draw!")

tic_tac_toe()