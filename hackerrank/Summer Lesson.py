#!/bin/python

from __future__ import print_function

import os
import sys


#
# Complete the howManyStudents function below.
#
def howManyStudents(m, c):
    # Return an array denoting the number of students taking each class.
    clas = [0] * m
    for n in c:
        clas[n] += 1
    return clas    
    
    


if __name__ == '__main__':
    f = open(os.environ['OUTPUT_PATH'], 'w')

    nm = raw_input().split()

    n = int(nm[0])

    m = int(nm[1])

    c = map(int, raw_input().rstrip().split())

    result = howManyStudents(m, c)

    f.write(' '.join(map(str, result)))
    f.write('\n')

    f.close()

