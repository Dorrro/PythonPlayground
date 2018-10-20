max_value = 26


def get_number():
    while True:
        key = int(input('Podaj liczbę (1-%s)' % max_value))
        if 1 <= key <= max_value:
            return key


def cypher(message, key):
    translated = ''

    for symbol in message:
        if symbol.isalpha():
            num = ord(symbol)
            num += key

            if symbol.isupper():
                if num > ord('Z'):
                    num -= 26
                elif num < ord('A'):
                    num += 26
            elif symbol.islower():
                if num > ord('z'):
                    num -= 26
                elif num < ord('a'):
                    num += 26

            translated += chr(num)
        else:
            translated += symbol
    return translated


message = input("Podaj wiadomość do zaszyfrowania: ")
key = get_number()

print('Twoja zaszyfrowana wiadomość to : ' + cypher(message, key))
