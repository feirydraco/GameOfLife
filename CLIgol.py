class GOL:
    def __init__(self, data):
        self.board_height = 20
        self.board_width = len(data)
        self.board = []
        self.temp_board = []
        self.data = data
        self.n = 0
        for char in self.data:
            self.n += ord(char)
    def board_init(self, board):
        for i in range(self.board_height + 1):
            board.append([0] * (self.board_width + 1))
    def print_board_beta(self):
        for i in range(self.board_height):
            for j in range(self.board_width):
                print(self.board[i][j], end = " ")
            print(sep = "\n")
    def add_org(self, x, y):
        self.board[x][y] = 1
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
    def play(self):
        self.board_init(self.temp_board)
        for i in range(0, self.board_height - 1):
            for j in range(0, self.board_width - 1):
                if self.nbrs(i, j) < 2 or self.nbrs(i, j) > 3:
                    self.temp_board[i][j] = 0
                elif (self.nbrs(i, j) == 2 or self.nbrs(i, j) == 3) and self.board[i][j] == 1:
                    self.temp_board[i][j] = 1
                elif self.nbrs(i, j) == 3 and self.board[i][j] == 0:
                    self.temp_board[i][j] = 1
    def compute(self):
        self.board_init(self.board)
        self.print_board_beta()

        print ("\n\n")



        for i in range(self.n):
            print (("Generation"), i + 1)
            print ("\n")
            self.play()
            self.print_board_beta()
            self.board_init(self.board)
            self.temp_board = self.board
            self.board_init(self.temp_board)
            print ("\n")
g = GOL("hi")
g.compute()
