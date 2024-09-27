#!/usr/bin/python3
"""Solves the N-queens puzzle challenge.

This program finds all valid ways to place N queens
on an NxN chessboard without threatening each other.

Usage example:
    $ ./101-nqueens.py N

N should be an integer, and it needs to be at least 4.

Variables:
    b (list): A list representing the chessboard.
    results (list): A list of valid board configurations.

Each result is a list of [x_axis, y_axis] positions where queens are placed.
"""
import sys


def create_board(n):
    """Create an `n`x`n` chessboard filled with spaces."""
    board = []
    pos = 0
    while pos < n:
        board.append([])
        pos = pos + 1
    pos = 0
    while pos < n:
        cnt = 0
        while cnt < n:
            board[pos].append(' ')
            cnt = cnt + 1
        pos = pos + 1
    return board


def tmp_board_cpy(board):
    """Make a copy of the current chessboard."""
    if type(board) == list:
        return [tmp_board_cpy(item) for item in board]
    return board


def est_sol(board):
    """Generate a list of the queen positions for a solution."""
    solution = []
    pos = 0
    while pos < len(board):
        cnt = 0
        while cnt < len(board):
            if board[pos][cnt] == "Q":
                solution.append([pos, cnt])
                break
            cnt = cnt + 1
        pos = pos + 1
    return solution


def output_result(board, x_axis, y_axis):
    """Mark spots on the board that are invalid for further queens.

    Updates the board to mark where future queens
    cannot be placed due to conflicts.

    Args:
        board (list): The current board state.
        x_axis (int): The x-axis (row) where the queen was placed.
        y_axis (int): The y-axis (column) where the queen was placed.
    """
    # Mark all spots forward in the row
    cnt = y_axis + 1
    while cnt < len(board):
        board[x_axis][cnt] = "x"
        cnt = cnt + 1
    # Mark all spots backward in the row
    cnt = y_axis - 1
    while cnt >= 0:
        board[x_axis][cnt] = "x"
        cnt = cnt - 1
    # Mark all spots below in the column
    pos = x_axis + 1
    while pos < len(board):
        board[pos][y_axis] = "x"
        pos = pos + 1
    # Mark all spots above in the column
    pos = x_axis - 1
    while pos >= 0:
        board[pos][y_axis] = "x"
        pos = pos - 1
    # Mark diagonal down-right
    cnt = y_axis + 1
    pos = x_axis + 1
    while pos < len(board) and cnt < len(board):
        board[pos][cnt] = "x"
        pos = pos + 1
        cnt = cnt + 1
    # Mark diagonal up-left
    cnt = y_axis - 1
    pos = x_axis - 1
    while pos >= 0 and cnt >= 0:
        board[pos][cnt] = "x"
        pos = pos - 1
        cnt = cnt - 1
    # Mark diagonal up-right
    cnt = y_axis + 1
    pos = x_axis - 1
    while pos >= 0 and cnt < len(board):
        board[pos][cnt] = "x"
        pos = pos - 1
        cnt = cnt + 1
    # Mark diagonal down-left
    cnt = y_axis - 1
    pos = x_axis + 1
    while pos < len(board) and cnt >= 0:
        board[pos][cnt] = "x"
        pos = pos + 1
        cnt = cnt - 1


def recurs_sol(board, x_axis, queens, results):
    """Recursively solve the N-queens problem.

    Args:
        board (list): The current board state.
        x_axis (int): The x_axis we're placing a queen in.
        queens (int): The current number of queens placed.
        results (list): The list storing all valid solutions.
    
    Returns:
        The list of all valid solutions.
    """
    if queens == len(board):
        results.append(est_sol(board))
        return results

    cnt = 0
    while cnt < len(board):
        if board[x_axis][cnt] == " ":
            temp_board = tmp_board_cpy(board)
            temp_board[x_axis][cnt] = "Q"
            output_result(temp_board, x_axis, cnt)
            results = recurs_sol(temp_board, x_axis + 1, queens + 1, results)
        cnt = cnt + 1

    return results


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: nqueens N")
        sys.exit(1)
    if not sys.argv[1].isdigit():
        print("N must be a number")
        sys.exit(1)
    if int(sys.argv[1]) < 4:
        print("N must be at least 4")
        sys.exit(1)

    board = create_board(int(sys.argv[1]))
    results = recurs_sol(board, 0, 0, [])
    for ans in results:
        print(ans)
