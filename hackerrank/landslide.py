#!/bin/python

import os
import sys
import collections

def query(graph, start, end):
    q = [(start, 0)]
    hist = {}
    while len(q) != 0:
        u, d = q.pop(0)
        if u == end:
            print d
            return
        if hist.has_key(u):
            continue
        hist[u] = True
        for v in graph[u]:
            if v[1] == 1:
                q.append((v[0], d + 1))
            
    print "Impossible"
    return 
            
def destroy(graph, u, v):
    if (v, 1) in graph[u]:
        graph[u].remove((v, 1))
        graph[u].add((v, 0))
        graph[v].remove((u, 1))
        graph[v].add((u, 0))

def connect(graph, u, v):
    if (v, 0) in graph[u]:
        graph[u].remove((v, 0))
        graph[u].add((v, 1))
        graph[v].remove((u, 0))
        graph[v].add((u, 1))
    
t = 0
f = None # start point of sub-tree
g = None # end point of sub-tree

def dfs(graph, v, u = 0, d = 0):
    global t
    global f
    global g
    t += 1
    f[v] = t
    for w in graph[v]:
        if (w == u):
            continue
        dfs(graph, w, v, d + 1)
    g[v] = t

def landslide(n):
    global f
    global g
    graph = collections.defaultdict(list)
    for i in xrange(n - 1):
        u, v = map(int, raw_input().split())
        u -= 1
        v -= 1
        graph[u].append(v)
        graph[v].append(u)

    f = [0] * n
    g = [0] * n

    print graph
    dfs(graph, 0)
    print f
    print g
    '''
    qn = int(raw_input())
    for _ in xrange(qn):
        arr = raw_input().strip().split()
        op = arr[0]
        u = int(arr[1])
        v = int(arr[2])
        if op == "q":
            query(graph, u, v)
        elif op == "d":
            destroy(graph, u, v)
        elif op == "c":
            connect(graph, u, v)
    '''    

if __name__ == '__main__':
    n = int(raw_input())

    landslide(n)

