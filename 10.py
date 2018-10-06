#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import random

def generate_matrix(r):
	matrix = []
	for i in range(0, r):
		matrix.append([])
		for j in range(0, r):
			matrix[i].append(random.randrange(1,9))
	
	return (matrix)

def print_matrix(matrix):
	for i in range(0, len(matrix[0])):
		for j in range(0 , len(matrix[0])):
			
			print('{:>4}'.format(matrix[i][j]), end='')
		print()

num = 128

a = generate_matrix(num)
b = generate_matrix(num)
c = generate_matrix(num)

print("A:")
print_matrix(a)
print("B:")
print_matrix(b)

print("calculating...")

for i in range(0, len(c[0])):
	for j in range(0 , len(c[0])):
		c[i][j] = a[i][j] + b[i][j]

print_matrix(c)
