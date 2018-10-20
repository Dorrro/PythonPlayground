import module

number_of_digits = int(input("Podaj ilość ocen: "))
digits = []


while number_of_digits > 0:
    digits.append(int(input("Podaj ocenę: ")))
    number_of_digits = number_of_digits - 1

print("Średnia: " + str(module.avg(digits)))
print("Mediana: " + str(module.median(digits)))
print("Odchylenie standardowe: " + str(module.std_deviation(digits)))