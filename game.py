from board import Board
from ai import AI

class Game:

    def __init__(self):
        self.board = Board()
        self.player1, self.player2 = self.board.get_players()
        self.is_running = True
        self.ai = AI(self.board)

    def play_game(self):
        print(self.board)
        while True:
            current_player = self.player1 if self.board.move_counter % 2 == 0 else self.player2
            if current_player == self.player2:
                val = input(f'Its {current_player} turn. Enter a valid space you want to move')
                if len(val) < 2 or not val.isdigit():
                    print("Illegal move")
                    continue
                if not self.board.move(int(val[0]) - 1, int(val[1]) - 1):
                    print("Illegal move no such coordinate found")
                    continue
            else:
                self.ai.best_move()

            print(self.board)

            result = self.board.check_win()
            if result == 1:
                print(f' X wins')
                return
            if result == 0:
                print("Its a draw")
                return
            if result == -1:
                print("O wins")


def main():
    game = Game()
    game.play_game()


if __name__ == '__main__':
    main()
