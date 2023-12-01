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
    def generate_legal_moves(self, row, col, is_attacking):
        pass

    @abstractclassmethod
    # generate moves between piece's start and supposed end position
    def moves_in_between(self, start, end, moves):
        pass
 
    # checks whether the move that a player wants to make is included in the legal moves list
    def validate_move(self, moves, row, col):
        if [row, col] not in moves:
            print("Invalid move")
            return False
        return True


class Tile(Piece):
    def __str__(self):
        return TILE

    def generate_legal_moves(self, row, col, is_attacking):
        pass
    def moves_in_between(self, start, end, moves):
        pass


class Pawn(Piece):
    def __str__(self):
        if self.color == "white":
            return WHITE_PAWN
        return BLACK_PAWN

    def generate_legal_moves(self, row, col, is_attacking):
        all_moves = []
        moves_on_board =[]

        if self._color == "white":
            if is_attacking:

                all_moves.append([row - 1, col + 1]) # up right 
                all_moves.append([row - 1, col - 1]) # up left

            if (row == 6): # first move for white pawn
                all_moves.append([row - 2, col])
                all_moves.append([row - 1, col])
            else:
                all_moves.append([row - 1, col])
        elif self._color == "black":
            if is_attacking:

                all_moves.append([row + 1, col - 1]) # down left 
                all_moves.append([row + 1, col + 1]) # down right

            if (row == 1): # first move for black pawn
                all_moves.append([row + 2, col])
                all_moves.append([row + 1, col])
            else: all_moves.append([row + 1, col])
    
        for move in all_moves:
            if (move[0] <= 7 and move[0] >= 0 and move[1] >= 0 and move[1] <= 7):
                moves_on_board.append(move)

        return moves_on_board
    
    def moves_in_between(self, start, end, moves):
        between = []
        for move in moves:    
            if (move[0] > start[0] and move[0] < end[0] and move[1] == start[1]): # down
                between.append(move)
            elif (move[0] < start[0] and move[0] > end[0] and move[1] == start[1]): # up
                between.append(move)
        return between


class Rook(Piece):
    def __str__(self):
        if self.color == "white":
            return WHITE_ROOK
        return BLACK_ROOK

    def generate_legal_moves(self, row, col, is_attacking):
        all_moves = []
        moves_on_board =[]

        for _ in range(8):
            all_moves.append([row, col + _ + 1])  # right
            all_moves.append([row, col - _ - 1])  # left
            all_moves.append([row + _ + 1, col])  # down
            all_moves.append([row - _ - 1, col])  # up
        
        for move in all_moves:
            if (move[0] <= 7 and move[0] >= 0 and move[1] >= 0 and move[1] <= 7):
                moves_on_board.append(move)

        return moves_on_board
    
    def validate_move(self, moves, row, col):
        if [row, col] not in moves:
            print("Invalid move")
            return False
        return True
    
    def moves_in_between(self, start, end, moves):
        between = []
        
        for move in moves:
            if (move[0] > start[0] and move[0] < end[0] and move[1] == start[1]): # down
                between.append(move)
            elif (move[0] < start[0] and move[0] > end[0] and move[1] == start[1]): # up
                between.append(move)
            elif (move[0] == start[0] and move[1] < start[1] and move[1] > end[1]): # left
                between.append(move)
            elif (move[0] == start[0] and move[1] > start[1] and move[1] < end[1]): # right
                between.append(move)
        
        return between


class Knight(Piece):
    def __str__(self):
        if self.color == "white":
            return WHITE_KNIGHT
        return BLACK_KNIGHT

    def generate_legal_moves(self, row, col, is_attacking):
        all_moves = []
        moves_on_board = []

        all_moves.append([row + 2, col + 1])
        all_moves.append([row - 2, col + 1])
        all_moves.append([row + 1, col + 2])
        all_moves.append([row - 1, col + 2])
        all_moves.append([row + 2, col - 1])
        all_moves.append([row - 2, col - 1])
        all_moves.append([row + 1, col - 2])
        all_moves.append([row - 1, col - 2])

        for move in all_moves:
            if (move[0] <= 7 and move[0] >= 0 and move[1] >= 0 and move[1] <= 7):
                moves_on_board.append(move)

        return moves_on_board
    
    def moves_in_between(self, start, end, moves):
        return []


