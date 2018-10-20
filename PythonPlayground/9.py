a = [1, 2, 12, 4]
b = [2, 4, 2, 8]

sum = 0
for i in range(0, len(a)):
	sum = sum + a[i]*b[i]
	
print(sum)
