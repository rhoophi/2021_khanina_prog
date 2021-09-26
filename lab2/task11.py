import turtle as trt

trt.shape('turtle')

trt.left(90)
for i in range(10):
    trt.circle(5 + 10 * (i + 1))
    trt.circle(-5-10 * (i + 1))
