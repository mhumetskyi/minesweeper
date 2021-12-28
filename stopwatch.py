import tkinter as tk


class Stopwatch(tk.Label):
    def __init__(self):
        super().__init__(text="0", font=("Helvetica", 20), fg="black")

        self.cancel_id = None

    def start_watch(self):
        now = self["text"]
        next_value = int(now) + 1
        self.configure(text=next_value)
        self.cancel_id = self.after(1000, self.start_watch)

    def reset(self):
        self.configure(text="0")
        self.stop_watch()
        self.start_watch()

    def stop_watch(self):
        self.after_cancel(self.cancel_id)
