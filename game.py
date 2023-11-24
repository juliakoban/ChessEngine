from board import Board
import os


def main():

    chess_board = Board()
    turn = "white"

    os.system("clear")
    print("WELCOME TO THE CHESS GAME")
    chess_board.display()

    while True:
        turn = "white"
        chess_board.update(turn)
        os.system("clear")
        chess_board.display()
        turn = "black"
        chess_board.update(turn)
        os.system("clear")
        chess_board.display()


if __name__ == "__main__":
    main()
