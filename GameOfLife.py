from tkinter import *
from random import randint
import tkinter.messagebox


'''globals'''
board_height = 80
board_width = 165
temp_board = []
gate = -1


#############################################################################################

class Cell():
    '''Parameters for each cell on the board'''
    FILLED_COLOR_BG = "green"
    EMPTY_COLOR_BG = "white"
    FILLED_COLOR_BORDER = "green"
    EMPTY_COLOR_BORDER = "black"

    def __init__(self, master, x, y, size):
        self.master = master
        self.abs = x
        self.ord = y
        self.size= size
        self.fill= False


    def _switch(self):
        ''' Switch if the cell is filled or not. '''
        self.fill = not self.fill

    def draw(self):
        ''' order to the cell to draw its representation on the canvas '''
        if self.master != None :
            fill = Cell.FILLED_COLOR_BG
            outline = Cell.FILLED_COLOR_BORDER

            if not self.fill:
                fill = Cell.EMPTY_COLOR_BG
                outline = Cell.EMPTY_COLOR_BORDER

            xmin = self.abs * self.size
            xmax = xmin + self.size
            ymin = self.ord * self.size
            ymax = ymin + self.size

            self.master.create_rectangle(xmin, ymin, xmax, ymax, fill = fill, outline = outline)


class CellGrid(Canvas):
    '''Actual Board'''
    def __init__(self, master, rowNumber, columnNumber, cellSize, board):
        Canvas.__init__(self, master, width = cellSize * (columnNumber - 1), height = cellSize * (rowNumber - 1))
        self.cellSize = cellSize
        self.grid = []
        for row in range(rowNumber - 1):
            line = []
            for column in range(columnNumber - 1):
                line.append(Cell(self, column, row, cellSize))
            self.grid.append(line)

        self.bind("<Button-1>", self.handleMouseClick)
        self.draw()

    def draw(self):
        '''Toggles a pixel's color'''
        for row in self.grid:
            for cell in row:
                cell.draw()

    def _eventCoords(self, event):
        '''returns (x, y) for a cell'''
        row = int(event.y / self.cellSize)
        column = int(event.x / self.cellSize)
        return row, column

    def handleMouseClick(self, event):
        '''updates in backend'''

        RandomPopulate.configure(state = DISABLED)
        row, column = self._eventCoords(event)
        cell = self.grid[row][column]
        cell._switch()
        cell.draw()
        if board[row][column] == 0:
            board[row][column] = 1
        else:
            board[row][column] = 0

#############################################################################################

#############################################################################################
#functions
def clear(board):
    '''Sets all cells to False'''
    for i in range(0, board_height - 1):
        for j in range(0, board_width - 1):
            cell = grid.grid[i][j]
            if board[i][j] == 1:
                board[i][j] = 0
                cell._switch()
                cell.draw()
    RandomPopulate.configure(state = NORMAL)

def board_init(board):
    '''Allocates memory for the board'''
    del board[:]
    for i in range(0, (board_height + 1)):
        board.append([0] * (board_width + 1))

def print_board(board):
    '''Prints the board in the backend'''
    #Not required for gui based application
    for i in range(0, board_height):
        for j in range(0, board_width):
            print(board[i][j], end = ' ')
        print ("\n")

def add_org(board, x, y):
    '''Desired co-ordinate cell is added to both backend and gui'''
    board[x][y] = 1


def populate(board, n):
    '''Randomly selects n cells and adds an organism to those cells'''
    for q in range(0, n):
        flag = 0
        while flag != 1:
            i = randint(0, board_height - 1)
            j = randint(0, board_width - 1)

            if board[i][j] != 1:
                add_org(board, i, j)
                flag = 1

    for i in range(0, board_height - 1):
        for j in range(0, board_width - 1):
            cell = grid.grid[i][j]
            if board[i][j] == 1:
                cell._switch()
                cell.draw()

def copy_board(source, dest):
    '''Copies a board to another'''
    for i in range(0, board_height):
        for j in range(0, board_width):
            dest[i][j] = source[i][j]


def nbrs(board, x, y):
    '''Returns the number of neighbors for any given cell, keeping boundary conditions intact'''
    no = 0
    for i in range(-1, 2):
        for j in range(-1, 2):
            if board[x + i][y + j] == 1 and ((x + i >= 0 and y + j >= 0) and (x + i < board_height and y + j < board_width)):
                '''last two conditions for boundary'''
                no = no + 1
    if board[x][y] == 1:
        no = no - 1
    return no

