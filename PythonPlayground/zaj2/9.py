start = ord('a')
diff = ord('A') - ord('a')
stop = ord('z') + 1

for i in range(start, stop):
    print(chr(i + diff), end="")
    print(chr(i), end="")

print()

for i in range(start, stop):
    print(chr(i), end="")
    print(chr(i + diff), end="")
