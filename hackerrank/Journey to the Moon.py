#!/bin/python

import math
import os
import random
import re
import sys

import collections

def bfs(graph, u, tag, tarr):
    q = [u]
    hist = {}
    while len(q) != 0:
        u = q.pop()
        if hist.has_key(u):
            continue
        hist[u] = True
        tarr[u] = tag
        for v in graph[u]:
            q.append(v)

def create_graph(arr):
    graph = collections.defaultdict(list)
    for e in arr:
        u, v = e[0], e[1]
        graph[u].append(v)
        graph[v].append(u)
    return graph
    
# Complete the journeyToMoon function below.
def journeyToMoon(n, arr):
    graph = create_graph(arr)
    tarr = [-1] * n
    tag = 0
    for u in xrange(n):
        if tarr[u] == -1:
            bfs(graph, u, tag, tarr) 
            tag += 1
    print tarr
    ct = collections.Counter(tarr)
    total = (n * (n - 1)) / 2
    for key in ct.keys():
        if key == -1:
            continue
        total -= (ct[key] * (ct[key] - 1)) / 2
    return total
    
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    np = raw_input().split()

    n = int(np[0])

    p = int(np[1])

    astronaut = []

    for _ in xrange(p):
        astronaut.append(map(int, raw_input().rstrip().split()))

    result = journeyToMoon(n, astronaut)

    fptr.write(str(result) + '\n')

    fptr.close()

