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
        end_input = input("Enter your end (e.g. B1C3): ").strip()
        if is_valid_format(end_input):
            return end_input
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


def start_from_input(input):
    return [8 - int(input[1]), letter_to_number(input[0])]


def end_from_input(input):
    return [8 - int(input[3]), letter_to_number(input[2])]

# 8x8 board
class Board:
    def __init__(self):
        self.board = [
            [
                piece.Rook("black"),
                piece.Knight("black"),
                piece.Bishop("black"),
                piece.Queen("black"),
                piece.King("black"),
                piece.Bishop("black"),
                piece.Knight("black"),  
                piece.Rook("black"),
            ],
            [piece.Pawn("black") for _ in range(8)],
            [piece.Tile() for _ in range(8)],
            [piece.Tile() for _ in range(8)],
            [piece.Tile() for _ in range(8)],
            [piece.Tile() for _ in range(8)],
            [piece.Pawn("white") for _ in range(8)],
            [
                piece.Rook("white"),
                piece.Knight("white"),
                piece.Bishop("white"),
                piece.Queen("white"),
                piece.King("white"),
                piece.Bishop("white"),
                piece.Knight("white"),
                piece.Rook("white"),
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

            start = start_from_input(input)
            end = end_from_input(input)
        
            current_piece = self.board[start[0]][start[1]]
            
            legal_moves = self.board[start[0]][start[1]].generate_legal_moves(start[0], start[1])
            moves_between = current_piece.moves_in_between(start, end, legal_moves)
            is_move_in_moves = current_piece.validate_move(legal_moves, end[0], end[1])

            #print(start[0], start[1], legal_moves)
            print(current_piece.moves_in_between(start, end, legal_moves))

            is_valid_color = False
            is_valid = True
           
            if(self.board[end[0]][end[1]].color != turn):
                is_valid_color = True

            for move in moves_between:
                    if(self.board[move[0]][move[1]].color != "none"):
                        is_valid = False

            if current_piece.color == turn and is_move_in_moves and is_valid_color and is_valid:
                # make this as a swap function?
                self.board[end[0]][end[1]] = self.board[start[0]][start[1]]
                self.board[start[0]][start[1]] = piece.Tile()
                break
