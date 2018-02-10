class Cell():
    FILLED_COLOR_BG = "green"
    EMPTY_COLOR_BG = "white"
    FILLED_COLOR_BORDER = "green"
    EMPTY_COLOR_BORDER = "black"

    def __init__(self, master, x, y, size):
        self.master = master
        self.x = x
        self.y = y
        self.size = size
        self.fill = False

    def switch(self):
        self.fill = not self.fill

    def draw(self):
        if self.master != None:
            if self.fill == True:
                fill = Cell.FILLED_COLOR_BG
                outline = Cell.FILLED_COLOR_BORDER
            if self.fill == False:
                fill = Cell.EMPTY_COLOR_BG
                outline = Cell.EMPTY_COLOR_BORDER

            xmin = self.x * self.size
            xmax = xmin + self.size
            ymin = self.y * self.size
            ymax = ymin + self.size

            self.master.create_rectangle(xmin, ymin, xmax, ymax, fill = fill, outline = outline)
