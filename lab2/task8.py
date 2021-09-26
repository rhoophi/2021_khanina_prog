import turtle as trt

trt.shape('turtle')
for i in range(10):
    trt.forward(10 + 10 * i)
    trt.left(90)
    trt.forward(10 + 10 * i)
    trt.left(90)
