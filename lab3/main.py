import turtle as trt
from random import randint

trt.hideturtle()
a = 205
trt.penup()
trt.goto(-a, -a)
trt.pendown()
trt.goto(-a, a)
trt.goto(a, a)
trt.goto(a, -a)
trt.goto(-a, -a)
trt.penup()

number = 10
t = 290

vol = [trt.Turtle(shape='circle') for i in range(number)]

for unit in vol:
    unit.turtlesize(0.5)
    unit.penup()
    unit.speed(randint(-15, 15))
    unit.goto(randint(-a + 10, a - 10), randint(-a + 10, a - 10))
    unit.seth(randint(0, 360))

for i in range(t):
    for j in range(len(vol)):
        angle_j = vol[j].heading()
        x_j, y_j = vol[j].pos()

        if x_j <= -a + 5 or x_j >= a - 5:
            vol[j].seth(180 - angle_j)
        elif y_j <= -a + 5 or y_j >= a - 5:
            vol[j].seth(-angle_j)
        vol[j].fd(5)
