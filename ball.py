from tkinter import *
import time
import random
class Ball:
    def __init__(self, canvas: Canvas):
        self.canvas = canvas
        self.speed_x = random.randint(-2, 2)
        self.speed_y = random.randint(-2, 2)
        self.create_ball()
    def create_ball(self):
        self.id = self.canvas.create_oval(50, 50, 100, 100, fill='red')
    def move(self):
        canvas.move(self.id, self.speed_x, self.speed_y)
        coord = canvas.coords(self.id)
        print(coord)
        if coord[0] <= 0 or coord[0] >= 500:
            self.speed_x *= -1
        if coord[2] <= 0 or coord[2] >= 500:
            self.speed_x *= -1
        if coord[1] <= 0 or coord[1] >= 500:
            self.speed_y *= -1
        if coord[3] <= 0 or coord[3] >= 500:
            self.speed_y *= -1







root= Tk()
root.geometry('600x600')
WIGHT = 600
HEIGHT = 600
INDENT = 50
canvas = Canvas(root, height= WIGHT - 2 * INDENT, width= HEIGHT - 2 * INDENT, bg= 'azure')
canvas.place(x = INDENT, y = INDENT)
ball = Ball(canvas)
while True:
    ball.move()
    time.sleep(0.05)
    root.update()
root.mainloop()
