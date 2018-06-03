#!/bin/python

import math
import os
import random
import re
import sys
from datetime import datetime

# Complete the lagDuration function below.
def lagDuration(h1, m1, h2, m2, k):
    # Return an integer denoting the duration of time in minutes by which the clock has been lagging.
    t1 = datetime.strptime("%d:%d"%(h1, m1), "%H:%M")
    t2 = datetime.strptime("%d:%d"%(h2, m2), "%H:%M")
    diff = t2 - t1
    return 60 * k - diff.seconds//60

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    q = int(raw_input())

    for q_itr in xrange(q):
        h1M1H2M2 = raw_input().split()

        h1 = int(h1M1H2M2[0])

        m1 = int(h1M1H2M2[1])

        h2 = int(h1M1H2M2[2])

        m2 = int(h1M1H2M2[3])

        k = int(raw_input())

        result = lagDuration(h1, m1, h2, m2, k)

        fptr.write(str(result) + '\n')

    fptr.close()

