import math

a = int(input("Podaj długość boku a: "))
b = int(input("Podaj długość boku b: "))
c = int(input("Podaj długość boku c: "))


def can_it_be_triangle(a, b, c):
    return a + b > c and a + c > b and c + b > a


def is_it_rectangular(a, b, c):
    arr = [a, b, c]
    arr.sort()
    return math.pow(arr[0], 2) + math.pow(arr[1], 2) == math.pow(arr[2], 2)

def area(a, b, c):
    top = (a + b + c) * (a + b - c) * (a - b + c) * (-a + b + c)
    top = math.sqrt(top)

    return top / 4

if can_it_be_triangle(a, b, c):
    print("Trójkąt może zostać zbudowany")
    if is_it_rectangular(a, b, c):
        print("Jest to trójkąt prostokątny")

    print("Obwód trójkąta to: " + str(a + b + c))
    print("Pole trójkąta  to: " + str(area(a, b, c)))
else:
    print("Trójkąt nie może zostać zbudowany")