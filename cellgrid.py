from cell import Cell
from tkinter import Tk, Canvas
from random import randint
class CellGrid(Canvas):
    def __init__(self, master, rowNumber, columnNumber, cellSize):
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
        for row in self.grid:
            for cell in row:
                cell.draw()

    def _eventCoords(self, event):
        row = int(event.y / self.cellSize)
        column = int(event.x / self.cellSize)
        return row, column

    def handleMouseClick(self, event):
        row, column = self._eventCoords(event)
        cell = self.grid[row][column]
        cell._switch()
        cell.draw()
        #print(row, column)
