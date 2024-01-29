#!/usr/bin/python3
import sys
"""Function to print the result in the specified format"""


def print_result(board):
    res = []
    for i in range(len(board)):
        res.append([i, board[i]])
    print(res)


def is_valid(board, current_queen):
    """Function to check if the current queen placement is valid"""

    for queen in range(current_queen):
        if (board[queen] == board[current_queen] or
                board[queen] - queen == board[current_queen] - current_queen or
                board[queen] + queen == board[current_queen] + current_queen):
            return False
    return True


# Recursive function to place queens on the board

def place_queens(board, n, current_queen):
    if current_queen == n:
        print_result(board)
        return

    for column in range(n):
        board[current_queen] = column
        if is_valid(board, current_queen):
            place_queens(board, n, current_queen + 1)


def check_args():
    if len(sys.argv) != 2:
        print("Usage: nqueens N")
        exit(1)
    if not (sys.argv[1]).isdigit():
        print("N must be a number")
        exit(1)
    n = int(sys.argv[1])
    if n < 4:
        print("N must be at least 4")
        exit(1)


if __name__ == "__main__":
    check_args()
    n = int(sys.argv[1])
    board = [-1 for _ in range(n)]
    place_queens(board, n, 0)
