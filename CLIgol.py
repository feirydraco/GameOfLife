
from random import randint

class GOL:
    def __init__(self, data):
        self.board_height = 100
        self.board_width = 100
        self.board = []
        self.temp_board = []
        self.data = data
        self.n = 0
        for char in data:
            self.n += ord(char)
    
    def board_init(self, board):
        for i in range(0, (self.board_height + 1)):
            self.board.append([0] * (self.board_width + 1))
    
#    def print_board_beta(board):
#        for i in range(board_height):
#            for j in range(board_width):
#                print(board[i][j], end = " ")
#            print(sep = "\n")
            
    def add_org(self, x, y):
        self.board[x][y] = 1
        
    def copy_board(source, dest):
        for i in range(0, board_height):
            for j in range(0, board_width):
                dest[i][j] = source[i][j]
    
    def nbrs(self, x, y):
        no = 0
        for i in range(-1, 2):
            for j in range(-1, 2):
                #print i, j
                if self.board[x + i][y + j] == 1 and ((x + i >= 0 and y + j >= 0) and (x + i < self.board_height and y + j < self.board_width)):
                    no = no + 1
        if self.board[x][y] == 1:
            no = no - 1
        return no
    
    def play(self, board):
        board_init(self.temp_board)
        for i in range(0, self.board_height - 1):
            for j in range(0, self.board_width - 1):
                if nbrs(board, i, j) < 2 or nbrs(board, i, j) > 3:
                    self.temp_board[i][j] = 0
                elif (nbrs(board, i, j) == 2 or nbrs(board, i, j) == 3) and board[i][j] == 1:
                    self.temp_board[i][j] = 1
                elif nbrs(board, i, j) == 3 and board[i][j] == 0:
                    self.temp_board[i][j] = 1
    
    board_init(self.board)
    
    print_board_beta(self.board)
    
    populate(board, n)
    
    print_board_beta(self.board)
    print ("\n\n")
    
    
    
    for i in range(0, n):
        print (("Generation"), i + 1)
        print ("\n")
        play(board)
        print_board_beta(temp_board)
        board_init(board)
        copy_board(temp_board, board)
        board_init(temp_board)
        print ("\n")


g = GOL("hello")