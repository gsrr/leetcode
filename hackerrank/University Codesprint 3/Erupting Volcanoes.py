#!/bin/python

import sys
from collections import deque

global mval

def ans(graph, x1, y1, w1):
    global mval
    hist = {}
    q = deque([(x1, y1, w1)])
    hist[(x1, y1)] = True
    while len(q) != 0:
        x, y, w = q.popleft()
        graph[x][y] += w
        
        #mval = max(mval, graph[x][y])
        if w == 1:
            continue
        for nx, ny in [(-1, 1), (-1, 0), (-1, -1), (0, 1), (0, -1), (1, 1), (1, 0), (1, -1)]:
            if x + nx >= 0 and x + nx < len(graph) and y + ny >= 0 and y + ny < len(graph[nx]):
                if hist.has_key((x + nx, y + ny)):
                    continue
                hist[(x + nx, y + ny)] = True
                q.append((x + nx, y + ny, w - 1))

def ans2(graph, x, y, w):
    for i in range(len(graph)):
        for j in range(len(graph[i])):
            graph[i][j]+=max(0,w - max(abs(x-i),abs(y-j)))

def ans3(grid, x, y, w):
    dis = 1
    grid[x][y] += w
    w -= 1
    while w>0:
        for i in xrange(x-dis,x+dis+1):
            if i>=0 and i<n and y-dis>=0:
                grid[i][y-dis] += w
        for i in xrange(x-dis,x+dis+1):
            if i>=0 and i<n and y+dis<n:
                grid[i][y+dis] += w
        for j in xrange(y-dis+1,y+dis):
            if x-dis>=0 and j>=0 and j<n:
                grid[x-dis][j] += w
        for j in xrange(y-dis+1,y+dis):
            if x+dis<n and j>=0 and j<n:
                grid[x+dis][j] += w
        w -= 1
        dis += 1
        
if __name__ == "__main__":
    n = int(raw_input().strip())
    m = int(raw_input().strip())
    graph = [ [0] * n for _ in xrange(n) ] 
    mval = 0
    for a0 in xrange(m):
        x, y, w = raw_input().strip().split(' ')
        x, y, w = [int(x), int(y), int(w)]
        # Write Your Code Here
        ans3(graph, x, y, w)
    #print graph
    for i in xrange(len(graph)):
        for j in xrange(len(graph[i])):
            if graph[i][j] > mval:
                mval = graph[i][j]
    print mval
