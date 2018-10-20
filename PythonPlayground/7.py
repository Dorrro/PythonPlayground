#!/usr/bin/env python3
# -*- coding: utf-8 -*-

words_to_replace = [' się', ' i', ' oraz', ' nigdy', ' dlaczego']

content = open('./1.txt', 'r').read()

print(content)

words = []
for word in content.split():
	if word not in words_to_replace:
		words.append(word)
	
print(' '.join(words))


