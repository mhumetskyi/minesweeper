import tkinter as tk
from cube import Cube
from random import shuffle


class PlayField(tk.Frame):

    ROWS = 8
    COLUMNS = 8
    MINES = 15

    def __init__(self, rows, columns):
        super().__init__()
        self.rows = rows
        self.columns = columns

        self.generate_field()
        self.create_widgets()
        self.insert_mines()

        self.count_mines_in_buttons()

        self.count_mines_in_buttons()
        self.print_button()

    def generate_field(self):
        self.buttons = []
        for row in range(self.rows + 2):
            temp = []
            for column in range(self.columns + 2):
                button = Cube(self, x=row, y=column)
                button.config(command=lambda btn=button: self.click(btn))

                temp.append(button)

            self.buttons.append(temp)

    def create_widgets(self):
        for row in range(1, self.rows + 1):
            for column in range(1, self.columns + 1):
                button = self.buttons[row][column]
                button.grid(row=row, column=column)

    def open_all_buttons(self):
        for row in range(self.rows + 2):
            for column in range(self.columns + 2):
                button = self.buttons[row][column]
                if button.mine:
                    button.config(text="*", background="red")
                else:
                    button.config(text=button.count_bomb, background="gray")

                    if button.count_bomb:
                        button.config(text=button.count_bomb, background="gray")
                    else:
                        button.config(text="", background="gray")

    def print_button(self):
        for row in range(1, self.rows + 1):
            for column in range(1, self.columns + 1):
                button = self.buttons[row][column]
                if button.mine:
                    print("B", end="")
                else:
                    print(button.count_bomb, end="")
            print()

    def click(self, clicked_button: Cube):
        print(clicked_button)
        if clicked_button.mine:
            clicked_button.config(text="*", background="red")
            self.open_all_buttons()
        else:
            if clicked_button.count_bomb:
                clicked_button.config(text=clicked_button.count_bomb, background="gray")
            else:
                clicked_button.config(text="", background="gray")

    def insert_mines(self):
        index_mines = self.get_places()
        print(index_mines)
        count = 1
        for row in range(1, self.rows + 1):
            for column in range(1, self.columns + 1):
                button = self.buttons[row][column]
                button.number = count
                if button.number in index_mines:
                    button.mine = True
                count += 1

    def count_mines_in_buttons(self):
        for row in range(1, self.rows + 1):
            for column in range(1, self.columns + 1):
                button = self.buttons[row][column]
                count_bomb = 0
                if not button.mine:
                    for row_dx in [-1, 0, 1]:
                        for col_dx in [-1, 0, 1]:
                            neighbour = self.buttons[row + row_dx][column + col_dx]
                            if neighbour.mine:
                                count_bomb += 1
                button.count_bomb = count_bomb

    @staticmethod
    def get_places():
        indexes = list(range(1, PlayField.ROWS * PlayField.COLUMNS + 1))
        shuffle(indexes)
        return indexes[: PlayField.MINES]

    def generate_fields(self, rows, columns):
        for row in range(rows):
            temp = []
            for column in range(columns):
                button = Cube(self, x=row, y=column)
                button.config(command=lambda btn=button: self.click(btn))
                button.grid(row=row, column=column)
                temp.append(button)
            self.buttons.append(temp)

    def destroy_buttons(self):

        for button in self.winfo_children():
            button.destroy()
