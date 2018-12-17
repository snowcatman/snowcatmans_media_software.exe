import os
import stat
import time
import sys
import re



# Walk sub-directories in reverse order
for (dirpath, dirnames, filenames) in os.walk('.', topdown=True):
    dirnames.reverse()
    print(dirpath, dirnames, filenames)
 
# Prune the ".git" directory
 
for (dirpath, dirnames, filenames) in os.walk('.', topdown=True):
    dirnames[:] = [dirname for dirname in dirnames if dirname != '.git']
    print(dirpath, dirnames, filenames)
 
# Pruning directories that contain a file named "foo"
 
for (dirpath, dirnames, filenames) in os.walk('.', topdown=True):
    if 'foo' in filenames:
        del dirnames
        continue
    print(dirpath, dirnames, filenames)