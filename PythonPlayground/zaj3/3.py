import matplotlib.pyplot as plt
import random
import math

r = 2

def newX(x):
    a = random.randint(0, 360)
    return x + r * math.cos(a)

def newY(y):
    a = random.randint(0,360)
    return y + r * math.sin(a)

def dist(x, y):
    return math.sqrt(math.pow(x, 2) + math.pow(y, 2))

n = int(input("Podaj ilość ruchów: "))

x = [0]
y = [0]
for i in range(1, n):
    x.append(newX(x[i - 1]))

for i in range(1, n):
    y.append(newY(y[i - 1]))

print(x)
print(y)

x2 = [x[-1], 0]
y2 = [y[-1], 0]

l1 = plt.plot(x2, y2, "b", label = 'Dabe x, y\nPrzemieszczenie: ' + str(dist(x[-1], y[-1])))
plt.legend(loc = 'upper left')
plt.plot(x,y, "g:o")
plt.grid(True)
plt.show()
