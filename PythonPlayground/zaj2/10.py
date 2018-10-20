n = int(input("Podaj ilość liczb do wpisania: "))

digits = []

for i in range(n):
    digits.append(int(input("Podaj liczbę numer %s: " % (i + 1))))

for i in range(n):
    print("Liczba o indeksie %(index)s to %(digit)s" % {"index": i, "digit": digits[i]})

digits.reverse()

print(digits)

digits.sort()

print(digits)

a = int(input("Podaj liczbę do usunięcia: "))

index = digits.index(a)

digits.pop(index)

print(digits)

a = int(input("Podaj index: "))

digits.pop(a)
print(digits)

a = int(input("Podaj liczbę: "))

print("Indeks elementu to: %s " % digits.index(a))
print("Ilość elementów w liście: %s" % len(([digit for digit in digits if digit == a])))

a = int(input("Podaj indeks startowy: "))
b = int(input("Podaj indeks końcowy: "))
print(digits[a:b])
