# tic-tac-toe
- This is an attempt to create an AI that can play tic-tac-toe and get the best results possible.
- Here we are using python as our language and pygame module for a GUI.

# Structure 

#### board.py
   The board.py file contains a Board class.
   - This class internalizes a tic-tac-toe board as a 3 * 3 list 
   - The class also keeps track of the number of valid moves, players on the board 
   - The class has methods such as `move()` and `check_win()` that help us to change and read the state of the board respectively

#### ui.py
   The ui.py uses pygame module to create a GUI and run the game and it has the UI class.
   The UI class is responsible for the following behaviours and attributes:
   - It uses our Board class to store and change the state of the board according to the user input
   - It has functions such as `draw()` and `check_events()` to draw our tic-tac-toe board and check for the user's action respectively.
   - For now, the GUI is 400 by 400 pixels.
#### ai.py
   The ai.py class represents our AI bot for our tic-tac-toe.
   - Our bot uses the minimax algorithm to find the move to get the best results possible.
   - The AI class need a reference to an instance of the **Board class** 
   - The `best_move()` method calls our `minimax()` method. 
#### game.py
   This class allows us to play the game through the terminal.

# Minimax Algorithm
For a game like tic-tac-toe, which is a two-player turn base game, we can recursively create all the possible outcomes possible. But creating all those possibilities is not enough. We have to find a way to know which is the best move for the current player. For that, we categorize the players as either the *minimizing* player or the *maximizing* player. The minimizing player aims to minimize the outcome of the game and the maximizing player aims to maximize the outcome of our game. 

So, to maximize or minimize our game. We assign a negative number to the end state that benefits the minimizing player. For our game **Player O** is the minimizing player. So whenever he wins we return -1. And for **player X** who is the maximizing player whenever he wins we return 1. If there is a draw we return 0. 
```python
    def minimax(self, next_is_maximizing: bool, depth) -> int:
         '''
        @param next_is_maximizing: is the next player a maximizing player (if ture then current player is minimizing
                                    else the current player is maximizing)
        @param depth: what depth we are on 
        @return: the best score if maximizing player then return the max possible score
                if the minimizing player then return the minimum possible score
        '''
        
        winnerVal = self.board_ref.check_win() # check for the win using th
        if winnerVal is not None: # if winner found return the state 
            return winnerVal
        
        if next_is_maximizing:
            best_score = float('-inf')
        else:
            best_score = float('inf')
         # checking every empty position in our board
        for slots in self.board_ref.get_empty_spaces():
            
            self.board_ref.move(slots[0], slots[1]) # moving the player 
            if next_is_maximizing:
                 
                best_score = max(best_score, self.minimax(False, depth + 1))
            else:
                best_score = min(best_score, self.minimax(True, depth + 1))
            self.board_ref.undo_previous_move(slots)

        return best_score
```
# Improvements to work on 
-  ### GUI and the Game
   * The Game for now only allows the user to play once. Additional features can be added to make the GUI more user friendly
      * This can be done by adding a restart/ play again button 
      * Adding different game modes such as Single player or multiplayer
      * In Single player mode, we can let the user choose if they want to go first or if the AI should go first.
- ### Improve Minimax Algorithm
   * for now the Minimax algorithm is a bit inefficient. 
   * We can make it efficient by incentivizing the algorithm to prefer a move that leads to the optimal solution is the least number of moves. For that, we can the **depth** it on and return values according to that 
   * We can also use alpha-beta pruning to prune moves that have already been discovered. 
               
    

