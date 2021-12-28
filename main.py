import tkinter as tk

from menu import MainMenu
from play_button import PlayButton
from play_field import PlayField
from stopwatch import Stopwatch


class App(tk.Tk):
    def __init__(self):
        super().__init__()
        self.geometry("700x700")
        self.title("Minesweeper")

        play_button = PlayButton()
        play_button.pack()
        play_button.configure(command=self.on_play_button_click)

        self.stopwatch = Stopwatch()
        self.stopwatch.start_watch()

        self.play_field = PlayField(PlayField.ROWS, PlayField.COLUMNS, self.stopwatch)
        self.play_field.pack(pady=10)

        self.stopwatch.pack()

        menu = MainMenu(self.play_field)
        self.config(menu=menu)

    def on_play_button_click(self):
        self.stopwatch.reset()

        self.play_field.destroy_buttons()
        self.play_field.generate_field()
        self.play_field.create_widgets()
        self.play_field.insert_mines()
        self.play_field.count_mines_in_buttons()


if __name__ == "__main__":
    app = App()
    app.mainloop()