def play(board):
    '''main driver function to intialise one step of the algorithm'''
    board_init(temp_board)

    for i in range(0, board_height - 1):
        for j in range(0, board_width - 1):
            '''Checks each cell's number of neighbours and performs predefined rules, All the new cells are stored in a temp board'''
            if nbrs(board, i, j) < 2 or nbrs(board, i, j) > 3:
                temp_board[i][j] = 0
            elif (nbrs(board, i, j) == 2 or nbrs(board, i, j) == 3) and board[i][j] == 1:
                temp_board[i][j] = 1
            elif nbrs(board, i, j) == 3 and board[i][j] == 0:
                temp_board[i][j] = 1

def inputPopup():
    '''Creates a popup dialog to input number of organisms'''
    inputDialog = popup1(gui)
    gui.wait_window(inputDialog.top)
    if int(inputDialog.number) > board_height * board_width:
        tkinter.messagebox.showerror("Undefined", "Too many organisms")
        return
    populate(board, int(inputDialog.number))
    RandomPopulate.configure(state = DISABLED)

def chooseGate():
    '''Creates a popup dialog to input which gate user wants to visualise'''
    Logic.configure(state = DISABLED)
    obj = popup2(gui)
    gui.wait_window(obj.top)
    gate = obj.gate
    SpawnGate(gate)
    Logic.configure(state = NORMAL)


def SpawnGate(gate):
    '''Spawns gate with relative coordinates. All coordinates are defined pre-execution'''
    if gate == 1:
        spawnGlider(board, 1, 0)
        spawnGlider(board, 0, 40)
        spawnReverseGlider(board, 3, 90)
        spawnEaterAnd(board)
        update_gui_()

        return
    if gate == 2:
        spawnGlider(board, 1, 0)
        spawnGlider(board, 1, 40)
        spawnGlider(board, 1, 80)
        spawnReverseGlider(board, 3, 120)
        spawnEaterOr(board)
        update_gui_()

        return
    if gate == 3:
        spawnGlider(board, 1, 0)
        spawnReverseGlider(board, 3, 40)
        spawnEaterNot(board)
        update_gui_()

        return
    tkinter.messagebox.showwarning("Undefined", "No gate selected")
    return -1

def update_board():
    '''updates board of the board ie. toggles cells to their respective and desired states'''
    play(board)
    for i in range(0, board_height - 1):
        for j in range(0, board_width - 1):
            cell = grid.grid[i][j]
            if cell.fill == True and temp_board[i][j] == 0:
                cell._switch()
                cell.draw()
            elif cell.fill == False and temp_board[i][j] == 1:
                cell._switch()
                cell.draw()
    copy_board(temp_board, board)
    board_init(temp_board)

def fast_forward():
    '''Forces program to exectute desired number of iterations'''
    RandomPopulate.configure(state = DISABLED)
    for i in range(29):
        play(board)
        copy_board(temp_board, board)
        board_init(temp_board)
    play(board)
    copy_board(temp_board, board)

    for i in range(0, board_height - 1):
        for j in range(0, board_width - 1):
            cell = grid.grid[i][j]
            if cell.fill == True and temp_board[i][j] == 0:
                cell._switch()
                cell.draw()
            elif cell.fill == False and temp_board[i][j] == 1:
                cell._switch()
                cell.draw()

def close():
    gui.destroy()

def update_gui_():
    '''update function for board when only a gate is spawned'''
    for i in range(0, board_height - 1):
        for j in range(0, board_width - 1):
            cell = grid.grid[i][j]
            if board[i][j] == 1:
                cell._switch()
                cell.draw()

#############################################################################################
                '''Particular coordinates on the board to visualise a logic gate'''

def spawnGlider(board, x, y):
    toSpawn = [[5, 1],[6, 1],[6, 2],[5, 2],[5, 5],[4, 6],[5, 6],[6, 6],[3, 7],[7, 7],[5, 8],[2, 9],[2, 10],[3, 11],
               [4, 12],[5, 12],[6, 12],[7, 11],[8, 10],[8, 9],[7, 17],[7, 20],[7, 21],[7, 22],[6, 22],[5, 21],[6, 26],
               [5, 26],[1, 26],[0, 26],[1, 28],[5, 28],[2, 29],[3, 29],[4, 29],[4, 30],[3, 30],[2, 30],[3, 35],
               [4, 35],[4, 36],[3, 36]]
    for emt in toSpawn:
        add_org(board, int(x + emt[0]), int(y + emt[1]))

