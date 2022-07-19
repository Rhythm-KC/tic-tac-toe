import sys

import pygame as pg
import board


class UI:
    WINDOW_WIDTH = 400
    WINDOW_HEIGHT = 400
    player_X = "X"
    player_O = "O"

    def __init__(self, game_board: board.Board):
        pg.font.init()
        pg.init()
        self.font = pg.font.SysFont(None, 200)
        self.winner_font = pg.font.SysFont(None, 50)
        self.player_X_font = self.font.render("X", True, (255, 255, 255))
        self.player_O_font = self.font.render("O", True, (255, 255, 255))
        self.window = pg.display.set_mode((UI.WINDOW_WIDTH, UI.WINDOW_HEIGHT))
        pg.display.set_caption("Tic Tac Toe")
        self.board = game_board
        self.isWinner = None

    def draw_board(self):
        pg.draw.line(self.window, 'white', (UI.WINDOW_WIDTH / 3, 0), (UI.WINDOW_WIDTH / 3, UI.WINDOW_HEIGHT), 7)
        pg.draw.line(self.window, 'white', (UI.WINDOW_WIDTH * (2 / 3), 0),
                     (UI.WINDOW_WIDTH * (2 / 3), UI.WINDOW_HEIGHT), 7)
        pg.draw.line(self.window, 'white', (0, UI.WINDOW_HEIGHT / 3), (UI.WINDOW_WIDTH, UI.WINDOW_HEIGHT / 3), 7)
        pg.draw.line(self.window, 'white', (0, UI.WINDOW_HEIGHT / 3 * 2), (UI.WINDOW_WIDTH, UI.WINDOW_HEIGHT / 3 * 2),
                     7)
        top_margin = 5
        left_width = 15
        for i in range(self.board.SIZE):
            for j in range(self.board.SIZE):
                x_coordinate = 0
                y_coordinate = 0
                if self.board.get_board()[i][j] == UI.player_X or self.board.get_board()[i][j] == UI.player_O:
                    if i == 0:
                        y_coordinate = 1
                    elif i == 1:
                        y_coordinate = UI.WINDOW_HEIGHT / 3
                    elif i == 2:
                        y_coordinate = UI.WINDOW_HEIGHT / 3 * 2

                    if j == 0:
                        x_coordinate = 1
                    elif j == 1:
                        x_coordinate = UI.WINDOW_WIDTH / 3
                    elif j == 2:
                        x_coordinate = UI.WINDOW_WIDTH / 3 * 2
                    self.window.blit(
                        self.player_X_font if self.board.get_board()[i][j] == UI.player_X else self.player_O_font,
                        (x_coordinate + left_width, y_coordinate + top_margin))

    def find_click(self, pos):
        pos_x = pos[0]
        pos_y = pos[1]
        first_index = -1
        second_index = -1
        if 0 < pos_y < UI.WINDOW_HEIGHT / 3:
            first_index = 0
        if UI.WINDOW_HEIGHT / 3 < pos_y < (UI.WINDOW_HEIGHT / 3 * 2):
            first_index = 1
        if UI.WINDOW_HEIGHT / 3 * 2 < pos_y < UI.WINDOW_HEIGHT:
            first_index = 2

        if 0 < pos_x < UI.WINDOW_WIDTH / 3:
            second_index = 0
        if UI.WINDOW_WIDTH / 3 < pos_x < (UI.WINDOW_WIDTH / 3 * 2):
            second_index = 1
        if UI.WINDOW_WIDTH / 3 * 2 < pos_x < UI.WINDOW_WIDTH:
            second_index = 2
        if first_index != -1 and second_index != -1:
            self.board.move(first_index, second_index)

    def check_event(self):

        for event in pg.event.get():
            if event.type == pg.QUIT:
                pg.quit()
                sys.exit()
            if event.type == pg.MOUSEBUTTONUP and not self.isWinner:
                self.find_click(pg.mouse.get_pos())

    def check_winner(self):
        winner = self.board.check_win(UI.player_X)
        if winner == 1:
            self.isWinner = UI.player_X
        if winner == 0:
            self.isWinner = "Draw"
        if self.board.check_win(UI.player_O) == 1:
            self.isWinner = UI.player_O

    def update_window(self):
        if not self.isWinner:
            self.draw_board()
            pg.display.update()
        if self.isWinner is not None:
            winner_tage = self.winner_font.render('Its a draw' if self.isWinner == "Draw" else f'{self.isWinner} is '
                                                                                               f'the Winner', True,
                                                  (200, 2, 200))
            self.window.blit(winner_tage, (UI.WINDOW_WIDTH / 2 - 105, UI.WINDOW_HEIGHT / 2))
            pg.display.update()


def main():
    window = UI(board.Board())
    while True:
        window.check_event()
        window.update_window()
        if window.isWinner is None:
            window.check_winner()


if __name__ == '__main__':
    main()
