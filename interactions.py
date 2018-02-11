from cell import Cell
from cellgrid import CellGrid
from tkinter import Tk, Frame, Button, Toplevel
import tkinter.messagebox
from random import randint
from popups import popupInput, popupGate
from spawners import *

board_height = 80
board_width = 80

def populate():
    for i in range(board_height//2):
        x, y = randint(0, board_height - 2), randint(0, board_width - 2)
        cell = grid.grid[x][y]
        print(x, y)
        if cell.fill == False:
            cell._switch()
            cell.draw()

def clear():
    for i in range(board_height - 1):
        for j in range(board_width - 1):
            cell = grid.grid[i][j]
            if cell.fill == True:
                cell._switch()
                cell.draw()
            cell.fill == False

def numOfNeighbors(x, y):
    count = 0
    for i in range(x - 1, x + 2):
        for j in range(y - 1, y + 2):
            try:
                cell = grid.grid[i][j]
                if cell.fill == True and ((i >= 0 and j >= 0) and (i < board_height and j < board_width)):
                    count += 1
            except IndexError:
                pass
    if grid.grid[x][y].fill == True:
        count -= 1
    return count


def update():
    to_toggle = []
    for i in range(board_height - 1):
        for j in range(board_width - 1):
            cell = grid.grid[i][j]
            #print("(" + str(i) + ", " + str(j) + "): " + str(numOfNeighbors(i, j)))
            n = numOfNeighbors(i, j)
            if cell.fill == False and n == 3:
                to_toggle.append((i, j))
            elif cell.fill == True and n != 3 and n != 2:
                to_toggle.append((i, j))
    for coord in to_toggle:
        cell = grid.grid[coord[0]][coord[1]]
        cell._switch()
        cell.draw()

def chooseGate():
    popup = popupGate(frame)
    gui.wait_window(popup.top)
    gate = popup.gate
    print(gate)

gui = Tk()
gui.title = "Game of Life"
frame = Frame(gui)
frame.pack(side = "bottom")
RandomPopulate = Button(frame, text = "Populate", command = populate)
RandomPopulate.grid(row = 0, column = 0, rowspan = 2, sticky = "W", padx = (0, 0))
Logic = Button(frame, text = "Demonstrate Logic Gates", command = chooseGate)
Logic.grid(row = 0, column = 5, rowspan = 2, sticky = "W")
Next = Button(frame, text = "Next Generation", repeatdelay = 1, repeatinterval = 1, command = update)
Next.grid(row = 0, column = 1, sticky = "W")
Clear = Button(frame, text = "Clear Memory", command = clear)
Clear.grid(row = 0, column = 100, sticky = "E")
Exit = Button(frame, text = "Exit", command = lambda: gui.destroy())
Exit.grid(row = 0, column = 101, sticky = "E")
grid = CellGrid(gui, board_height, board_width, 10)
grid.pack()

gui.mainloop()
