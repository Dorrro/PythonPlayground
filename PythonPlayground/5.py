import sys
import math

if len(sys.argv) != 4:
	print("You need to specify exactly 3 arguments")
	exit()
	
a = int(sys.argv[1])
b = int(sys.argv[2])
c = int(sys.argv[3])
	
def delta(a, b, c):
	return b*b - 4*a*c
	
delta = delta(a, b, c)

if delta == 0:
	print("x0 = " + str(-b/(2*a)))
elif delta > 0:
	print("x1 = " + str((-b - math.sqrt(delta))/(2*a)))
	print("x2 = " + str((-b + math.sqrt(delta))/(2*a)))
else:
	print("No square roots")
