import random as rd
import tkinter as tk

scl = 1

class player:
    def __init__(self, num, canvas):
        self.x = 300
        self.xspeed = 0

        if num == 1:
            self.y = 25
        else:
            self.y = 575

        self.canvas = canvas.create_rectangle(250, self.y+5, 350, self.y-5, fill='white', tags = (f"player {num}"))
    def pos(self):
        self.x = self.x + self.xspeed

class ballGame:
    def __init__(self, canvas):
        self.x = 300
        self.y = 300
        self.xspeed = rd.randint(-5,5)*scl
        self.yspeed = rd.randint(-5,5)*scl
        while self.yspeed == 0:
            self.yspeed = rd.randint(-5, 5)*scl

        self.canvas = canvas.create_oval(285, 315, 315, 285, fill = 'gray', outline='gray')

    def pos(self):
        self.x = self.x + self.xspeed
        self.y = self.y + self.yspeed

    def wallcolision(self):
        if self.x == 0 or self.x == 600:
            self.xspeed*=(-1)
            self.yspeed = self.yspeed + rd.randint(0,1)*scl

        if self.y == 0 or self.y == 600:
            self.yspeed*=(-1)
            self.xspeed = self.xspeed + rd.randint(0,1)*scl