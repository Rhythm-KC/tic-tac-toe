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
        self.__board = [[""*Board.SIZE]*Board.SIZE]
        self.__player1 = "X"
        self.__player2 = "O"
        self.move_counter = 0

    def move(self, player:string, x:int,y:int)->bool:
        '''
            move the player to the valid position
            @returns true if the move was valid; false other wise
        '''
        if self.__board[x][y] != "" or (x >2) or y>2 or self.move_counter < 9:
            return False
        self.move_counter +=1
        self.__board[x][y] = player
        return True

    def get_players(self)-> list:
        """
            retruns the player in the game
        """
        return self.__player1, self.__player2

    def display_board(self)->None:
        """
            print the board in the terminal/console
        """
        for row in self.__board:
            print(f"[{str(row)}]")

    def check_win(self,player)->int:
        '''
            Checks if a player has won the game or not
            @retrun 1 if player wins 0 if its a draw and -1 if the game is still alive
        '''
        if self.move_counter ==9:
            return 0
        for i in range(3):
            if self.__board[i][1] == self.__board[i][2] == self.__board[i][3] == player:
                return 1
        for i in range(3):
            if self.__board[1][i] == self.__board[2][i] == self.__board[3][i] == player:
                return 1
        if self.__board[1][1] == self.__board[2][2] == self.__board[0][0] == player or self.__board[0][2] == self.__board[1][1] == self.__board[2][0] == player:
            return 1
        return -1