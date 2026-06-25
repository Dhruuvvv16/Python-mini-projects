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

    scores = []
    for i in range(9):
        if board[i] == EMPTY:
            board[i] = current_player
            next_player = human_player if current_player == ai_player else ai_player
            scores.append(minimax(board, next_player, ai_player, human_player))
            board[i] = EMPTY

    if current_player == ai_player:
        return max(scores)
    return min(scores)


def best_move(board, ai_player, human_player):
    best_score = -math.inf
    move = None
    for i in range(9):
        if board[i] == EMPTY:
            board[i] = ai_player
            score = minimax(board, human_player, ai_player, human_player)
            board[i] = EMPTY
            if score > best_score:
                best_score = score
                move = i
    return move

if __name__ == "__main__":
    main()