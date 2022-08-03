class Game:
    def __init__(self, coordinates=0, board=[[" "," "," "],[" "," "," "],[" "," "," "]]):
        self.board = board
        self.coordinates = coordinates

    def __str__(self):
        board = ""
        for cell in self.board:
            
            board += "|".join(cell)
            board += "\n"

        return board
    def move(x,y,player):
        ...




