import random as rd
import tkinter as tk

scl = 1

class player:
    def __init__(self, num, canvas):
        self.canvas = canvas
        self.xspeed = 0

        if num == 1:
            self.y = 25
        else:
            self.y = 575

        self.image = self.canvas.create_rectangle(250, self.y+5, 350, self.y-5, fill='white', tags = (f"player {num}"))

    def move(self):
        self.coordinates = self.canvas.coords(self.image)
        if(self.coordinates[2]>=590):
            if(self.xspeed == 5):
                self.xspeed = 0
            else:
                self.canvas.move(self.image, self.xspeed, 0)
        elif(self.coordinates[0]<=10):
            if(self.xspeed == -5):
                self.xspeed = 0
            else:
                self.canvas.move(self.image, self.xspeed, 0)
        else:
            self.canvas.move(self.image, self.xspeed, 0)
            

class ballGame:
    def __init__(self, canvas):
        self.canvas = canvas
        self.x = 300
        self.y = 300
        self.xspeed = rd.randint(-5,5)*scl
        self.yspeed = rd.randint(-5,5)*scl
        while self.yspeed == 0:
            self.yspeed = rd.randint(-5, 5)*scl

        self.image = canvas.create_oval(285, 315, 315, 285, fill = 'gray', outline='gray')
 
   
    def move(self):
        coordinates = self.canvas.coords(self.image)

        if(coordinates[2]>=600 or coordinates[0]<0):
            self.xspeed = self.xspeed*(-1)
        if(coordinates[3]>=600 or coordinates[1]<0):
            self.yspeed = self.yspeed*(-1)

        self.canvas.move(self.image, self.xspeed, self.yspeed)