import matplotlib.pyplot as pltimport math

a = 1
b = -3
c = 1

def f(x):
    return a*math.pow(x, 2) + b * x + c

x = range(-10, 11)

y = list(map(lambda num: f(float(num)), x))

print(x)
print(y)

plt.plot(x, y)
plt.grid(linestyle=':')
plt.xlim(-10, 10)
plt.ylim(-20, 140)
plt.show()