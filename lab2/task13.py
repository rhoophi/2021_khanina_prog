import turtle as trt
import math


def circle(R):
    l = 2 * math.pi * R
    step = l / 120
    for _ in range(120):
        trt.forward(step)
        trt.left(3)


def semicircle(R):
    l = 2 * math.pi * R
    step = l / 180
    for _ in range(90):
        trt.forward(step)
        trt.left(2)


trt.colormode(255)
trt.shape('turtle')
# перемещение в нужную координату
trt.up()
trt.goto(150, 0)
trt.left(90)
trt.down()
# тело
trt.fillcolor(224, 220, 175)
trt.begin_fill()
circle(150)
trt.end_fill()
# левый глаз
trt.up()
trt.goto(-40, 50)
trt.down()
trt.fillcolor(99, 142, 173)
trt.begin_fill()
circle(15)
trt.end_fill()
# правый глаз
trt.up()
trt.goto(70, 50)
trt.down()
trt.fillcolor(99, 142, 173)
trt.begin_fill()
circle(15)
trt.end_fill()
# нос
trt.up()
trt.goto(0, 30)
trt.down()
trt.color(219, 200, 151)
trt.pensize(8)
trt.left(180)
trt.forward(50)
# рот
trt.up()
trt.goto(-70, -10)
trt.color(214, 116, 99)
trt.down()
semicircle(70)
