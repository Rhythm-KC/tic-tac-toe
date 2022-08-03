from board import Board
import logging
from logging.handlers import RotatingFileHandler


class AI:

    def __init__(self, board: Board):
        """

        @type board: object
        """
        self.board_ref = board

    def best_move(self):
        best_score = float("-inf")
        best_spot = (-1, -1)
        available_spot = self.board_ref.get_empty_spaces()
        for slot in available_spot:
            self.board_ref.move(slot[0], slot[1])

            score = self.minimax(False, 0)
            self.board_ref.undo_previous_move(slot)
            if score > best_score:
                best_score = score
                best_spot = slot
        self.board_ref.move(best_spot[0], best_spot[1])

    def minimax(self, next_is_maximizing: bool, depth) -> int:
        winnerVal = self.board_ref.check_win()
        if winnerVal is not None:
            return winnerVal

        if next_is_maximizing:
            best_score = float('-inf')
        else:
            best_score = float('inf')

        for slots in self.board_ref.get_empty_spaces():
            self.board_ref.move(slots[0], slots[1])
            if next_is_maximizing:
                best_score = max(best_score, self.minimax(False, depth + 1))
            else:
                best_score = min(best_score, self.minimax(True, depth + 1))
            self.board_ref.undo_previous_move(slots)

        return best_score
