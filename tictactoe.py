import random

# Make board with dashes
board = ["-"] * 9

# Show the board nicely
def show():
    print(board[0], "|", board[1], "|", board[2])
    print(board[3], "|", board[4], "|", board[5])
    print(board[6], "|", board[7], "|", board[8])

# Check for winner
def check_winner(symbol):
    wins = [
        [0,1,2], [3,4,5], [6,7,8],  # rows
        [0,3,6], [1,4,7], [2,5,8],  # columns
        [0,4,8], [2,4,6]            # diagonals
    ]
    for line in wins:
        if board[line[0]] == board[line[1]] == board[line[2]] == symbol:
            return True
        else: False

# Player move
def player_turn():
    while True:
        move = input("Choose 1-9: ")
        pos = int(move) - 1
        if board[pos] == "-":
                board[pos] = "X"
                break
        else:
                print("Taken spot.")
    

# Computer move
def computer_turn():
    print("Computer's turn:")
    empty = [i for i in range(9) if board[i] == "-"]
    pos = random.choice(empty)
    board[pos] = "O"

# Play the game
def play():
    show()
    for turn in range(9):
        if turn % 2 == 0:
            player_turn()
        else:
            computer_turn()
        show()

        if check_winner("X"):
            print("You win!")
            return
        elif check_winner("O"):
            print("Computer wins!")
            return

    print("It's a tie!")

play()
