import turtle as trt

n = int(input())

trt.shape('turtle')

for i in range(n):
    alpha = 360 / n
    trt.forward(50)
    trt.stamp()
    trt.backward(50)
    trt.left(alpha)

trt.exitonclick()