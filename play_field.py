import tkinter as tk


class PlayField(tk.Frame):
    def __init__(self):
        super().__init__()
        self.list = []

    def generate_field(self, rows, columns):
        for row in range(rows):
            for column in range(columns):
                button = tk.Button(self)
                button.grid(row=row, column=column)
                self.my_button = [button]

    def destroy_buttons(self):
        self.destroy(self.my_button)

