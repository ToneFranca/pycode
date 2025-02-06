
import turtle
import math
#Função que utiliza o Turtle para desenhar polígonos. N =e a quantidade de lados, lenght o tamanho.

def polygon(t, n, length):
    angle = 360/n
    for i in range(n):
        t.fd(length)
        t.lt(angle)

#Função circle faz uma aproximação de um circulo, utilizando a função polygon. Desenha uma série de pequenos segmentos formando um circulo.

def circle(t, r):
    circumference = 2 * math.pi * r
    n = int(circumference / 3 )+1
    lenght = circumference / n
    polygon(t, n, lenght)



bob = turtle.Turtle()
circle(bob,20)

turtle.mainloop()