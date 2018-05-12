#!/bin/python

import math
import os
import random
import re
import sys

def show_graph(graph):
    print type(graph)
    '''
    index = [ str(i) for i in range(len(graph))]
    print ("  ", ", ".join(index))
    for i in range(len(graph)):
        print (i, graph[i])
    '''

import collections
    
def ans(n, graph, s, ret):
    q = [(s, 0)]
    visited = [0] * n
    while len(q) != 0:
        u, dist = q.pop(0)
        if visited[u] != 0:
            continue
        visited[u] = 1
        ret[u] = 6 * dist
        for v in graph[u]:
            q.append((v, dist + 1))
    #print ret
        
# Complete the bfs function below.
def bfs(n, m, edges, s):
    ret = [-1] * n
    graph = collections.defaultdict(list)
    for e in edges:
        graph[e[0] - 1].append(e[1] - 1)
        graph[e[1] - 1].append(e[0] - 1)
    print graph[s - 1]
    ans(n, graph, s - 1, ret)
    ret.pop(s - 1)
    return ret
    
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    q = int(raw_input())

    for q_itr in xrange(q):
        nm = raw_input().split()

        n = int(nm[0])

        m = int(nm[1])

        edges = []

        for _ in xrange(m):
            edges.append(map(int, raw_input().rstrip().split()))

        s = int(raw_input())

        result = bfs(n, m, edges, s)

        fptr.write(' '.join(map(str, result)))
        fptr.write('\n')

    fptr.close()

