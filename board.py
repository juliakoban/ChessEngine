import piece
import os


def is_valid_format(input):
    # only letters A, ..., H
    # only numbers 1, ..., 8
    # only 4 letter strings
    # make letters capital
    return True


def read():
    while True:
        move_input = input("Enter your move (e.g. B1C3): ").strip()
        if is_valid_format(move_input):
            return move_input
        print("Invalid input")


def letter_to_number(letter):
    match letter:
        case "A":
            return 0
        case "B":
            return 1
        case "C":
            return 2
        case "D":
            return 3
        case "E":
            return 4
        case "F":
            return 5
        case "G":
            return 6
        case "H":
            return 7


def get_pos_from_input(input):
    return [8 - int(input[1]), letter_to_number(input[0])]


def get_move_from_input(input):
    return [8 - int(input[3]), letter_to_number(input[2])]


# 8x8 board
class Board:
    def __init__(self):
        self.board = [
            [
                piece.Rook("b"),
                piece.Knight("b"),
                piece.Bishop("b"),
                piece.Queen("b"),
                piece.King("b"),
                piece.Bishop("b"),
                piece.Knight("b"),
                piece.Rook("b"),
            ],
            [piece.Pawn("b") for _ in range(8)],
            [piece.Tile() for _ in range(8)],
            [piece.Tile() for _ in range(8)],
            [piece.Tile() for _ in range(8)],
            [piece.Tile() for _ in range(8)],
            [piece.Pawn("w") for _ in range(8)],
            [
                piece.Rook("w"),
                piece.Knight("w"),
                piece.Bishop("w"),
                piece.Queen("w"),
                piece.King("w"),
                piece.Bishop("w"),
                piece.Knight("w"),
                piece.Rook("w"),
            ],
        ]

    def display(self):
        for row in range(8):
            print(8 - row, end=" ")
            for column in range(8):
                print(self.board[row][column], end=" ")
            print()
        print("  A B C D E F G H")

    def update(self, turn):
        while True:
            print(f"{turn} to move!")
            input = read()

            current_pos = get_pos_from_input(input)
            move = get_move_from_input(input)

            moves = self.board[current_pos[0]][current_pos[1]].generate_legal_moves(
                current_pos[0], current_pos[1]
            )
            is_valid = self.board[current_pos[0]][current_pos[1]].validate_move(
                moves, move[0], move[1]
            )

            if self.board[current_pos[0]][current_pos[1]].color == turn and is_valid:
                self.board[move[0]][move[1]] = self.board[current_pos[0]][
                    current_pos[1]
                ]
                self.board[current_pos[0]][current_pos[1]] = piece.Tile()
                break
