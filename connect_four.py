"""
PURPOSE: Creates Connect 4 game and it's played through the Terminal.
"""

import sys

import numpy as np
import random as rand


# NOTE: Logic is set up to only work with board ROWS=6 and COLUMNS=7
ROWS = 6
COLUMNS = 7


def create_board() -> np.array:
    board = np.zeros((ROWS, COLUMNS))
    return board


def see_board(board: np.array) -> None:
    print(np.flip(board, axis=0))


def check_move(board: np.array, col: int) -> bool:
    if 0 <= col - 1 <= COLUMNS:
        if 0 in board[:, col - 1]:
            return True


def place_disc(board: np.array, col: int, disc: int) -> None:
    for _ in range(0, ROWS):
        if board[_, col - 1] == 0:
            board[_, col - 1] = disc
            break


def check_win(board: np.array, disc: int) -> bool:
    """
    Check the board to see if anyone won.

    Args:
        board (np.array): up-to-date game board
        disc (int): Integer determining what player the disc belongs to

    Returns:
        pd.Series: Boolean if someone won or not (True/False)
    """

    # horizontal checks
    for c in range(COLUMNS - 3):
        for r in range(ROWS):
            if (
                (board[r][c] == disc)
                & (board[r][c + 1] == disc)
                & (board[r][c + 2] == disc)
                & (board[r][c + 3] == disc)
            ):
                return True

    # vertical checks
    for c in range(COLUMNS):
        for r in range(ROWS - 3):
            if (
                (board[r][c] == disc)
                & (board[r + 1][c] == disc)
                & (board[r + 2][c] == disc)
                & (board[r + 3][c] == disc)
            ):
                return True

    # up diagonal checks
    for c in range(COLUMNS - 3):
        for r in range(ROWS - 3):
            if (
                (board[r][c] == disc)
                & (board[r + 1][c + 1] == disc)
                & (board[r + 2][c + 2] == disc)
                & (board[r + 3][c + 3] == disc)
            ):
                return True

    # down diagonal checks
    for c in range(COLUMNS - 3):
        for r in range(3, ROWS):
            if (
                (board[r][c] == disc)
                & (board[r - 1][c + 1] == disc)
                & (board[r - 2][c + 2] == disc)
                & (board[r - 3][c + 3] == disc)
            ):
                return True


def play_game() -> None:
    """
    Creates the board and starts the game.
    """

    board = create_board()

    # determines if game continues or ends
    game_ends = False

    # helps determine if all spaces on board are taken up
    total_moves = 0

    # picks player to start
    p_turn = rand.randint(1, 2)
    print(
        f"Starting Game. Player {p_turn} will start the game."
        + " Type STOP to end the game."
    )

    while not game_ends:
        if total_moves == (ROWS * COLUMNS):
            print("Tie game!")
            break
        else:
            see_board(board)

            valid_move = False
            while valid_move is False:
                p_move = 0
                # player move has to fall within one of the valid column #s
                while p_move not in list(range(1, COLUMNS + 1)):
                    p_move = input(
                        f"Player {p_turn}"
                        + " must make a move (valid moves are column"
                        + f" #s between 1 and {COLUMNS}):"
                    )

                    try:
                        p_move = int(p_move)
                        if 1 <= p_move <= COLUMNS:
                            break

                    except ValueError:
                        if p_move.upper() == "STOP":
                            print("Game ended by user.")
                            sys.exit()
                        else:
                            continue

                valid_move = check_move(board, col=p_move)

            place_disc(board, col=p_move, disc=p_turn)

            if check_win(board, disc=p_turn):
                print(f"Player {p_turn} wins!")
                break

            # change player for next iteration
            if p_turn == 1:
                p_turn = 2
            else:
                p_turn = 1

            total_moves = +1

    see_board(board)

    sys.exit()


if __name__ == "__main__":
    play_game()
