from cell import Cell
from cellgrid import CellGrid
from tkinter import Tk, Frame, Button
import tkinter.messagebox
from random import randint
from popups import popupInput
board_height = 5
board_width = 5

def populate():
    x, y = randint(0, board_height - 2), randint(0, board_width - 2)
    cell = grid.grid[x][y]
    print(x, y)
    if cell.fill == False:
        cell.switch()
        cell.draw()

def clear():
    for i in range(board_height - 1):
        for j in range(board_width - 1):
            cell = grid.grid[i][j]
            if cell.fill == True:
                cell.switch()
                cell.draw()
            cell.fill == False

def numOfNeighbors(x, y):
    cell = grid.grid[x][y]
    print(cell.fill)


''' def update():
     temp = []
     for i in range(board_height - 2):
         temp.append([0] * board_width)

     for i in range(board_height - 2):
         for j in range(baord_width - 2):
             cell = grid.grid[i][j]
             if cell.fill == True'''

gui = Tk()
gui.title = "Game of Life"
frame = Frame(gui)
frame.pack(side = "bottom")
RandomPopulate = Button(frame, text = "Populate", command = populate)
RandomPopulate.grid(row = 0, column = 0, rowspan = 2, sticky = "W", padx = (0, 0))
Next = Button(frame, text = "Next Generation", repeatdelay = 1, repeatinterval = 1, command = lambda: numOfNeighbors(2, 2))
Next.grid(row = 0, column = 1, sticky = "W")
Clear = Button(frame, text = "Clear Memory", command = clear)
Clear.grid(row = 0, column = 100, sticky = "E")
Exit = Button(frame, text = "Exit", command = lambda: gui.destroy())
Exit.grid(row = 0, column = 101, sticky = "E")
grid = CellGrid(gui, 5, 5, 20)
grid.pack()

gui.mainloop()
