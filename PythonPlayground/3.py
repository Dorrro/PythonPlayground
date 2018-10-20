#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import os
	
def list_files(startpath):
	for root, dirs, files in os.walk(startpath):
		for f in files:
			print(os.path.join(root, f))
		for d in dirs:
			list_files(os.path.join(root, d))

list_files(".")
