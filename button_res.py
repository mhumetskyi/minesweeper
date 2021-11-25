import tkinter as tk


class App(tk.Tk):
    def __init__(self):
        super().__init__()
        self.geometry("700x600")
        self.title("Minesweeper")
        but1 = Button_play()
        but1.pack()


class Button_play(tk.Button):
    def __init__(self):
        super().__init__(text="START", font=(None, 12))


if __name__ == "__main__":
    app = App()
    app.mainloop()
