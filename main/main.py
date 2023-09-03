import tkinter as tk
import time

from elements import player, ballGame

vel = 12
score1 = None
score2 = None

def onKeyPress(event):
    match event.keycode:
        case 65:
            p1.xspeed = -vel
        case 68:
            p1.xspeed = vel
        case 37:
            p2.xspeed = -vel
        case 39:
            p2.xspeed = vel

def releaseKey(event):
    if (event.keycode == 65 or event.keycode == 68):
        p1.xspeed = 0
    if (event.keycode == 37 or event.keycode == 39):
        p2.xspeed = 0

root = tk.Tk()
root.title("Pong in Python3")
root.resizable(width=False, height=False)

mainframe = tk.Canvas(root, width=600, height=600, background="black")
mainframe.pack()
mainframe.grid(column=0, row=0, sticky=(tk.N, tk.W, tk.E, tk.S))
mainframe.create_line(0, 300, 600, 300, fill='white')

p1 = player(1, mainframe, vel)
p2 = player(2, mainframe, vel)

newBall = ballGame(mainframe)

def score(mainframe, p1, p2, score1, score2):
    if(score1 != None or score2 != None):
        mainframe.delete(score1)
        mainframe.delete(score2)
        score1 = mainframe.create_text(557, 125, text=p1.score, anchor="center", font=("Atari", 40), fill="white")
        score2 = mainframe.create_text(557, 430, text=p2.score, anchor="center", font=("Atari", 40), fill="white")
    else:
        score1 = mainframe.create_text(557, 125, text=p1.score, anchor="center", font=("Atari", 40), fill="white")
        score2 = mainframe.create_text(557, 430, text=p2.score, anchor="center", font=("Atari", 40), fill="white")

    return (score1, score2)



def ballDeath(newBall, mainframe, p1, p2):
    ballCoords = newBall.canvas.coords(newBall.image)
    if(ballCoords[3]>=615):
        p1.score += 1
        newBall.delete()
        newBall = ballGame(mainframe)
        time.sleep(1)

    elif(ballCoords[1]<-15):
        p2.score += 1
        newBall.delete()
        newBall = ballGame(mainframe)
        time.sleep(1)
    
    return newBall

def close(event):
    root.destroy()

while True:
    root.bind('<KeyPress>', onKeyPress)
    root.bind('<KeyRelease>', releaseKey)
    
    newBall = ballDeath(newBall, mainframe, p1, p2)
    (score1, score2) = score(mainframe, p1, p2, score1, score2)
    newBall.collision(p1, p2)
    
    newBall.move()

    p1.move()
    p2.move()
    
    root.update()
    root.bind('<Escape>', close)
    time.sleep(0.05)
    