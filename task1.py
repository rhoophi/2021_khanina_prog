import numpy as np
import matplotlib.pyplot as pt
import matplotlib.ticker as ticker

file = open("task1.txt")
b = []
c = []
for line in file:
    a = line.split()
    b.append(int(a[0]))
    c.append(int(a[1]))

print(b)
print(c)
pt.figure(dpi = 500)
pt.grid()
pt.plot(b, c, 'ro')
pt.savefig('graph.png')


