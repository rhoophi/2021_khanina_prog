import turtle as trt
from random import randint

trt.hideturtle()
a = 205  # линейный размер сосуда
number = 10  # число черепах

trt.penup()
trt.goto(-a, -a)
trt.pendown()
trt.goto(-a, a)
trt.goto(a, a)
trt.goto(a, -a)
trt.goto(-a, -a)
trt.penup()

vol = [trt.Turtle(shape='circle') for i in range(number)]  # volume
for unit in vol:
    unit.penup()
    unit.turtlesize(0.5)
    unit.goto(randint(-a + 10, a - 10), randint(-a + 10, a - 10))
    unit.speed(randint(-15, 15))
    unit.seth(randint(-360, 360))

for i in range(1000):
    for j in range(number):
        x_j, y_j = vol[j].position()
        angle_j = vol[j].heading()

        if x_j <= -a + 5 or x_j >= a - 5:  # столкновения
            vol[j].seth(180 - angle_j)
        if y_j <= -a + 5 or y_j >= a - 5:
            vol[j].seth(-angle_j)

        vol[j].fd(5)
