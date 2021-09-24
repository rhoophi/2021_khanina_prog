import turtle as trt
import functions2 as func

lines = []
with open('func.txt') as file:
    for line in file:
        lines.append(line)

nums = list(map(int, input()))
for i in range(len(nums)):
    eval(lines[int(nums[i])])
trt.exitonclick()
