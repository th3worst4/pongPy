import random as rd
import tkinter as tk
from playsound import playsound
import threading

scl = 2

class player:
    def __init__(self, num, canvas, vel):
        self.score = 0

        self.canvas = canvas
        self.xspeed = 0
        self.vel = vel

        if num == 1:
            self.y = 25
        else:
            self.y = 575

        self.image = self.canvas.create_rectangle(250, self.y+5, 350, self.y-5, fill='white', tags = (f"player {num}"))

    def move(self):
        self.coordinates = self.canvas.coords(self.image)
        if(self.coordinates[2]>=590):
            if(self.xspeed == self.vel):
                self.xspeed = 0
            else:
                self.canvas.move(self.image, self.xspeed, 0)
        elif(self.coordinates[0]<=10):
            if(self.xspeed == -self.vel):
                self.xspeed = 0
            else:
                self.canvas.move(self.image, self.xspeed, 0)
        else:
            self.canvas.move(self.image, self.xspeed, 0)
            

class ballGame:
    def __init__(self, canvas):
        self.canvas = canvas
        self.canvas.pack()
        self.xspeed = rd.randint(-5,5)*scl
        self.yspeed = rd.randint(-5,5)*scl
        while abs(self.yspeed)<3:
            self.yspeed = rd.randint(-5, 5)*scl

        self.image = canvas.create_oval(285, 315, 315, 285, fill = 'gray', outline='gray')
        self.canvas.pack()
 
   
    def move(self):
        ballCoords = self.canvas.coords(self.image)

        if(ballCoords[2]>=590 or ballCoords[0]<10):
            self.xspeed = self.xspeed*(-1)
            threading.Thread(target=playsound, args=("sounds/2.wav",), daemon=True).start()
        

        self.canvas.move(self.image, self.xspeed, self.yspeed)

    def collision(self, p1, p2):
        coordinates =  [p1.canvas.coords(p1.image), p2.canvas.coords(p2.image)]
        ballCoords = self.canvas.coords(self.image)

        if(coordinates[0][0]<=ballCoords[2] and coordinates[0][2]>=ballCoords[0]):
            if(coordinates[0][3]>=ballCoords[1]):
                self.yspeed = abs(self.yspeed)+rd.randint(0,1)*scl
                self.xspeed = self.xspeed + p1.xspeed*0.25
                threading.Thread(target=playsound, args=("sounds/1.wav",), daemon=True).start()
        
        if(coordinates[1][0]<=ballCoords[2] and coordinates[1][2]>=ballCoords[0]):
            if(coordinates[1][1]<=ballCoords[3]):
                self.yspeed = (abs(self.yspeed)+rd.randint(0,1)*scl)*(-1)
                self.xspeed = self.xspeed + p2.xspeed*0.25 
                threading.Thread(target=playsound, args=("sounds/1.wav",), daemon=True).start()

    def delete(self):
        self.canvas.delete(self.image)
        threading.Thread(target=playsound, args=("sounds/3.mp3",), daemon=True).start()