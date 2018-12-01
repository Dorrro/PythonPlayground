import matplotlib.pyplot as plt

a = float(input("Podaj a:"))

def f1(x):
    return (x/(-3))+a

def f2(x):
    return x*x/3

r2 = range(0, 21)
r1 = range(-20, 1)

x1 = list(map(lambda num: float(num)/2, r1))
x2 = list(map(lambda num: float(num)/2, r2))
        
y1 = list(map(lambda num: f1(num), x1))
y2 = list(map(lambda num: f2(num), x2))

print(x1)
print(y1)
print(x2)
print(y2)

plt.plot(x1,y1)
plt.plot(x2, y2)
plt.title("Wykres f(x)")
plt.grid(True)
plt.xlabel("x")
plt.ylabel("y")
plt.show()