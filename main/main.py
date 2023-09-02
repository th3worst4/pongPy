import tkinter as tk
from tkinter import ttk

from elements import player, ballGame

def onKeyPress(event):
    match event.keycode:
        case 65:
            p1.xspeed -=1
        case 68:
            p1.xspeed +=1
        case 37:
            p2.xspeed -= 1
        case 39:
            p2.xspeed +=1


root = tk.Tk()
root.title("Pong in Python3")

mainframe = tk.Canvas(root, width=600, height=600, background="black")
mainframe.grid(column=0, row=0, sticky=(tk.N, tk.W, tk.E, tk.S))
mainframe.create_line(0, 300, 600, 300, fill='white')

p1 = player(1, mainframe)
p2 = player(2, mainframe)

newBall = ballGame(mainframe)

root.bind('<KeyPress>', onKeyPress)
root.mainloop()