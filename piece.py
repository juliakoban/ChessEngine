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
    def __init__(self, color="none"):
        self._color = color

    @property
    def color(self):
        return self._color

    @abstractclassmethod
    def __str__(self):
        pass

    @abstractclassmethod
    # legal in terms of chess rules
    def generate_legal_moves(self, row, col):
        pass

    @abstractclassmethod
    def moves_in_between(self, start, end, moves):
        pass
 
    def validate_move(self, moves, row, col):
        if [row, col] not in moves:
            print("Invalid move")
            return False
        return True


class Tile(Piece):
    def __str__(self):
        return TILE

    def generate_legal_moves(self, row, col):
        pass
    def moves_in_between(self, start, end, moves):
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
    
    def moves_in_between(self, start, end, moves):
        return []


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
    
    def moves_in_between(self, start, end, moves):
        between = []
        row_diff = end[0] - start[0]
        col_diff = end[1] - start[1]
        
        for move in moves:
            if (col_diff == 0): # horizontal move
                if (row_diff > 0): 
                    if (move[0] > start[0] and move[0] < end[0]): # down
                        between.append(move)
                if (move[0] < start[0] and move[0] > end[0]): # up
                        between.append(move)
            elif (row_diff == 0): # vertical move
                if (col_diff < 0): 
                    if (move[1] < start[1] and move[1] > end[1]): # left
                        between.append(move)
                if (move[1] > start[1] and move[1] < end[1]): # right
                        between.append(move)

        
        return between


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
    
    def moves_in_between(self, start, end, moves):
        return []


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
    
    def moves_in_between(self, start, end, moves):
        between = []
        row_diff = end[0] - start[0]
        col_diff = end[1] - start[1]
        
        for move in moves:
            if (col_diff > 0): 
                if (row_diff > 0): 
                    if (move[0] > start[0] and move[0] < end[0] and move[1] > start[1] and move[1] < end[1]): # right down
                        between.append(move)
                if (move[0] < start[0] and move[0] > end[0] and move[1] > start[1] and move[1] < end[1]): # right up
                        between.append(move)
            elif (col_diff < 0): 
                if (row_diff < 0): 
                    if (move[1] < start[1] and move[1] > end[1] and move[0] < start[0] and move[0] > end[0]): # left up
                        between.append(move)
                if (move[1] < start[1] and move[1] > end[1] and move[0] > start[0] and move[0] < end[0]): #left down
                        between.append(move)

        return between


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
    
    def moves_in_between(self, start, end, moves):
        return []


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
    
    def moves_in_between(self, start, end, moves):
        between = []
        row_diff = end[0] - start[0]
        col_diff = end[1] - start[1]

        for move in moves:
            if (col_diff >= 0): 
                if (row_diff > 0): 
                    if (move[0] > start[0] and move[0] < end[0] and move[1] >= start[1] and move[1] <= end[1]): # right down
                        between.append(move)
                if (move[0] < start[0] and move[0] > end[0] and move[1] >= start[1] and move[1] <= end[1]): # right up
                        between.append(move)
            elif (col_diff < 0): 
                if (row_diff < 0): 
                    if (move[1] < start[1] and move[1] > end[1] and move[0] < start[0] and move[0] > end[0]): # left up
                        between.append(move)
                if (move[1] < start[1] and move[1] > end[1] and move[0] > start[0] and move[0] < end[0]): #left down
                        between.append(move)
            

        return between
