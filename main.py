from board import Board
from game import Game

# This keeps variables local to the main function (Helps to keep scope nice and clean)
def main() -> None:
    board = Board()
    game = Game(board)
    game.run_game()


if __name__ == '__main__':
    main()
