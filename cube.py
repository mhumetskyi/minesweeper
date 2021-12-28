import tkinter as tk


class Cube(tk.Button):
    def __init__(self, master, x, y, number=0, *args, **kwargs):
        super(Cube, self).__init__(master, width=6, height=3, *args, **kwargs)
        self.x = x
        self.y = y
        self.number = number
        self.mine = False
        self.count_bomb = 0

    def __repr__(self):
        return f"Cube {self.x} {self.y} {self.number}, {self.mine}"
