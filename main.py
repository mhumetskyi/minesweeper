import tkinter as tk

from play_button import PlayButton

from menu import MainMenu


class App(tk.Tk):
    def __init__(self):
        super().__init__()
        self.geometry("700x600")
        self.title("Minesweeper")
        play_button = PlayButton()
        play_button.pack()

        menu = MainMenu()
        self.config(menu=menu)


if __name__ == "__main__":
    app = App()
    app.mainloop()
