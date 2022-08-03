class Game:
    def __init__(self, coordinates=0, board=[[" "," "," "],[" "," "," "],[" "," "," "]]):
        self.board = board
        self.coordinates = coordinates
        self.wins = {
            'row_x': ["x","x","x"],
            'row_o': ["o","o","o"],
            'col_1x': [["x"," "," "],["x"," "," "],["x"," "," "]],
            'col_2x': [[" ","x"," "],[" ","x"," "],[" ","x"," "]],
            'col_3x': [[" "," ","x"],[" "," ","x"],[" "," ","x"]],
            'col_1o': [["o"," "," "],["o"," "," "],["o"," "," "]],
            'col_2o': [[" ","o"," "],[" ","o"," "],[" ","o"," "]],
            'col_3o': [[" "," ","o"],[" "," ","o"],[" "," ","o"]],
            'dia_1x': [["x"," "," "],[" ","x"," "],[" "," ","x"]],
            'dia_2x': [[" "," ","x"],[" ","x"," "],["x"," "," "]],
            'dia_1o': [["o"," "," "],[" ","o"," "],[" "," ","o"]],
            'dia_2o': [[" "," ","o"],[" ","o"," "],["o"," "," "]],
        }

    def __str__(self):
        board = ""
        for cell in self.board:
            
            board += "|".join(cell)
            board += "\n"

        return board
    def move(self, x, y, player):
        self.board[x][y] = player

    def calc_winner(self):
        scorex, scorey = 0, 0

        grid = ''
        grid2 = ''
        for row in range(3):
            # grid += '],['.join(self.board[row])
            grid += '\n'
            grid2 += '\n'
            
            for cell in range(3):
                # if self.board[row][cell] == self.wins['col_1x'][row][cell]:
                    # print(True)
                grid += self.board[row][cell]
                grid2 += self.wins['col_1x'][row][cell]
        
        print(grid)
        print(grid2)
            

mygame = Game()
mygame.move(0, 1, 'x')
mygame.move(0, 2, 'o')
mygame.move(1, 1, 'o')
mygame.move(2, 1, 'o')
mygame.move(0, 0, 'x')
mygame.move(1, 0, 'x')
mygame.move(2, 0, 'x')

mygame.calc_winner()
# print(mygame)