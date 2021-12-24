import tkinter as tk
from menu import MainMenu
from play_button import PlayButton
from play_field import PlayField
from stopwatch import Stopwatch

class App(tk.Tk):


    def __init__(self):
        super().__init__()
        self.geometry("700x600")
        self.title("Minesweeper")

        play_button = PlayButton()
        play_button.pack()
        play_button.configure(command=self.on_play_button_click)

        menu = MainMenu()
        self.config(menu=menu)

        play_field = PlayField(PlayField.ROWS, PlayField.COLUMNS)
        play_field.pack(pady=10)

        self.stopwatch = Stopwatch()
        self.stopwatch.pack()
        self.stopwatch.start_watch()

    def on_play_button_click(self):
        self.stopwatch.reset()



if __name__ == "__main__":
    app = App()
    app.mainloop()
