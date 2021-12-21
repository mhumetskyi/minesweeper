import tkinter as tk


class MainMenu(tk.Menu):
    def __init__(self, play_field):
        super().__init__()
        self.play_field = play_field


        levels_menu = tk.Menu(self, tearoff=0)
        levels_menu.add_command(label="Легко", command=self.easy_click)
        levels_menu.add_command(label="Нормально",command=self.normal_click)
        levels_menu.add_command(label="Складно",command=self.hard_click)

        game_menu = tk.Menu(self, tearoff=0)
        game_menu.add_command(label="Початок гри")
        game_menu.add_cascade(label="Складність", menu=levels_menu)
        game_menu.add_command(label="Вихід", command=quit)

        self.add_cascade(label="Гра", menu=game_menu)

    def quit(self):
        self.destroy()

    def easy_click(self):
        self.play_field.generate_field(rows=5, columns=5)

    def normal_click(self):
        self.play_field.generate_field(rows=10, columns=10)
        self.play_field.destroy_buttons()
    def hard_click(self):
        self.play_field.generate_field(rows=15, columns=15)
