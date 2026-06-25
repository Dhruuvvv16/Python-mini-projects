import math

EMPTY = " "


def print_board(board):
    print()
    for i in range(0, 9, 3):
        row = board[i:i + 3]
        print(" | ".join(row))
        if i < 6:
            print("--+---+--")
    print()


def winner(board):
    lines = [
        (0, 1, 2), (3, 4, 5), (6, 7, 8),  # rows
        (0, 3, 6), (1, 4, 7), (2, 5, 8),  # columns
        (0, 4, 8), (2, 4, 6),             # diagonals
    ]
    for a, b, c in lines:
        if board[a] != EMPTY and board[a] == board[b] == board[c]:
            return board[a]
    return None


def is_full(board):
    return EMPTY not in board


def minimax(board, current_player, ai_player, human_player):
    win = winner(board)
    if win == ai_player:
        return 1
    if win == human_player:
        return -1
    if is_full(board):
        return 0

if __name__ == "__main__":
    main()