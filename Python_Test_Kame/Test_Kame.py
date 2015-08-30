#coding:shift-jis
import turtle
import random
kame = turtle.Turtle()
kame.clear()
kame.shape('turtle')
kame.shapesize(2,2,3)
kame.home()
kame.clear()
kame.penup()
kame.forward(200)
kame.left(90)
kame.pendown()
kame.circle(200)
kame.penup()
kame.home()
kame.pendown()
while kame.distance(0,0) < 200:
    kame.left(random.randint(1,360))
    kame.forward(15)
    