text = input("text: ")

words = text.split(" ")
words.reverse()

for word in words:
    print(word, end=" ")
