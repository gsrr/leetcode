#!/bin/python

import math
import os
import random
import re
import sys
import heapq
import collections

def create_graph(edges):
    graph = collections.defaultdict(list)
    for e in edges:
        u = e[0] - 1
        v = e[1] - 1
        w = e[2]
        graph[u].append((v, w))
        graph[v].append((u, w))
    return graph

# Complete the shortestReach function below.
def shortestReach(n, edges, s):
    pq = []
    graph = create_graph(edges)
    heapq.heappush(pq, (0, s - 1)) # (dist, node)
    visited = [-1] * n
    while len(pq) != 0:
        du, u = heapq.heappop(pq)
        if visited[u] != -1:
            continue
        visited[u] = du
        for v, w in graph[u]:
            heapq.heappush(pq, (du + w , v))
    return visited

if __name__ == '__main__':
    n = 4
    m = 4
    edges = [[1, 2, 24], [1, 4, 20], [3, 1, 3], [4, 3, 12]]
    result = shortestReach(n, edges, 1)
    print result #0 24 3 15



