#!/usr/bin/env python3
# -*- coding: utf-8 -*-

mapping = {
	'i':'oraz', 
	'oraz':'i', 
	'nigdy':'prawie nigdy', 
	'dlaczego': 'czemu'}


content = open('./1.txt', 'r').read()
#content = 'tak jest i ponieważ oraz test też nigdy tak dlaczego'

print(content)

words = []
for word in content.split():
	if word in mapping:
		word = mapping[word]
	words.append(word)
	
print(' '.join(words))
