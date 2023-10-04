from tkinter import *
import time
import random as r
tk = Tk()
w, h = 600, 560
cv = Canvas(tk, width=w, height=h)
cv.pack()
tk.title("贪吃蛇")
tk.wm_attributes("-topmost", 1)
tk.resizable(0, 0)
class body():
    def __init__(self, x1, y1, cv, colour):
        self.big = 20
        self.cv = cv
        self.x1 = x1
        self.y1 = y1
        self.x2 = x1 + self.big
        self.y2 = y1 + self.big
        self.colour = colour
        self.id = cv.create_rectangle(self.x1, self.y1, self.x2, self.y2, fill=self.colour)

class food(body):
    pass

rx, ry = r.choice(list(range(20, w-20, 20))), r.choice(list(range(20, h-20, 20)))
food1 = food(rx, ry, cv, 'red')
first = body(220, 300, cv, 'green')
bodies = [first]
x, y = first.x1, first.y1
towards = 'u'
long = 10
die = False
t = 0.1

def move(event):
    global x
    global y
    global towards
    if event.keysym == 'Left':
        if towards == 'r':
            pass
        else:
            towards = 'l'
    elif event.keysym == 'Right':
        if towards == 'l':
            pass
        else:
            towards = 'r'
    elif event.keysym == 'Up':
        if towards == 'd':
            pass
        else:
            towards = 'u'
    elif event.keysym == 'Down':
        if towards == 'u':
            pass
        else:
            towards = 'd'

cv.bind_all('<KeyPress-Left>', move)
cv.bind_all('<KeyPress-Right>', move)
cv.bind_all('<KeyPress-Up>', move)
cv.bind_all('<KeyPress-Down>', move)

while True:
    b = body(x, y, cv, 'green')
    bodies.append(b)
    before = bodies[-1]
    if towards == 'l':
        x = before.x1 - before.big
        y = before.y1
    if towards == 'r':
        x = before.x1 + before.big
        y = before.y1
    if towards == 'u':
        x = before.x1
        y = before.y1 - before.big
    if towards == 'd':
        x = before.x1
        y = before.y1 + before.big
    if len(bodies) > long:
        cv.delete(bodies[0].id)
        del bodies[0]
    if before.x1 < 0 or before.y1 <0 or before.x2 > w or before.y2 > h:
        cv.create_text(280, 260, text='你输了!', font=('微软雅黑', 20, 'bold'))
        die = True
    if before.x1 == food1.x1 and before.y1 == food1.y1:
        cv.delete(food1.id)
        del food1
        rx, ry = r.choice(list(range(20, w-20, 20))), r.choice(list(range(20, h-20, 20)))
        food1 = food(rx, ry, cv, 'red')
        long += 1
        t - 0.01
    for a in bodies[0:len(bodies)-2]:
        if before.x1 == a.x1 and before.y1 == a.y1:
            cv.create_text(280, 260, text='你死了!', font=('微软雅黑', 20, 'bold'))
            die = True
    tk.update_idletasks() 
    tk.update()
    time.sleep(t)
    if die == True:
       main()
