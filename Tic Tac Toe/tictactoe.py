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



if __name__ == "__main__":
    main()