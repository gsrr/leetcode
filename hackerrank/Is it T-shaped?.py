#!/bin/python

import math
import os
import random
import re
import sys

def is_first(grid, arr):
    arr.sort()
    for i in xrange(1, len(grid)):
        d1 = (arr[i][0] - arr[i - 1][0], arr[i][1] - arr[i - 1][1])
        d2 = (grid[i][0] - grid[i - 1][0], grid[i][1] - grid[i - 1][1])
        if d1 != d2:
            return False
    return True

# Complete the solve function below.
def solve(grid):
    grid.sort()
    arr1 = [[1, 0], [1, 1], [1, 2], [2, 2], [0, 2]]
    arr2 = [[2, 1], [1, 1], [0, 1], [0, 0], [0, 2]]
    arr3 = [[2, 0], [1, 0], [0, 0], [1, 1], [1, 2]]
    arr4 = [[2, 0], [2, 1], [2, 2], [1, 1], [0, 1]]
    if is_first(grid, arr1):
        return "Yes"
    if is_first(grid, arr2):
        return "Yes"
    if is_first(grid, arr3):
        return "Yes"
    if is_first(grid, arr4):
        return "Yes"
    return "No"
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    t = int(raw_input().strip())

    for t_itr in xrange(t):
        points = []

        for _ in xrange(5):
            points.append(map(int, raw_input().rstrip().split()))

        result = solve(points)

        fptr.write(result + '\n')

    fptr.close()

