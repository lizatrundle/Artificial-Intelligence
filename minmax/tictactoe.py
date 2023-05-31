#
# Tic-Tac-Toe Minimax with Alpha-beta pruning (Suboptimal play with -INFINITE = -2, +INFINITE = 2)
#

INFINITE = 10
# if you change infinite to less , bc 10 is higher than 1
DEPTH_INCREMENT = 1
# we need depth increment to be 1, if you had anymore than 1 

# the best you can get is a tie 

class TicTacToe():
    def __init__(self, prune=False,grid=[['_','_','_'],['_','_','_'],['_','_','_']]):
        self._game_counter = 0
        self._play_counter = 0
        self._grid = grid
        self._player_turn = 'X'
        self._prune = prune

    def __draw(self):
        print ("")

        for i in range(0, 3):
            for j in range(0, 3):
                print ("{}|".format(self._grid[i][j]), end="")

            print ("")

        print ("")

    def __valid_coordinates(self, px, py):
        if px < 0 or px > 2 or py < 0 or py > 2:
            return False
        elif self._grid[px][py] != '_':
            return False
        else:
            return True

    def __game_over(self):
        # horizontal win: X player wins when ['X', 'X', 'X'] in rows 0 to 2

        for i in range(0, 3):
            if (self._grid[i] == ['X', 'X', 'X']):
                return 'X'

        # horizontal win: O player wins when ['X', 'X', 'X'] in rows 0 to 2

        for i in range(0, 3):
            if (self._grid[i] == ['O', 'O', 'O']):
                return 'O'

        # vertical win: for i=0 to 2 grid positions [0][i], [1][i], and [2][i] are not '_' and have the same value

        for i in range(0, 3):
            if (self._grid[0][i] != '_' and self._grid[0][i] == self._grid[1][i] and self._grid[1][i] == self._grid[2][i]):
                return self._grid[0][i]

        # main diagonal win: grid positions [0][0], [1][1], and [2][2] have the same value

        if (self._grid[0][0] != '_' and self._grid[0][0] == self._grid[1][1] and self._grid[0][0] == self._grid[2][2]):
            return self._grid[0][0]

        # second diagonal win: grid positions [0][2], [1][1], and [2][0] have the same value

        if (self._grid[0][2] != '_' and self._grid[0][2] == self._grid[1][1] and self._grid[0][2] == self._grid[2][0]):
            return self._grid[0][2]

        # if the grid is full the game ends with a tie

        for i in range(0, 3):
            for j in range(0, 3):
                # if there is an empty position '_', the game is not over

                if (self._grid[i][j] == '_'):
                    return None

        return '_'

    def __minimax_max(self, depth, alpha, beta):
        # the AI player (O) is a Max player, possible values for the Max player are -1 (X player wins), +1 (O player wins), or zero (tie)

        max_value = -INFINITE

        # max_px, max_py are the coordinates of the optimal play

        max_px = -1
        max_py = -1

        winner = self.__game_over()

        # check if the current state is a final state of the game 'X': X player wins, 'O': O player wins, '_': tie

        if winner == 'X' or winner == 'O' or winner == '_':
            self._play_counter += 1
            self._game_counter += 1

        # if the game is over, return the score

        if winner == 'X':
            return (-INFINITE+depth, 0, 0)  # X is a Min player, the value of its best play is -1
        elif winner == 'O':
           return (INFINITE-depth, 0, 0)   # O is a Max player, the value of its best play is 1
        elif winner == '_':
            return (0, 0, 0)   # the game ends with a tie

        # evaluate all possible plays

        for i in range(0, 3):
            for j in range(0, 3):
                if self._grid[i][j] == '_':
                    self._grid[i][j] = 'O'

                    # minimax_min returns a tuple with the value of a final state

                    (value, min_x, min_y) = self.__minimax_min(depth+DEPTH_INCREMENT,alpha, beta)

                  #  print("best score for" , i, j, "for max player after min plays is", value)

                    # max_value is updated when a larger value is found

                    if value > max_value:
                        max_value = value
                        max_px = i
                        max_py = j

                    # when the recursive calls for the [i][j] play terminate, the value of [i][j] is restored

                    self._grid[i][j] = '_'

                    # update alpha with the best value for Max player

                    if max_value > alpha:
                        alpha = max_value

                    if self._prune is True:
                        if beta <= alpha:
                            return (alpha, max_px, max_py)

                    

        # minimax_max returns alpha and the coordinates max_px, max_py of the optimal play

        return (alpha, max_px, max_py)

    def __minimax_min(self, depth, alpha, beta):
        # the human player (X) is a Min player, possible values for Min player are are -1 X player wins), +1 (O player wins), or zero (tie)

        min_value = INFINITE

        # min_px, min_py are the coordinates of the optimal play

        min_px = -1
        min_py = -1

        winner = self.__game_over()

        # check if the current state is a final state of the game 'X': X player wins, 'O': O player wins, '_': tie

        if winner == 'X' or winner == 'O' or winner == '_':
            self._play_counter += 1
            self._game_counter += 1

        # if the game is over, return the score

        if winner == 'X':
            return (-INFINITE+depth, 0, 0)  # X is a Min player, the value of its best play is -1
        elif winner == 'O':
            return (INFINITE-depth, 0, 0)   # O is a Max player, the value of its best play is 1
        elif winner == '_':
            return (0, 0, 0)   # the game ends with a tie

        # evaluate all possible plays

        for i in range(0, 3):
            for j in range(0, 3):
                if self._grid[i][j] == '_':
                    self._grid[i][j] = 'X'

                    # minimax_max returns a tuple with the value of a final state

                    (value, max_x, max_y) = self.__minimax_max(depth + DEPTH_INCREMENT,alpha, beta)

                   # print("best score for" , i, j, "for min player after max plays is", value)

                    # min_value is updated when a smaller value is found

                    

                    if value < min_value:
                        min_value = value
                        min_px = i
                        min_py = j

                    # when the recursive calls for the [i][j] play terminate, the value of [i][j] is restored

                    self._grid[i][j] = '_'

                    # update beta with the best value for Min player

                    if min_value < beta:
                        beta = min_value

                    if self._prune is True:
                        if beta <= alpha:
                            return (beta, min_px, min_py)

                    

        # minimax_min returns beta and the coordinates min_px, min_py of the optimal play

        return (beta, min_px, min_py)

    @property
    def game_counter(self):
        return self._game_counter

    def play(self):
        while True:
            self.__draw()

            winner = self.__game_over()

            # if the game is over

            if winner != None:
                if winner == 'X':
                    print ("X player wins!")
                elif winner == 'O':
                    print ("O player wins!")
                elif winner == '_':
                    print ("The game ends with a tie!")

                return

            if self._player_turn == 'X':

                # X plays

                while True:
                    print ("Player X enter coordinates x y: ", end="")

                    px, py = map(int, input().split())

                    if self.__valid_coordinates(px, py):
                        self._grid[px][py] = 'X'
                        self._player_turn = 'O'
                        break
                    else:
                        print ("Coordinates are not valid! Play again")

            else:

                # O plays

                self._play_counter = 0

                (value, px, py) = self.__minimax_max(0,-INFINITE, INFINITE)

                self._grid[px][py] = 'O'
                self._player_turn = 'X'

                print("States evaluated for the last play:", self._play_counter)


# to run the program from the terminal: $ python tictactoeminimaxsuboptimal.py

if __name__ == "__main__":

    print ("Tic-Tac-Toe Minimax")

    # g = TicTacToe([['X', 'O', '_'], ['_', 'O', '_'], ['_', '_', 'X']])
    g = TicTacToe(prune=True)
    
    g.play()

    print("\nTotal states evaluated with pruning:", g.game_counter)

    f = TicTacToe(prune=False)
    
    f.play()
    print("\nTotal states evaluated without pruning:", f.game_counter)

