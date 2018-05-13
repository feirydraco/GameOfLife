
from random import randint
board_height = 10
board_width = 60
board = []
temp_board = []

def board_init(board):
    for i in range(0, (board_height + 1)):
        board.append([0] * (board_width + 1))

def print_board_beta(board):
    for i in range(board_height):
        for j in range(board_width):
            print(board[i][j], end = " ")
        print(sep = "\n")
def add_org(board, x, y):
    board[x][y] = 1


def populate(board, n):
    '''for i in range(0, board_height):
        for j in range(0, board_width):
            if board[i][j] != 1 and n > 0:
                add_org(board, i, j)
                n = n - 1'''
    for q in range(0, n):
        flag = 0
        while flag != 1:
            i = randint(0, board_height - 1)
            j = randint(0, board_width - 1)

            if board[i][j] != 1:
                add_org(board, i, j)
                flag = 1

def copy_board(source, dest):
    for i in range(0, board_height):
        for j in range(0, board_width):
            dest[i][j] = source[i][j]

def nbrs(board, x, y):
    no = 0
    for i in range(-1, 2):
        for j in range(-1, 2):
            #print i, j
            if board[x + i][y + j] == 1 and ((x + i >= 0 and y + j >= 0) and (x + i < board_height and y + j < board_width)):
                no = no + 1
    if board[x][y] == 1:
        no = no - 1
    return no

def play(board):
    board_init(temp_board)
    for i in range(0, board_height - 1):
        for j in range(0, board_width - 1):
            if nbrs(board, i, j) < 2 or nbrs(board, i, j) > 3:
                temp_board[i][j] = 0
            elif (nbrs(board, i, j) == 2 or nbrs(board, i, j) == 3) and board[i][j] == 1:
                temp_board[i][j] = 1
            elif nbrs(board, i, j) == 3 and board[i][j] == 0:
                temp_board[i][j] = 1

board_init(board)

print_board_beta(board)

cc = 0

while(cc == 0):
    n = int(input("Enter number of organisms to spawn: "))
    if n <= board_height * board_width:
        cc = 1
    else:
        print ("Too many organisms")


populate(board, n)

print_board_beta(board)
print ("\n\n")

gen = int(input("Simulate for how many generations?: "))

for i in range(0, gen):
    print (("Generation"), i + 1)
    print ("\n")
    play(board)
    print_board_beta(temp_board)
    board_init(board)
    copy_board(temp_board, board)
    board_init(temp_board)
    print ("\n")
