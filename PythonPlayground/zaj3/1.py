import matplotlib.pyplot as plt

a = int(input("Podaj a:"))
b = int(input("Podaj b:"))

def f(x):
    return a*x+b

x = range(-10, 11, 1)
y = list(map(lambda num: f(num), x))

print(x)
print(y)

plt.plot(x,y)
plt.title("Wykres f(x) = a*x + b")
plt.grid(True)
plt.show()