import turtle

t = turtle.Turtle()
screen = turtle.Screen()

t.speed(0)
t.color("black")

#plano cartesiano
t.goto(0,400)
t.lt(90)
t.stamp()

t.lt(180)
t.goto(0,-400)
t.stamp()  

t.goto(0,0)
t.lt(90)
t.goto(400,0)
t.stamp()
t.lt(180)
t.goto(-400,0)
t.stamp()


#forma 1
t.pu()
t.goto(-200,300)
t.pd()

cor1 = screen.textinput("Escolha de Cor para a forma 1", "Digite a cor para a forma:")


t.begin_fill()
t.color(cor1)
for i in range(12):
    t.fd(50)
    t.lt(30)
t.end_fill()

cor2 = screen.textinput("Escolha de Cor para a forma 2", "Digite a cor para a forma:")


#tp para estrela
t.pu()
t.goto(300,200)
t.pd()
t.begin_fill()
t.color(cor2)

#estrela
for i in range(5):
    t.fd(70)
    t.lt(72)
    t.fd(70)
    t.rt(144)

t.end_fill()

#tp para forma 3
t.pu()
t.goto(-200,-100)
t.pd()

cor3 = screen.textinput("Escolha de Cor para a forma 3", "Digite a cor para a forma:")


#forma 3
t.begin_fill()
t.color(cor3)
for i in range(6):
    t.fd(100)
    t.lt(60)
t.end_fill()

#tp para forma 4
t.pu()
t.goto(50,-150)
t.pd()

cor4 = screen.textinput("Escolha de Cor para a forma 4", "Digite a cor para a forma:")

t.begin_fill()
t.color(cor4)
t.lt(180)
for i in range(5):
    t.fd(80)
    t.lt(72)
t.end_fill()

#tp para espiral
t.pu()
t.goto(300,-350)
t.pd()
t.color("black")

#tive que pesquisar nessa parte para otimizar o codigo, antes fiz oque esta escrito abaixo, porem queria otimizar isso.
# for i in range(100):
#    t.fd(4.4)
#    t.lt(2)
#for i in range(100):
#    t.fd(4.1)
#    t.lt(2)

passo_inicial = 4.4
decremento = 0.3
num_loops = 15

for espiral in range(num_loops):
    passo = passo_inicial - espiral * decremento
    for _ in range(100):
        t.fd(passo)
        t.lt(2)




turtle.mainloop()