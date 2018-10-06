import os

path, dirs, files = next(os.walk("/usr/lib"))
print (len(files))
