import tkinter as tk


class PlayField(tk.Frame):
    def __init__(self):
        super().__init__()
        self.buttons = []

    def generate_field(self, rows, columns):
        for row in range(rows):
            temp = []
            for column in range(columns):
                button = tk.Button(self)
                button.grid(row=row, column=column)
                temp.append(button)
            self.buttons.append(temp)

    def destroy_buttons(self):
        for button in self.winfo_children():
            button.destroy()
