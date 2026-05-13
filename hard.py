from turtle import *
from time import sleep
from random import randint

t = Turtle()
t.speed(0)

def randomColor():
  return (randint(0, 255), randint(0, 255), randint(0, 255))

colormode(255)
t.pu()
t.goto(0,50)
t.pd()

def formadificil(t,size,angle,nivel):
    if size < 25:
        return
    t.pd()
    t.fd(size)

    #down
    t.rt(90)
    t.fd(size)
    formadificil(t, size * 0.8, angle, nivel - 1)
    t.back(size)

    t.lt(90)

    t.lt(90)
    t.fd(size)
    formadificil(t, size * 0.8, angle, nivel - 1)
    t.back(size)

    t.rt(90)
    
    # right tree
    t.rt(angle)
    t.fd(size)
    formadificil(t, size * 0.8, angle, nivel - 1)
    t.back(size)

    t.pencolor(0, 255 // nivel, 0)

    # left tree
    t.lt(2 * angle)
    t.fd(size)
    formadificil(t, size * 0.8, angle, nivel - 1)
    t.back(size)

    t.pencolor(0, 255 // nivel, 0)
    t.lt(-angle)
    t.back(size)

t.goto(0, -200)
t.lt(90)
formadificil(t, 80, 40, 20)

mainloop()