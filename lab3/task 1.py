import turtle as trt
import random as rnd

trt.speed(10)
trt.shape('circle')
for i in range(500):
    trt.forward(rnd.randint(-50, 50))
    trt.left(rnd.randint(-360, 360))
