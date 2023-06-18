from tkinter import *
import time
import random
class Ball:
    def __init__(self, canvas: Canvas):
        global ball_list
        self.canvas = canvas
        self.speed_x = random.randint(-2, 2)
        self.speed_y = random.randint(-2, 2)
        self.create_ball()
    def create_ball(self):
        self.id = self.canvas.create_oval(50, 50, 100, 100, fill='red')
    def move(self):
        canvas.move(self.id, self.speed_x, self.speed_y)
        coord= self.coord_show()
        if coord[0] <= 0 or coord[0] >= 500:
            self.speed_x *= -1
        if coord[2] <= 0 or coord[2] >= 500:
            self.speed_x *= -1
        if coord[1] <= 0 or coord[1] >= 500:
            self.speed_y *= -1
        if coord[3] <= 0 or coord[3] >= 500:
            self.speed_y *= -1
    def coord_show(self):
        return self.canvas.coords(self.id)
    def change_color(self):
        self.canvas.itemconfig(self.id, fill= 'orange')
    def delete_ball(self):
        global ball_list
        for i in range(2):
             ball_list.append(Ball(canvas))
        ball_list.pop(self.id - 1)
        self.canvas.delete(self.id)

    
def mouse_click(event):
    global ball_list
    x = event.x 
    y = event.y
    coord_mouse = [x, y]
    print(coord_mouse)
    for ball in ball_list:
        coord_ball = ball.coord_show()
        if x >= coord_ball[0] and x <= coord_ball[2] and y <= coord_ball[3] and y >= coord_ball[1]:
            ball.delete_ball()
            print(ball_list)

            
    
    

        


root = Tk()
root.geometry('600x600')
WIGHT = 600
HEIGHT = 600
INDENT = 50
canvas = Canvas(root, height= WIGHT - 2 * INDENT, width= HEIGHT - 2 * INDENT, bg= 'azure')
canvas.place(x = INDENT, y = INDENT)
ball_list = [Ball(canvas), Ball(canvas), Ball(canvas)]
root.bind('<Button-1>', mouse_click)
while True:
    for ball in ball_list:
        ball.move()
    time.sleep(0.05)
    root.update()
root.mainloop()