def spawnReverseGlider(board, x, y):
    toSpawn = [[0, 0], [1, 0], [1, 1], [0, 1], [0, 6], [1, 6], [1, 7], [0, 7], [-1, 7], [-1, 6], [-2, 8], [-2, 10],
               [-3, 10], [2, 8], [2, 10], [3, 10], [3, 14], [4, 14], [4, 15], [4, 16], [2, 15], [4, 19], [4, 25],
               [3, 24], [2, 24], [1, 24], [0, 25], [-1, 26], [-1, 27], [5, 26], [5, 27], [2, 28], [2, 30], [2, 31],
               [1, 30], [3, 30], [0, 29], [4, 29], [2, 34], [2, 35], [3, 35], [3, 34]]
    for emt in toSpawn:
        add_org(board, int(x + emt[0]), int(y + emt[1]))

def spawnEaterAnd(board):
    toSpawn = [[56, 66], [57, 66], [57, 67], [57, 69], [57, 67], [55, 69], [55, 70],
               [56, 70], [55, 73], [56, 73], [56, 74], [55, 74], [59, 66], [59, 67], [60, 67], [60, 66], [57, 68]]
    for emt in toSpawn:
        add_org(board, int(emt[0]), int(emt[1]))

def spawnEaterOr(board):
    toSpawn = [[72, 82], [73, 82], [73, 83], [73, 84], [73, 85], [72, 86], [71, 86], [71, 85], [71, 89],
               [72, 89], [72, 90], [71, 90], [75, 82], [75, 83], [76, 83], [76, 82]]
    for emt in toSpawn:
        add_org(board, int(emt[0]), int(emt[1]))

def spawnEaterNot(board):
    toSpawn = [[32, 24], [32, 25], [33, 24], [33, 24], [33, 25], [32, 28], [32, 29], [33, 28],
                [34, 29], [34, 30], [34, 31], [34, 32], [33, 32], [36, 31], [36, 32], [37, 32],
                [37, 31]]
    for emt in toSpawn:
        add_org(board, int(emt[0]), int(emt[1]))

#############################################################################################


#############################################################################################

#PopupDialogs
class popup1:
    def __init__(self, parent):
        top = self.top = Toplevel(parent)
        self.Label = Label(top, text='Enter number of organisms')
        self.Label.pack()
        self.EntryBox = Entry(top)
        self.EntryBox.pack()
        self.SubmitButton = Button(top, text='Submit', command=self.send)
        self.SubmitButton.pack()

    def send(self):
        self.number = self.EntryBox.get()
        self.top.destroy()

class popup2:

    def __init__(self, parent):

        top = self.top = Toplevel(parent)
        self.Label = Label(top, text='Select Logic Gate')
        self.And = Button(top, text = 'AND', command = lambda i=1: self.Return(i))
        self.And.grid(row = 0, column = 0, padx = 5)
        self.Or = Button(top, text = 'OR', command = lambda i=2: self.Return(i))
        self.Or.grid(row = 0, column = 1, padx = 5)
        self.Not = Button(top, text = 'NOT', command = lambda i=3: self.Return(i))
        self.Not.grid(row = 0, column = 2, padx = 5)
        self.top.protocol('WM_DELETE_WINDOW', self.doSomething)

    def Return(self, i):
        self.gate = i
        self.top.destroy()

    def doSomething(self):
        self.Return(4)

#############################################################################################


gui = Tk()

gui.title("Game Of Life")
board = []
board_init(board)

frame = Frame(gui)
frame.pack(side = BOTTOM)


RandomPopulate = Button(frame, text = "Populate", command = inputPopup)
RandomPopulate.grid(row = 0, column = 4, rowspan = 2, sticky = N + S, padx = (20, 0))


Logic = Button(frame, text = "Demonstrate Logic Gates", command = chooseGate)
Logic.grid(row = 0, column = 5, rowspan = 2, sticky = N + S)

Next = Button(frame, text = "Next Generation", repeatdelay=1, repeatinterval=1, command = lambda: update_board())
Next.grid(row = 0, column = 6, rowspan = 2, sticky = N + S)

FF = Button(frame, text = "Fast forward 30 Generations", command = fast_forward)
FF.grid(row = 0, column = 7, rowspan = 2, sticky = N + S)



Clear = Button(frame, text = "Clear Memory", command = lambda: clear(board))
Clear.grid(row = 0, column = 9, sticky = N + E + W)

Exit = Button(frame, text = "Exit", command = close)
Exit.grid(row = 1, column = 9, sticky = E + W)



grid = CellGrid(gui, board_height, board_width, 10, board)
grid.pack()

gui.focus_set()
gui.grab_set()
gui.mainloop()
