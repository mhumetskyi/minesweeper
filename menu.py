import tkinter as tk
from play_field import PlayField


class MainMenu(tk.Menu):
    def __init__(self, play_field):
        super().__init__()
        self.play_field = play_field

        levels_menu = tk.Menu(self, tearoff=0)
        levels_menu.add_command(label="Легко", command=self.easy_click)
        levels_menu.add_command(label="Нормально", command=self.normal_click)
        levels_menu.add_command(label="Складно", command=self.hard_click)

        game_menu = tk.Menu(self, tearoff=0)
        game_menu.add_cascade(label="Складність", menu=levels_menu)
        game_menu.add_command(label="Вихід", command=quit)

        self.add_cascade(label="Гра", menu=game_menu)

    def quit(self):
        self.destroy()

    def easy_click(self):
        PlayField.ROWS = 6
        PlayField.COLUMNS = 6
        PlayField.MINES = 10

        self.play_field.destroy_buttons()
        self.play_field.rows = 6
        self.play_field.columns = 6

        self.play_field.generate_field()
        self.play_field.create_widgets()
        self.play_field.insert_mines()

        self.play_field.count_mines_in_buttons()

    def normal_click(self):
        PlayField.ROWS = 8
        PlayField.COLUMNS = 8
        PlayField.MINES = 15

        self.play_field.destroy_buttons()
        self.play_field.rows = 8
        self.play_field.columns = 8

        self.play_field.generate_field()
        self.play_field.create_widgets()
        self.play_field.insert_mines()

        self.play_field.count_mines_in_buttons()

    def hard_click(self):
        PlayField.ROWS = 10
        PlayField.COLUMNS = 10
        PlayField.MINES = 20

        self.play_field.destroy_buttons()
        self.play_field.rows = 10
        self.play_field.columns = 10

        self.play_field.generate_field()
        self.play_field.create_widgets()
        self.play_field.insert_mines()

        self.play_field.count_mines_in_buttons()
