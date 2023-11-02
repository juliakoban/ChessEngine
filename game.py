from board import Board

def main():
    chess_board = Board()
    chess_board.display()
    
    round = 0
    turn = "w"
    

    while(round < 2):
        turn = "w"
        chess_board.update(turn)
        chess_board.display()
        turn = "b"
        chess_board.update(turn)
        chess_board.display()
        round += 1

if __name__ == "__main__":
    main()
