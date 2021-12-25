import tkinter as tk

class Stopwatch(tk.Label):
    def __init__(self):
        super().__init__(text="0", font=("Helvetica", 20), fg="black")

    def start_watch(self):
        now = self["text"]
        next_value = int(now) + 1
        self.configure(text=next_value)
        self.after(1000, self.start_watch)

    def reset(self):
        self.configure(text="0")


