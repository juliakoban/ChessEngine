from board import Board
import os


def main():

    chess_board = Board()
    round = 0
    turn = "white"

    print("WELCOME TO THE CHESS GAME")
    chess_board.display()

    while round < 2:
        turn = "white"
        chess_board.update(turn)
        os.system("clear")
        chess_board.display()
        turn = "black"
        chess_board.update(turn)
        os.system("clear")
        chess_board.display()
        round += 1


if __name__ == "__main__":
    main()
