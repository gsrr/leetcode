import sys
import os
print sys.argv
cmd = 'python "%s.py" < "%s.txt"'%(sys.argv[1], sys.argv[1])
print cmd
os.system(cmd)

