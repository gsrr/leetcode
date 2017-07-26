#!/bin/python

import sys
import collections

def graph_matrix_create(matrix, e):
    x = e[0] - 1
    y = e[1] - 1
    matrix[x][y] = 1
    matrix[y][x] = 1

def graph_dic_create(dic, e):
    x = e[0] - 1
    y = e[1] - 1
    dic[x].append(y)
    dic[y].append(x)

def dj(dic, n, sn, cost):
    cs = [0] * n
    q = [sn]
    hist = [0] * n
    while len(q) != 0:
        node = q.pop(0)
        cs[node] += cost[node]
        hist[node] = 1
        for i in xrange(len(dic[node])):
            nt = dic[node][i]
            if hist[nt] != 1:
                cs[nt] += cs[node]
                q.append(nt)
    return 0
    sf = 0
    for c in cs:
        sf += fibo(c)
    return sf


f = range(10000)
f[0] = 1
f[1] = 1
for i in xrange(2, 10000):
    f[i] = (f[i - 1] + f[i - 2]) % (pow(10,9) + 7)

def fibo(n):
    global f
    return f[n] 

if __name__ == "__main__":
    n = int(raw_input().strip())
    #matrix = [ [0] * n  for i in xrange(n)] 
    dic = collections.defaultdict(list)
    for a0 in xrange(n-1):
        x, y = raw_input().strip().split(' ')
        x, y = [int(x), int(y)]
        graph_dic_create(dic, (x,y))

    c = map(int, raw_input().strip().split(' '))
    s = 0
    for i in xrange(n):
        s += dj(dic, n, i, c)
        s = s % (pow(10, 9) + 7)
    print s
