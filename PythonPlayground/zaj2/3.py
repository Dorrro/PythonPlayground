import random

slowa = {"python": "jezyk programowania", "gdansk": "jedno z trójmiejskich miast", "dlaczego": "synonim do czemu",
         "gdynia": "jedno z trójmiejskich miast", "wsb": "jedna z uczelnii prywatnych"}
word = random.choice(list(slowa))
# print (word)
poprawnie = word
print(poprawnie)
pomie = ""

while word:
    position = random.randrange(len(word))
    pomie += word[position]
    word = word[:position] + word[(position + 1):]
print(pomie)

print(
    """
Witaj w grze 'Wymieszane litery'!
Uporządkuj litery, aby odtworzyć prawidłowe słowo.
(Aby zakończyć zgadywanie, naciśnij klawisz Enter bez
podawania odpowiedzi.)
"""
)

score = 10
hint = False

print("Zgadnij, jakie to słowo:", pomie)

zgaduj = input("\nTwoja odpowiedź: ")
while zgaduj != poprawnie and zgaduj != "" and score > 0:
    score = score - 1
    print("Niestety, to nie to słowo.")
    if not hint:
        podpowiedz = input("Potrzebujesz podpowiedzi? (T/N): ")
        if podpowiedz == "T":
            print(slowa[poprawnie])
            hint = True
            score = score - 5
    zgaduj = input("Twoja odpowiedź: ")
if zgaduj == poprawnie:
    print("Zgadza się! Zgadłeś! Uzyskałeś " + str(score) + " punktów!")
else:
    print("Niestety, nie udało Ci się. Hasło to: " + poprawnie)

print("Dziękuję za udział w grze.")
