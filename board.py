import piece
import os


def is_valid_format(input):
    # only letters A, ..., H
    # only numbers 1, ..., 8
    # only 4 letter strings
    return True


def read():
    while True:
        end_input = input("enter your move (e.g. B1C3): ").strip()
        if is_valid_format(end_input):
            return end_input
        print("Invalid input format")


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
    return [8 - int(input[1]), letter_to_number(input[0].upper())]


def end_from_input(input):
    return [8 - int(input[3]), letter_to_number(input[2].upper())]


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

    def check(self, turn):
        for row in range(8):
            for column in range(8):

                if (self.board[row][column].color == turn):
                    start = [row, column]
                    legal_moves = self.board[row][column].generate_legal_moves(row, column, True)

                    for move in legal_moves:
                        end = [move[0], move[1]]
                        moves_between = self.board[row][column].moves_in_between(start, end, legal_moves)

                        clear_path = True
                        for move in moves_between:
                            if(self.board[move[0]][move[1]].color != "none"):
                                clear_path = False
                                break
                        if clear_path:
                            if turn == "black":
                                if (self.board[end[0]][end[1]].__str__() == "\u265A"):
                                    #print(f"{turn} checks white king")
                                    return True
                            elif turn == "white":
                                if (self.board[end[0]][end[1]].__str__() == "\u2654"):
                                    #print(f"{turn} checks black king")
                                    return True
        return False
        
    
    def final_move_list(self, start, turn):
        final_move_list = []

        opposite_turn = "black"
        if turn == "black":
            opposite_turn = "white"

        moves = self.board[start[0]][start[1]].generate_legal_moves(start[0], start[1], True)
        legal_moves = []

        if self.board[start[0]][start[1]].__str__() == "\u265F":
                for move in moves:
                    end = [move[0], move[1]]
                    
                    if (end[0] == start[0] - 1) and ((end[1] == start[1] - 1) or (end[1] == start[1] + 1)):
                        
                        if self.board[end[0]][end[1]].color == "black":
                            legal_moves.append(move)
                    else:
                        if self.board[end[0]][end[1]].color != "black":
                            legal_moves.append(move)
        elif self.board[start[0]][start[1]].__str__() == "\u2659":
                for move in moves:
                    end = [move[0], move[1]]
                    
                    if (end[0] == start[0] + 1) and ((end[1] == start[1] - 1) or (end[1] == start[1] + 1)):
                        
                        if self.board[end[0]][end[1]].color == "white":
                            legal_moves.append(move)
                    else:
                        if self.board[end[0]][end[1]].color != "white":
                            legal_moves.append(move)
        else:
            legal_moves = moves

            
        for move in legal_moves:
            end = [move[0], move[1]]
            
            moves_between = self.board[start[0]][start[1]].moves_in_between(start, end, legal_moves)

        # checks whether the piece is not "jumping" over other pieces while moving
            clear_path = True
            for mo_ve in moves_between:
                if(self.board[mo_ve[0]][mo_ve[1]].color != "none"):
                    #print("You cannot jump over pieces!")
                    clear_path = False

            # make sure that the piece that is moving can only attack the opposite color
            is_valid_color = True

            if(self.board[move[0]][move[1]].color == turn):
                #print("You cannot attack yourself!")
                is_valid_color = False

            if (self.board[start[0]][start[1]].color == turn and is_valid_color and clear_path):
                # moving piece

                start_piece = self.board[start[0]][start[1]]
                end_piece = self.board[move[0]][move[1]]

                self.board[move[0]][move[1]] = self.board[start[0]][start[1]]
                self.board[start[0]][start[1]] = piece.Tile()
                
                if not self.check(opposite_turn):
                    final_move_list.append([move[0], move[1]])

                self.board[move[0]][move[1]] = end_piece
                self.board[start[0]][start[1]] = start_piece

        return final_move_list
        
    def check_mate(self, turn):
        for row in range(8):
            for column in range(8):
                start = [row, column]
                if self.board[row][column].color == turn:
                    if self.final_move_list(start, turn) == []:
                        continue
                    return False
        
        return True

    def update(self, turn):

        opposite_turn = "black"
        if turn == "black":
            opposite_turn = "white"

        while True:
            print(f"{turn} to move!")
            
            input = read()

            start = start_from_input(input)
            end = end_from_input(input)

            # self.final_move_list(start, turn)

            if end not in self.final_move_list(start, turn):
                continue
            
            self.board[end[0]][end[1]] = self.board[start[0]][start[1]]
            self.board[start[0]][start[1]] = piece.Tile()
            break
        
            # current_piece = self.board[start[0]][start[1]]

            # is_attacking = True
            # if(self.board[end[0]][end[1]].color == turn or self.board[end[0]][end[1]].color == "none"):
            #     is_attacking = False
            
            # # generate legal, in terms of chess theory, moves and checks whether the move that a player wants to make is included
            # legal_moves = self.board[start[0]][start[1]].generate_legal_moves(start[0], start[1], is_attacking)
            # is_move_legal = current_piece.validate_move(legal_moves, end[0], end[1])

            # # generate moves between piece's start and supposed end position
            # moves_between = current_piece.moves_in_between(start, end, legal_moves)
            # # checks whether the piece is not "jumping" over other pieces while moving
            # clear_path = True
            # for move in moves_between:
            #         if(self.board[move[0]][move[1]].color != "none"):
            #             print("You cannot jump over pieces!")
            #             clear_path = False

            # # make sure that the piece that is moving can only attack the opposite color
            # is_valid_color = True

            # if(self.board[end[0]][end[1]].color == turn):
            #     print("You cannot attack yourself!")
            #     is_valid_color = False

            # # and if your king will not be in check after move 
            # if (current_piece.color == turn and is_move_legal and is_valid_color and clear_path):
            #     # moving piece
            #     start_piece = self.board[start[0]][start[1]]
            #     end_piece = self.board[end[0]][end[1]]

            #     self.board[end[0]][end[1]] = self.board[start[0]][start[1]]
            #     self.board[start[0]][start[1]] = piece.Tile()
                
            #     if self.check(opposite_turn):
            #         self.board[end[0]][end[1]] = end_piece
            #         self.board[start[0]][start[1]] = start_piece
            #         continue
            #     break
