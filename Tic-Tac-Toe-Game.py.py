import random


# GAME BOARD

board = [" ", " ", " ",
         " ", " ", " ",
         " ", " ", " "]


# DISPLAY BOARD

def display_board():
    print()
    print(" " + board[0] + " | " + board[1] + " | " + board[2])
    print("---+---+---")
    print(" " + board[3] + " | " + board[4] + " | " + board[5])
    print("---+---+---")
    print(" " + board[6] + " | " + board[7] + " | " + board[8])
    print()


# DISPLAY POSITION GUIDE

def display_positions():
    print()
    print(" 1 | 2 | 3")
    print("---+---+---")
    print(" 4 | 5 | 6")
    print("---+---+---")
    print(" 7 | 8 | 9")
    print()


# CHECK WINNER

def check_winner(symbol):
    winning_combinations = [
        [0, 1, 2],
        [3, 4, 5],
        [6, 7, 8],
        [0, 3, 6],
        [1, 4, 7],
        [2, 5, 8],
        [0, 4, 8],
        [2, 4, 6]
    ]

    for combination in winning_combinations:
        if (board[combination[0]] == symbol and
                board[combination[1]] == symbol and
                board[combination[2]] == symbol):
            return True

    return False


# CHECK DRAW

def check_draw():
    return " " not in board


# RESET BOARD

def reset_board():
    global board

    board = [" ", " ", " ",
             " ", " ", " ",
             " ", " ", " "]


# PLAYER MOVE

def player_move(player_name, symbol):
    while True:
        try:
            position = int(
                input(f"{player_name} ({symbol}), choose a position (1-9): ")
            )

            position -= 1

            if position < 0 or position > 8:
                print("Please choose a number between 1 and 9.")
                continue

            if board[position] != " ":
                print("That position is already taken.")
                continue

            board[position] = symbol
            break

        except ValueError:
            print("Please enter a valid number.")


# COMPUTER MOVE

def computer_move():
    empty_positions = []

    for i in range(len(board)):
        if board[i] == " ":
            empty_positions.append(i)

    position = random.choice(empty_positions)
    board[position] = "O"

    print(f"Computer chose position {position + 1}")


# TWO PLAYER GAME

def two_player_game(player1, player2, scores):
    current_player = player1
    current_symbol = "X"

    while True:
        display_board()

        if current_symbol == "X":
            player_move(player1, "X")
        else:
            player_move(player2, "O")

        if check_winner(current_symbol):
            display_board()
            print(f"🎉 {current_player} wins!")

            scores[current_player] += 1
            break

        if check_draw():
            display_board()
            print("🤝 It's a draw!")
            break

        if current_symbol == "X":
            current_symbol = "O"
            current_player = player2
        else:
            current_symbol = "X"
            current_player = player1


# SINGLE PLAYER GAME

def single_player_game(player_name, scores):
    current_symbol = "X"

    while True:
        display_board()

        if current_symbol == "X":
            player_move(player_name, "X")
        else:
            computer_move()

        if check_winner(current_symbol):
            display_board()

            if current_symbol == "X":
                print(f"🎉 {player_name} wins!")
                scores[player_name] += 1
            else:
                print("🤖 Computer wins!")
                scores["Computer"] += 1

            break

        if check_draw():
            display_board()
            print("🤝 It's a draw!")
            break

        if current_symbol == "X":
            current_symbol = "O"
        else:
            current_symbol = "X"


# DISPLAY SCOREBOARD

def display_scoreboard(scores):
    print("\n🏆 SCOREBOARD")
    print("----------------")

    for player, score in scores.items():
        print(f"{player}: {score}")

    print("----------------")


# MAIN PROGRAM

print("================================")
print("       TIC-TAC-TOE GAME")
print("================================")

print("\nChoose Game Mode:")
print("1. Single Player")
print("2. Two Players")

while True:
    mode = input("\nEnter 1 or 2: ")

    if mode in ["1", "2"]:
        break

    print("Please enter 1 or 2.")


# SINGLE PLAYER SETUP

if mode == "1":
    player_name = input("\nEnter your name: ")

    scores = {
        player_name: 0,
        "Computer": 0
    }

    while True:
        reset_board()
        display_positions()

        single_player_game(player_name, scores)

        display_scoreboard(scores)

        play_again = input(
            "\nDo you want to play again? (yes/no): "
        ).lower()

        if play_again not in ["yes", "y"]:
            break


# TWO PLAYER SETUP

else:
    player1 = input("\nEnter Player 1 name: ")
    player2 = input("Enter Player 2 name: ")

    scores = {
        player1: 0,
        player2: 0
    }

    while True:
        reset_board()
        display_positions()

        two_player_game(player1, player2, scores)

        display_scoreboard(scores)

        play_again = input(
            "\nDo you want to play again? (yes/no): "
        ).lower()

        if play_again not in ["yes", "y"]:
            break


# GAME END

print("\n================================")
print("          FINAL SCORE")
print("================================")

display_scoreboard(scores)

print("\nThanks for playing! 🎮")