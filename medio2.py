from turtle import *
from time import sleep
from random import randint

t = Turtle()
t.speed(0)

def randomColor():
  return (randint(0, 255), randint(0, 255), randint(0, 255))

colormode(255)

def forma_facil(t,size,step):
    if size == 0 or step == 0:
       return
    t.begin_fill()
    t.color(randomColor())
    for i in range(6):
        t.fd(size)
        t.lt(60)
    t.end_fill()
    forma_facil(t,size-5,step-1)

forma_facil(t,100,50)

mainloop()