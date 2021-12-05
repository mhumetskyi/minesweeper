import tkinter as tk


class PlayField(tk.Frame):
    def __init__(self, rows, columns):
        super().__init__()
        self.rows = rows
        self.columns = columns
        self.generate_field()

    def generate_field(self):
        for row in range(self.rows):
            for column in range(self.columns):
                button = tk.Button(self)
                button.grid(row=row, column=column)
