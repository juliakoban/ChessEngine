from abc import ABC, abstractclassmethod

# PIECES IN UNICODE
WHITE_KING = "\u265A"
WHITE_QUEEN = "\u265B"
WHITE_ROOK = "\u265C"
WHITE_BISHOP = "\u265D"
WHITE_KNIGHT = "\u265E"
WHITE_PAWN = "\u265F"

BLACK_KING = "\u2654"
BLACK_QUEEN = "\u2655"
BLACK_ROOK = "\u2656"
BLACK_BISHOP = "\u2657"
BLACK_KNIGHT = "\u2658"
BLACK_PAWN = "\u2659"

# TILE IN UNICODE
TILE = "\u25FB"


# abstract class
class Piece(ABC):
    def __init__(self, color="black"):
        self._color = color

    @property
    def color(self):
        return self._color

    @abstractclassmethod
    def __str__(self):
        pass

    @abstractclassmethod
    def generate_legal_moves(self, row, col):
        pass

    @abstractclassmethod
    def validate_move(self, moves, row, col):
        pass


class Tile(Piece):
    def __str__(self):
        return TILE

    def generate_legal_moves(self, row, col):
        pass

    def validate_move(self, moves, row, col):
        pass


class Pawn(Piece):
    def __str__(self):
        if self.color == "white":
            return WHITE_PAWN
        return BLACK_PAWN

    def generate_legal_moves(self, row, col):
        # first move row -2
        # attack one diagonal
        if self._color == "white":
            return [[row - 1, col]]
        return [[row + 1, col]]
    
    def validate_move(self, moves, row, col):
        if [row, col] not in moves:
            print("Invalid move")
            return False
        return True


class Rook(Piece):
    def __str__(self):
        if self.color == "white":
            return WHITE_ROOK
        return BLACK_ROOK

    def generate_legal_moves(self, row, col):
        moves = []
        for _ in range(8):
            moves.append([row, col + _ + 1])  # right
            moves.append([row, col - _ - 1])  # left
            moves.append([row + _ + 1, col])  # down
            moves.append([row - _ - 1, col])  # up
        return moves
    
    def validate_move(self, moves, row, col):
        if [row, col] not in moves:
            print("Invalid move")
            return False
        return True


class Knight(Piece):
    def __str__(self):
        if self.color == "white":
            return WHITE_KNIGHT
        return BLACK_KNIGHT

    def generate_legal_moves(self, row, col):
        return [
            [row + 2, col + 1],
            [row - 2, col + 1],
            [row + 1, col + 2],
            [row - 1, col + 2],
            [row + 2, col - 1],
            [row - 2, col - 1],
            [row + 1, col - 2],
            [row - 1, col - 2],
        ]
    
    def validate_move(self, moves, row, col):
        if [row, col] not in moves:
            print("Invalid move")
            return False
        return True


class Bishop(Piece):
    def __str__(self):
        if self.color == "white":
            return WHITE_BISHOP
        return BLACK_BISHOP

    def generate_legal_moves(self, row, col):
        moves = []
        for _ in range(8):
            moves.append([row - _ - 1, col + _ + 1])  # up right diagonal
            moves.append([row - _ - 1, col - _ - 1])  # up left diagonal
            moves.append([row + _ + 1, col - _ - 1])  # down left diagonal
            moves.append([row + _ + 1, col + _ + 1])  # down right diagonal
        return moves
    
    def validate_move(self, moves, row, col):
        if [row, col] not in moves:
            print("Invalid move")
            return False
        return True


class King(Piece):
    def __str__(self):
        if self.color == "white":
            return WHITE_KING
        return BLACK_KING

    def generate_legal_moves(self, row, col):
        return [
            [row - 1, col + 1],  # up right diagonal
            [row - 1, col - 1],  # up left diagonal
            [row + 1, col - 1],  # down left diagonal
            [row + 1, col + 1],  # down right diagonal
            [row - 1, col],  # up
            [row + 1, col],  # down
            [row, col - 1],  # left
            [row, col + 1],  # right
        ]
    
    def validate_move(self, moves, row, col):
        if [row, col] not in moves:
            print("Invalid move")
            return False
        return True


class Queen(Piece):
    def __str__(self):
        if self.color == "white":
            return WHITE_QUEEN
        return BLACK_QUEEN

    def generate_legal_moves(self, row, col):
        moves = []
        for _ in range(8):
            moves.append([row - _ - 1, col + _ + 1])  # up right diagonal
            moves.append([row - _ - 1, col - _ - 1])  # up left diagonal
            moves.append([row + _ + 1, col - _ - 1])  # down left diagonal
            moves.append([row + _ + 1, col + _ + 1])  # down right diagonal
            moves.append([row, col + _ + 1])  # right
            moves.append([row, col - _ - 1])  # left
            moves.append([row + _ + 1, col])  # down
            moves.append([row - _ - 1, col])  # up
        return moves
    
    def validate_move(self, moves, row, col):
        if [row, col] not in moves:
            print("Invalid move")
            return False
        return True
