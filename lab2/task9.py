import turtle as trt
import math


def polygon(x):
    while x <= n:
        trt.left((180 - 360 / n) / 2)
        trt.left(360 / n)
        trt.forward(2 * R * math.sin(math.pi / n))
        x += 1
        trt.right((180 - 360 / n) / 2)


trt.shape('turtle')
R = 15
trt.penup()
trt.goto(R, 0)
trt.pendown()

n = 3
x = 1

while n <= 11:
    polygon(x)
    n += 1
    R += 9
    trt.up()
    trt.goto(R, 0)
    trt.down()
