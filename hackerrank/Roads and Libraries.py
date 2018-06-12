#!/bin/python

import math
import os
import random
import re
import sys

import collections

def bfs(graph, visited, u, tag):
    cnt = 0
    q = [u]
    while len(q) != 0:
        #u = q.pop(0)
        u = q.pop()
        if visited[u] != 0:
            continue
        visited[u] = tag
        cnt += 1
        for v in graph[u]:
            q.append(v)
    return cnt
    
# Complete the roadsAndLibraries function below.
def roadsAndLibraries(n, c_lib, c_road, cities):
    if c_lib <= c_road:
        return n * c_lib
    
    graph = collections.defaultdict(list)
    for e in cities:
        u = e[0] - 1
        v = e[1] - 1
        graph[u].append(v)
        graph[v].append(u)
    
    #ret = 0
    visited = [0] * n
    tag = 1
    for u in xrange(n):
        if visited[u] == 0:
            #cnt = bfs(graph, visited, u, tag)
            bfs(graph, visited, u, tag)
            #ret += c_lib
            #ret += ((cnt - 1) * c_road)
            tag += 1
    
    ret = 0
    ct = collections.Counter(visited)
    for key in ct.keys():
        ret += c_lib
        ret += ((ct[key] - 1) * c_road)
    
    return ret
    
    
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    q = int(raw_input())

    for q_itr in xrange(q):
        nmC_libC_road = raw_input().split()

        n = int(nmC_libC_road[0])

        m = int(nmC_libC_road[1])

        c_lib = int(nmC_libC_road[2])

        c_road = int(nmC_libC_road[3])

        cities = []

        for _ in xrange(m):
            cities.append(map(int, raw_input().rstrip().split()))

        result = roadsAndLibraries(n, c_lib, c_road, cities)

        fptr.write(str(result) + '\n')

    fptr.close()

