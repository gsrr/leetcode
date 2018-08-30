#!/bin/python

import math
import os
import random
import re
import sys
import heapq
import collections

def create_graph(edges):
    graph = collections.defaultdict(dict)
    for e in edges:
        u = e[0] - 1
        v = e[1] - 1
        w = e[2]
        if graph[u].has_key(v):
            graph[u][v] = min(graph[u][v], w)
            graph[v][u] = min(graph[v][u], w)
        else:
            graph[u][v] = w
            graph[v][u] = w
    return graph

# Complete the shortestReach function below.
def shortestReach(n, graph, s):
    pq = []
    #graph = create_graph(edges)
    heapq.heappush(pq, (0, s - 1)) # (dist, node)
    visited = [-1] * n
    while len(pq) != 0:
        du, u = heapq.heappop(pq)
        if visited[u] != -1:
            continue
        visited[u] = du
        for v, w in graph[u].items():
            heapq.heappush(pq, (du + w , v))
    ret = []
    for i in xrange(len(visited)):
        if i != s - 1:
            ret.append(visited[i])
    return ret

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    t = int(raw_input())

    for t_itr in xrange(t):
        nm = raw_input().split()

        n = int(nm[0])

        m = int(nm[1])

        graph = collections.defaultdict(dict)

        for _ in xrange(m):
            u, v, w = map(int, raw_input().rstrip().split())
            u -= 1
            v -= 1
            if graph[u].has_key(v):
                graph[u][v] = min(graph[u][v], w)
                graph[v][u] = min(graph[v][u], w)
            else:
                graph[u][v] = w
                graph[v][u] = w

        s = int(raw_input())

        result = shortestReach(n, graph, s)

        fptr.write(' '.join(map(str, result)))
        fptr.write('\n')

    fptr.close()

