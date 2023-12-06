from board import Board
import os

def main():

    chess_board = Board()

    os.system("clear")
    print("WELCOME TO THE CHESS GAME")
    chess_board.display()

    while True:
        turn = "white"
        if chess_board.check_mate(turn):
            print("CHECK MATE! BLACK WINS!")
            break
        chess_board.update(turn)
        os.system("clear")
        chess_board.display()
        turn = "black"
        if chess_board.check_mate(turn):
            print("CHECK MATE! WHITE WINS!")
            break
        chess_board.update(turn)
        os.system("clear")
        chess_board.display()


if __name__ == "__main__":
    main()
