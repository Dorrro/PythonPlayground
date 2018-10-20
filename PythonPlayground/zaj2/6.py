dictionary = {}


def extract_def(text):
    definition = text.split(":")
    dictionary[definition[0]] = definition[1].replace(" ", "").split(",")


content = open('./dictionary.txt', 'r').read()

lines = content.splitlines()

for line in lines:
    extract_def(line)

word_def = input("Podaj definicję słowa: ")
while word_def != "koniec":
    extract_def(word_def)
    word_def = input("Podaj definicję słowa: ")


print(dictionary)

content = open('./dictionary.txt', 'w+')

for key, value in dictionary.items():
    content.write(key + ": " + str.join(", ", value) + "\n")

content.close()