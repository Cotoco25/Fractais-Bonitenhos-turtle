from turtle import *
from time import sleep
t = Turtle()
t.speed(0)


#funcao abaixo:
#ola tudo bem
#ola tudo be
#ola tudo b ...
def mostra_palavra_for(palavra):
    for i in range(len(palavra)):
        print(palavra[:len(palavra) - i])

mostra_palavra_for("ola, tudo bem?")


xgui = 0
def mostra_palavra_recursivo_gui(palavra):
    global xgui
    while xgui<len(palavra):
        print(palavra[:len(palavra) - xgui])
        xgui+=1
        mostra_palavra_recursivo_gui(palavra)

mostra_palavra_recursivo_gui("aiiii caralho")

def mostra_palavra_recursivo(palavra):
    if palavra == "":
        return
    print("antes da chamada recursiva:", palavra)
    mostra_palavra_recursivo(palavra[:-1])
    print("depois da chamada recursiva:", palavra)
    return

mostra_palavra_recursivo("bicalho-o-o-o-o-o-o-o-o-o")

#def fibonacci(n):
#    if n == 0 or n == 1:
#        return
#    return fibonacci(n-1) + fibonacci(n-2)

#fibonacci(10)


colormode(255)

def drawsquare(t, size):
    t.pd()
    t.begin_fill()
    t.fillcolor(randomColor())
    for i in range(4):
        t.fd(size)
        t.rt(90)
    t.end_fill()
    t.pu()


def drawsquarefractal(t,size,step = 50):
    if size == 0 or step == 0:
        return
    t.fd(size / 1.5)
    t.lt(10)
    drawsquare(t, size)
    drawsquarefractal(t,size-1,step-1)

drawsquarefractal(t,70,60)

def drawMotherFuckingStar(t,size):
    if size < 10:
        return
    for i in range(5):
        t.fd(size)
        drawMotherFuckingStar(t,size / 3)
        t.lt(216)

mainloop()