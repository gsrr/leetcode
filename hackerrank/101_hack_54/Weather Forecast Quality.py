#!/bin/python

from __future__ import print_function

import os
import sys

# Complete the totalForecastInaccuracy function below.
def totalForecastInaccuracy(t, f):
    # Return the sum of the weather forecast inaccuracies across all 7 days.

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    t = map(int, raw_input().rstrip().split())

    f = map(int, raw_input().rstrip().split())

    result = totalForecastInaccuracy(t, f)

    fptr.write(str(result) + '\n')

    fptr.close()

