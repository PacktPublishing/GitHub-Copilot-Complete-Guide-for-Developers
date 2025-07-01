def print_board(board):
    """
    Print the current state of the Tic-Tac-Toe board.
    """
    for row in board:
        print(" | ".join(row))
        print("-" * 9)


def check_winner(board):
    """
    Check if there is a winner or if the game is a draw.

    :param board: The current state of the board
    :return: 'X', 'O' if there is a winner, 'Draw' if it's a draw, or None if the game is ongoing
    """
    # Check rows and columns
    for i in range(3):
        if board[i][0] == board[i][1] == board[i][2] and board[i][0] != " ":
            return board[i][0]
        if board[0][i] == board[1][i] == board[2][i] and board[0][i] != " ":
            return board[0][i]

    # Check diagonals
    if board[0][0] == board[1][1] == board[2][2] and board[0][0] != " ":
        return board[0][0]
    if board[0][2] == board[1][1] == board[2][0] and board[0][2] != " ":
        return board[0][2]

    # Check for a draw
    if all(cell != " " for row in board for cell in row):
        return "Draw"

    return None


def tic_tac_toe():
    """
    Main function to play Tic-Tac-Toe.
    """
    board = [[" " for _ in range(3)] for _ in range(3)]
    current_player = "X"

    print("Welcome to Tic-Tac-Toe!")
    print_board(board)

    while True:
        print(f"\nPlayer {current_player}'s turn.")
        try:
            row = int(input("Enter the row (0, 1, 2): "))
            col = int(input("Enter the column (0, 1, 2): "))

            if board[row][col] != " ":
                print("Cell is already occupied. Try again.")
                continue

            board[row][col] = current_player
            print_board(board)

            winner = check_winner(board)
            if winner:
                if winner == "Draw":
                    print("It's a draw!")
                else:
                    print(f"Player {winner} wins!")
                break

            # Switch player
            current_player = "O" if current_player == "X" else "X"

        except (ValueError, IndexError):
            print("Invalid input. Please enter a valid row and column (0, 1, 2).")


if __name__ == "__main__":
    tic_tac_toe()