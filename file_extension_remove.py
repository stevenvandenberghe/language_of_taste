# needed to be able to distinguish cats.txt (with categories)
# from regular text files

import os
import glob

os.chdir("/path/to/dir")
files = glob.glob('.*txt')
for file in files:
    os.rename(file, file.split('.')[0])