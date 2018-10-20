import random

words = ["jeden", "dwa", "dom", "test"]
word = random.choice(words)

step = 1

guess = ""

print("W słowie znajduje się " + str(len(word)) + " liter")

while step <= 5 and guess != word:
    letter = input("Podaj literę, która może istnieć w słowie: ")
    if len(letter) != 1:
        print("Litera ma tylko jeden znak :)")
        continue

    if letter in word:
        print("TAK!")
    else:
        print("NIE!")

    guess = input("Odgadnij słowo: ")
    step = step + 1

if guess == word:
    print("Gratulacje!")
else:
    print("Niestety, nie udało Ci się odgadnąć słowa: " + word)