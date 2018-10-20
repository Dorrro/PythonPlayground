import math


def avg(arr):
    return sum(arr) / len(arr)


def median(arr):
    arr.sort()
    n = len(arr)
    if n % 2 == 0:
        mid = int(n/2)
        return avg([arr[mid - 1], arr[mid]])
    else:
        return arr[((n + 1) / 2) - 1]


def std_deviation(arr):
    variance = 0
    a = avg(arr)
    for digit in arr:
        variance = variance + math.pow((digit - a), 2)

    variance = variance / len(arr)

    return math.sqrt(variance)
