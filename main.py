import tkinter as tk

from menu import MainMenu
from play_button import PlayButton
from play_field import PlayField


class App(tk.Tk):
    ROWS = 10
    COLUMNS = 10

    def __init__(self):
        super().__init__()
        self.geometry("700x600")
        self.title("Minesweeper")

        play_button = PlayButton()
        play_button.pack()

        menu = MainMenu()
        self.config(menu=menu)

        play_field = PlayField(self.ROWS, self.COLUMNS)
        play_field.pack(pady=10)


if __name__ == "__main__":
    app = App()
    app.mainloop()
