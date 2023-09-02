import tkinter as tk
from tkinter import ttk
import time

from elements import player, ballGame

def onKeyPress(event):
    vel = 5
    match event.keycode:
        case 65:
            if p1.xspeed == -5:
                pass
            else:
                p1.xspeed -= vel
        case 68:
            if p1.xspeed == 5:
                pass
            else:
                p1.xspeed += vel
        case 37:
            if p2.xspeed == -5:
                pass
            else:
                p2.xspeed -= vel
        case 39:
            if p2.xspeed == 5:
                pass
            else:
                p2.xspeed += vel


root = tk.Tk()
root.title("Pong in Python3")
root.resizable(width=False, height=False)

mainframe = tk.Canvas(root, width=600, height=600, background="black")
mainframe.pack()
mainframe.grid(column=0, row=0, sticky=(tk.N, tk.W, tk.E, tk.S))
mainframe.create_line(0, 300, 600, 300, fill='white')

p1 = player(1, mainframe)
p2 = player(2, mainframe)

newBall = ballGame(mainframe)



while True:
    root.bind('<KeyPress>', onKeyPress)
    newBall.move()
    p1.move()
    p2.move()
    root.update()
    time.sleep(0.067)
    
root.mainloop()