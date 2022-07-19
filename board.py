"""
    This is the board for the tic-tac-toe game
"""
from typing import List


class Board:
    """
        Board class
    """
    __board: List[List[str]]
    SIZE = 3  # size of the board

    def __init__(self) -> None:
        self.__board = [[" " for i in range(Board.SIZE)] for j in range(Board.SIZE)]
        self.__player1 = "X"
        self.__player2 = "O"
        self.move_counter = 0

    def __str__(self):
        string = ''
        for rows in self.__board:
            string += f"{str(rows)}\n"
        return string

    def get_board(self):
        return self.__board

    def move(self, x: int, y: int) -> bool:
        """
            move the player to the valid position
            @returns true if the move was valid; false other wise
        """
        if " " != self.__board[x][y] or not (0 <= x <= 2) or not (0 <= y <= 2) or self.move_counter > 9:
            return False
        self.__board[x][y] = self.__player1 if self.move_counter % 2 == 0 else self.__player2
        self.move_counter += 1
        return True

    def get_players(self):
        """
            returns the player in the game
        """
        return self.__player1, self.__player2

    def check_win(self, player) -> int:
        """
            Checks if a player has won the game or not
            @return 1 if player wins 0 if its a draw and -1 if the game is still alive
        """
        if self.move_counter == 9:
            return 0
        for i in range(3):
            if self.__board[i][0] == self.__board[i][1] == self.__board[i][2] == player:
                return 1
        for i in range(3):
            if self.__board[0][i] == self.__board[1][i] == self.__board[2][i] == player:
                return 1
        if self.__board[1][1] == self.__board[2][2] == self.__board[0][0] == player or self.__board[0][2] == \
                self.__board[1][1] == self.__board[2][0] == player:
            return 1
        return -1
