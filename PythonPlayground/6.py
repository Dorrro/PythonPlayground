import random

def bubble_sort(arr):
    for number in range(len(arr)-1,0,-1):
        for i in range(number):
            if arr[i]<arr[i+1]:
                temp = arr[i]
                arr[i] = arr[i+1]
                arr[i+1] = temp

arr = []
for i in range(0, 50):
	arr.append(random.randrange(1,100))

print("Before sorting: ")
print(arr)

bubble_sort(arr)

print("After sorting: ")
print(arr)
