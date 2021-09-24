import turtle as trt
import math

trt.pensize(2)
trt.shape('turtle')

trt.speed(100)
x = -300
y = 0
trt.penup()
trt.goto(x, y)
trt.pendown()
trt.speed(1)

v_y = v_y0 = 50
v_x = 10
x_0 = 0
a_y = -9.98
dt = 0.001

while v_y0 >= 0.5:
    while y >= 0:
        x_0 = x
        trt.goto(x, y)
        x = x + v_x * dt
        y = y + v_y * dt + a_y * (dt ** 2) / 2
        v_y = v_y + a_y * dt
        dt += 0.0001

    if y < 0:
        v_y = v_y0 / math.sqrt(2)
        v_y0 = v_y
        y = 0
        trt.goto(x_0, 0)
