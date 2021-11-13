from tkinter import *

root = Tk()
root.geometry('700x600')
root.title('Minesweeper')

def new_game():
    return

def diff_easy():
    return
def diff_normal():
    return
def diff_hard():
    return
def exit():
     return
mainmenu = Menu(root)
root.config(menu = mainmenu)

filemenu = Menu(mainmenu, tearoff = 0)
filemenu2 = Menu(mainmenu, tearoff = 0)

filemenu.add_command(label="Початок гри", command = new_game)
filemenu.add_cascade(label="Складність", menu = filemenu2)
filemenu.add_command(label="Вихід", command = exit)

filemenu2.add_command(label="Легко", command = diff_easy)
filemenu2.add_command(label="Нормально", command = diff_normal)
filemenu2.add_command(label="Складно", command = diff_hard)


mainmenu.add_cascade(label = 'Гра', menu = filemenu)

root.mainloop()