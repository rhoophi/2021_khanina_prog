import turtle as trt


def star(n, k=2):
    x = 1
    while x <= n:
        trt.right(180 - (180 * (n - 2 * k) / n))
        trt.forward(150)
        x += 1


trt.shape('turtle')
star(10, 7)
trt.penup()
trt.goto(160, 0)
trt.pendown()
star(11, 5)
trt.penup()
trt.goto(0, 160)
trt.pendown()
