'''
    This is the board for the tic-tac-toe game
'''
import string


class Board:
    """
        Board class
    """
    SIZE = 3 #size of the board
    def __init__(self) -> None:
        self.board = [[""*Board.SIZE]*Board.SIZE]
        self.player1 = "X"
        self.player2 = "O"

    def move(self, player:string, x:int,y:int)->bool:
        '''
            move the player to the valid position
            @returns true if the move was valid; false other wise
        '''
        if self.board[x][y] != "" or (x >2) or y>2:
            return False
        self.board[x][y] = player
        return True

    def get_players(self)-> list:
        """
            retruns the player in the game
        """
        return [self.player1, self.player2]

    def display_board(self)->None:
        """
            print the board in the terminal/console
        """
        for row in self.board:
            print(f"[{str(row)}]")

    def check_win(self,player)->bool:
        '''
            Checks if a player has won the game or not
            @retrun True if the given player wins else false
        '''
        for i in range(3):
            if self.board[i][1] == self.board[i][2] == self.board[i][3] == player:
                return True
        for i in range(3):
            if self.board[1][i] == self.board[2][i] == self.board[3][i] == player:
                return True
        return