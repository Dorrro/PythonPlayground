import os, os.path
from PIL import Image
from os.path import basename

for root, dirs, files in os.walk('.'):
	for f in files:
		if f.endswith('.jpg'):
			im = Image.open(f)
			im.save(os.path.splitext(f)[0] + '.png')
