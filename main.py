from cell import Cell
from cellgrid import CellGrid
from tkinter import Tk, Frame, Button, Toplevel, ttk, Listbox
import tkinter.messagebox
from random import randint
from spawners import spawnGlider, spawnReverseGlider, spawnEaterOr, spawnEaterAnd, spawnEaterNot
import AND, OR, NOT, os

board_height = 80
board_width = 158
#board_height = 50
#board_width = 100


def populate():
    for i in range(board_height//2):
        x, y = randint(0, board_height - 2), randint(0, board_width - 2)
        cell = grid.grid[x][y]
        # print(x, y)
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


def toToggle(i, j):
    cell = grid.grid[i][j]
    n = numOfNeighbors(i, j)
    if cell.fill == False and n == 3:
        return True
    elif cell.fill == True and n != 3 and n != 2:
        return True

def updateCell(i, j):
    cell = grid.grid[i][j]
    if toToggle(i, j) == True:
        return (i, j)

def update():
    toggle = []
    for i in range(board_height - 1):
        for j in range(board_width - 1):
            toggle.append(updateCell(i, j))
    for coord in toggle:
        try:
            cell = grid.grid[coord[0]][coord[1]]
            cell._switch()
            cell.draw()
        except TypeError:
            pass
    del toggle[::]


    
def popupmsg(msg):   
    def showSimulation(x):
        print(x)
        for i in x:
            print(listbox.get(i))
            
    popup = Tk()
    popup.wm_title("!")
    listbox = Listbox(popup)
    listbox.pack()

    listbox.insert(1, "AND 0-0")
    listbox.insert(2, "AND 0-1")
    listbox.insert(3, "AND 1-0")
    listbox.insert(4, "AND 1-1")
    listbox.insert(5, "OR 0-0")
    listbox.insert(6, "OR 0-1")
    listbox.insert(7, "OR 1-0")
    listbox.insert(8, "OR 1-1")
    listbox.insert(9, "NOT 0")
    listbox.insert(10, "NOT 1")
    

    B1 =  ttk.Button(popup, text = "Simulate", command = showSimulation(listbox.curselection()))
    B1.pack()
    
    B2 = ttk.Button(popup, text = "Exit", command = popup.destroy)
    B2.pack()
    
    popup.mainloop()

# def orPressed():
#     Or.configure(state = "disabled")
#     Not.configure(state = "disabled")
#     And.configure(state = "disabled")
#     # toSpawn = []
#     # toSpawn.append(spawnGlider(1, 0))
#     # toSpawn.append(spawnGlider(1, 40))
#     # toSpawn.append(spawnGlider(1, 80))
#     # toSpawn.append(spawnReverseGlider(3, 120))
#     # toSpawn.append(spawnEaterOr())
#     # for listemt in toSpawn:
#     #     for emt in listemt:
#     #         cell = grid.grid[emt[0]][emt[1]]
#     #         if cell.fill == True:
#     #             pass
#     #         else:
#     #             cell._switch()
#     #             cell.draw()
#     # del toSpawn[::]
#     os.system('python OR.py')
#
#
# def AndPressed():
#     Or.configure(state = "disabled")
#     Not.configure(state = "disabled")
#     And.configure(state = "disabled")
#     # toSpawn = []
#     # toSpawn.append(spawnGlider(1, 0))
#     # toSpawn.append(spawnGlider(0, 40))
#     # toSpawn.append(spawnReverseGlider(3, 90))
#     # toSpawn.append(spawnEaterOr())
#     # for listemt in toSpawn:
#     #     for emt in listemt:
#     #         cell = grid.grid[emt[0]][emt[1]]
#     #         if cell.fill == True:
#     #             pass
#     #         else:
#     #             cell._switch()
#     #             cell.draw()
#     # del toSpawn[::]
#     os.system('python AND.py')
#
# def NotPressed():
#     Or.configure(state = "disabled")
#     Not.configure(state = "disabled")
#     And.configure(state = "disabled")
#     # toSpawn = []
#     # toSpawn.append(spawnGlider(1, 0))
#     # toSpawn.append(spawnReverseGlider(3, 40))
#     # toSpawn.append(spawnEaterNot())
#     # for listemt in toSpawn:
#     #     for emt in listemt:
#     #         cell = grid.grid[emt[0]][emt[1]]
#     #         if cell.fill == True:
#     #             pass
#     #         else:
#     #             cell._switch()
#     #             cell.draw()
#     # del toSpawn[::]
#     os.system('python NOT.py')
#
def enableButtons():
    # Or.configure(state = "normal")
    # Not.configure(state = "normal")
    # And.configure(state = "normal")
    clear()


gui = Tk()
gui.title = "Game of Life"
frame = Frame(gui)
frame.pack(side = "bottom")
RandomPopulate = Button(frame, text = "Populate", command = populate)
RandomPopulate.grid(row = 0, column = 0)
Logic = Button(frame, text = "Demonstrate Logic Gates", command = lambda: popupmsg("Hello"))
Logic.grid(row = 0, column = 2)
# And = Button(frame, text = "AND", command = AndPressed  )
# And.grid(row = 1, column = 2, sticky = "E")
# Or = Button(frame, text = "OR", command = orPressed)
# Or.grid(row = 1, column = 2)
# Not = Button(frame, text = "NOT", command = NotPressed)
# Not.grid(row = 1, column = 2, sticky = "W")
# Next = Button(frame, text = "Next Generation", command = update)
Next = Button(frame, text = "Next Generation", repeatdelay = 1, repeatinterval = 1, command = update)
Next.grid(row = 0, column = 1)
Clear = Button(frame, text = "Clear Memory", command = clear)
Clear.grid(row = 0, column = 3)
Exit = Button(frame, text = "Exit", command = lambda: gui.destroy())
Exit.grid(row = 0, column = 4)
grid = CellGrid(gui, board_height, board_width, 10)
grid.pack()

# Or.configure(state = "disabled")
# Not.configure(state = "disabled")
# And.configure(state = "disabled")

gui.mainloop()