class Bishop(Piece):
    def __str__(self):
        if self.color == "white":
            return WHITE_BISHOP
        return BLACK_BISHOP

    def generate_legal_moves(self, row, col, is_attacking):
        all_moves = []
        moves_on_board =[]
        for _ in range(8):
            all_moves.append([row - _ - 1, col + _ + 1])  # up right diagonal
            all_moves.append([row - _ - 1, col - _ - 1])  # up left diagonal
            all_moves.append([row + _ + 1, col - _ - 1])  # down left diagonal
            all_moves.append([row + _ + 1, col + _ + 1])  # down right diagonal

        for move in all_moves:
            if (move[0] <= 7 and move[0] >= 0 and move[1] >= 0 and move[1] <= 7):
                moves_on_board.append(move)

        return moves_on_board
    
    def moves_in_between(self, start, end, moves):
        between = []
        
        for move in moves:
            if (move[0] > start[0] and move[0] < end[0] and move[1] > start[1] and move[1] < end[1]): # right down
                        between.append(move)
            elif (move[0] < start[0] and move[0] > end[0] and move[1] > start[1] and move[1] < end[1]): # right up
                        between.append(move)    
            elif (move[1] < start[1] and move[1] > end[1] and move[0] < start[0] and move[0] > end[0]): # left up
                        between.append(move)            
            elif (move[1] < start[1] and move[1] > end[1] and move[0] > start[0] and move[0] < end[0]): #left down
                        between.append(move)

        return between


class King(Piece):
    def __str__(self):
        if self.color == "white":
            return WHITE_KING
        return BLACK_KING

    def generate_legal_moves(self, row, col, is_attacking):
        all_moves = []
        moves_on_board = []

        all_moves.append([row - 1, col + 1]) # up right diagonal
        all_moves.append([row - 1, col - 1]) # up left diagonal
        all_moves.append([row + 1, col - 1]) # down left diagonal
        all_moves.append([row + 1, col + 1]) # down right diagonal
        all_moves.append([row - 1, col]) # up
        all_moves.append([row + 1, col]) # down
        all_moves.append([row, col - 1]) # left
        all_moves.append([row, col + 1]) # right

        for move in all_moves:
            if (move[0] <= 7 and move[0] >= 0 and move[1] >= 0 and move[1] <= 7):
                moves_on_board.append(move)

        return moves_on_board
    
    def moves_in_between(self, start, end, moves):
        return []


class Queen(Piece):
    def __str__(self):
        if self.color == "white":
            return WHITE_QUEEN
        return BLACK_QUEEN

    def generate_legal_moves(self, row, col, is_attacking):
        all_moves = []
        moves_on_board = []
        for _ in range(8):
            all_moves.append([row - _ - 1, col + _ + 1])  # up right diagonal
            all_moves.append([row - _ - 1, col - _ - 1])  # up left diagonal
            all_moves.append([row + _ + 1, col - _ - 1])  # down left diagonal
            all_moves.append([row + _ + 1, col + _ + 1])  # down right diagonal
            all_moves.append([row, col + _ + 1])  # right
            all_moves.append([row, col - _ - 1])  # left
            all_moves.append([row + _ + 1, col])  # down
            all_moves.append([row - _ - 1, col])  # up

        for move in all_moves:
            if (move[0] <= 7 and move[0] >= 0 and move[1] >= 0 and move[1] <= 7):
                moves_on_board.append(move)

        return moves_on_board
    
    def moves_in_between(self, start, end, moves):
        between = []
        col_diff = end[1] - start[1]
        row_diff = end[0] - start[0]
        direction = ""

        if col_diff == 0:
            direction = "vertical"
        elif row_diff == 0:
            direction = "horizontal"
        else:
            direction = "diagonal"

        for move in moves:
            
            if (move[0] > start[0] and move[0] < end[0] and move[1] > start[1] and move[1] < end[1]): # right down
                between.append(move)
            elif (move[0] < start[0] and move[0] > end[0] and move[1] > start[1] and move[1] < end[1]): # right up
                between.append(move)    
            elif (move[1] < start[1] and move[1] > end[1] and move[0] < start[0] and move[0] > end[0]): # left up
                between.append(move)            
            elif (move[1] < start[1] and move[1] > end[1] and move[0] > start[0] and move[0] < end[0]): #left down
                between.append(move)
            elif (direction == "vertical" and move[0] > start[0] and move[0] < end[0] and move[1] == start[1]): # down
                between.append(move)
            elif (direction == "vertical" and move[0] < start[0] and move[0] > end[0] and move[1] == start[1]): # up
                between.append(move)
            elif (direction == "horizontal" and move[0] == start[0] and move[1] < start[1] and move[1] > end[1]): # left
                between.append(move)
            elif (direction == "horizontal" and move[0] == start[0] and move[1] > start[1] and move[1] < end[1]): # right
                between.append(move)

        return between
