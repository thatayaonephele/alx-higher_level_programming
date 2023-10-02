#!/usr/bin/python3
'''A module that defines the N Queens'''


def isSafe(board, r, col):
    """A function that verifies if pos is safe from att.
    """
    for c_var in range(col):
        if abs(board[c_var] - r) is abs(c_var - col) or board[c_var] is r:
            return False
    return True


def checkBoard(board, col):
    '''A function that uses backtracking for colunm verrification.
    '''
    n = len(board)
    if col is n:
        print(str([[c_var, board[c_var]] for c_var in range(n)]))
        return

    for r in range(n):
        if isSafe(board, r, col):
            board[col] = r
            checkBoard(board, col + 1)


if __name__ == "__main__":
    from sys import exit as e, argv as av

    x = len(sys.av)
    if x != 2:
        print("Usage: nqueens N")
        sys.e(1)
    n = 0
    try:
        n = int(sys.av[1])
    except ValueError:
        print("N must be a number")
        sys.e(1)
    if n < 4:
        print("N must be at least 4")
        sys.e(1)
    board = [0 for col in range(n)]
    checkBoard(board, 0)
