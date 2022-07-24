#!/usr/bin/python3
import sys


def print_board(board, n):
    """prints allocated positions to the queen"""
    b = []

    for i in range(n):
        for j in range(n):
            if j == board[i]:
                b.append([i, j])
    print(b)


def safe_position(board, i, j, r):
    """Determines whether the position is safe for the queen"""
    if (board[i] == j) or (board[i] == j - i + r) or (board[i] == i - r + j):
        return True
    return False


def determine_positions(board, row, n):
    """Recursively finds all safe positions where the queen can be allocated"""
    if row == n:
        print_board(board, n)

    else:
        for j in range(n):
            allowed = True
            for i in range(row):
                if safe_position(board, i, j, row):
                    allowed = False
            if allowed:
                board[row] = j
                determine_positions(board, row + 1, n)


def create_board(size):
    """Generates the board"""
    return [0 * size for i in range(size)]


if len(sys.argv) != 2:
    print("Usage: nqueens N")
    exit(1)

try:
    n = int(sys.argv[1])
except BaseException:
    print("N must be a number")
    exit(1)

if (n < 4):
    print("N must be at least 4")
    exit(1)

board = create_board(int(n))
row = 0
determine_positions(board, row, int(n))


if __name__ == '__main__':
    print('nqueens: N = 4:')
    determine_positions(8, 0, 4)
    print('nqueens: N = 6:')
    determine_positions(8, 0, 6)
