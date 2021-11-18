from tkinter import *


class Window:

    root = Tk()
    root.title("Minesweeper")
    root.geometry("700x600")

    def __init__(self):
        pass

    def start(self):

        Window.root.mainloop()


game = Window()
game.start()
