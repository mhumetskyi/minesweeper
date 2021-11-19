import tkinter as tk


class App(tk.Tk):
    def __init__(self):
        super().__init__()
        self.geometry("700x600")
        self.title("Minesweeper")


if __name__ == "__main__":
    app = App()
    app.mainloop()
