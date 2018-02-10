from tkinter import *

class popupInput:
    def __init__(self, parent):
        top = self.top = Toplevel(parent)
        self.Label = Label(top, text = 'Enter number of organisms')
        self.Label.pack()
        self.EntryBox = Entry(top)
        self.EntryBox.pack()
        self.SubmitButton = Button(top, text = 'Sumbit', command = self.send)
        self.SubmitButton.pack()
    def send(self):
        self.number = self.EntryBox.get()
        self.top.destroy()
