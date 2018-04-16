#!/bin/python

#from __future__ import print_function

import os
import sys




# Complete the averageOfTopEmployees function below.
def averageOfTopEmployees(rating):
    ret = 0
    cnt = 0
    for r in rating:
        if r >= 90:
            ret += r
            cnt += 1
    val = ret / float(cnt)
    val = round(val, 3)
    val = int(val * 1000)
    r = val % 10
    val = val / 10
    if r >= 5:
        val += 1
    return "%.2f"%(val / 100.0)

if __name__ == '__main__':
    n = int(raw_input())

    rating = []

    for _ in xrange(n):
        rating_item = int(raw_input())
        rating.append(rating_item)

    print averageOfTopEmployees(rating)

