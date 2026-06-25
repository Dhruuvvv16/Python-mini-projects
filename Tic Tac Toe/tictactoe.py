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


def get_human_move(board):
    while True:
        raw = input("Your move (1-9): ").strip()
        if not raw.isdigit() or not (1 <= int(raw) <= 9):
            print("Enter a number from 1 to 9.")
            continue
        pos = int(raw) - 1
        if board[pos] != EMPTY:
            print("That square is taken, pick another.")
            continue
        return pos


def choose_symbol():
    while True:
        raw = input("Choose your symbol, X or O (X goes first): ").strip().upper()
        if raw in ("X", "O"):
            return raw
        print("Please type X or O.")


def main():
    print("=" * 40)
    print("   TIC-TAC-TOE  (vs unbeatable AI)")
    print("=" * 40)
    print("Squares are numbered 1-9, left to right, top to bottom.\n")

    human = choose_symbol()
    ai = "O" if human == "X" else "X"
    board = [EMPTY] * 9
    turn = "X"  # X always starts

    print_board([str(i + 1) if c == EMPTY else c for i, c in enumerate(board)])

    while True:
        if turn == human:
            pos = get_human_move(board)
            board[pos] = human
        else:
            print("Computer is thinking...")
            pos = best_move(board, ai, human)
            board[pos] = ai

        print_board([str(i + 1) if c == EMPTY else c for i, c in enumerate(board)])

        win = winner(board)
        if win:
            print("You win!" if win == human else "Computer wins!")
            break
        if is_full(board):
            print("It's a tie!")
            break

        turn = "O" if turn == "X" else "X"


if __name__ == "__main__":
    main()