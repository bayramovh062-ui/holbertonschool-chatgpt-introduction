def print_board(board):
    for i, row in enumerate(board):
        print(" | ".join(row))
        if i < 2:
            print("-" * 9)


def check_winner(board):
    # Rows
    for row in board:
        if row[0] == row[1] == row[2] != " ":
            return True

    # Columns
    for col in range(3):
        if board[0][col] == board[1][col] == board[2][col] != " ":
            return True

    # Diagonals
    if board[0][0] == board[1][1] == board[2][2] != " ":
        return True

    if board[0][2] == board[1][1] == board[2][0] != " ":
        return True

    return False


def is_draw(board):
    for row in board:
        if " " in row:
            return False
    return True


def get_valid_input(player, name):
    while True:
        value = input(f"Enter {name} (0, 1, or 2) for player {player}: ")
        try:
            value = int(value)
            if value in [0, 1, 2]:
                return value
            print("Invalid input. Please enter 0, 1, or 2.")
        except ValueError:
            print("Invalid input. Please enter a number.")


def tic_tac_toe():
    board = [[" "] * 3 for _ in range(3)]
    player = "X"

    while True:
        print_board(board)

        row = get_valid_input(player, "row")
        col = get_valid_input(player, "column")

        if board[row][col] != " ":
            print("That spot is already taken! Try again.")
            continue

        board[row][col] = player

        if check_winner(board):
            print_board(board)
            print("Player " + player + " wins!")
            break

        if is_draw(board):
            print_board(board)
            print("It's a draw!")
            break

        player = "O" if player == "X" else "X"


tic_tac_toe()
