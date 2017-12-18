#!/bin/python

import sys

def ans_1(n, i_start, j_start, i_end, j_end):
    # UL, UR, R, LR, LL, L.
    hist = {}
    q = [(i_start, j_start, "")]
    rpath = None
    while len(q) != 0:
        x, y, path = q.pop(0)
        if x == i_end and y == j_end:
            if rpath == None:
                rpath = path
            else:
                if len(rpath.split()) > len(path.split()):
                    rpath = path
            continue
        if hist.has_key((x, y)):
            continue
        hist[(x, y)] = True
        for nx, ny, p in [(x - 2, y - 1, "UL"), (x - 2, y + 1, "UR"), (x, y + 2, "R"), (x + 2, y + 1, "LR"), (x + 2, y - 1, "LL"), (x, y - 2, "L")]:
            if nx >= 0 and nx < n and ny >= 0 and ny < n:
                q.append((nx, ny, path + " " + p))
    return rpath
    
#def printShortestPath(n, i_start, j_start, i_end, j_end):
    #  Print the distance along with the sequence of moves.
    
if __name__ == "__main__":
    n = int(raw_input().strip())
    i_start, j_start, i_end, j_end = raw_input().strip().split(' ')
    i_start, j_start, i_end, j_end = [int(i_start), int(j_start), int(i_end), int(j_end)]
    #printShortestPath(n, i_start, j_start, i_end, j_end)
    path = ans_1(n, i_start, j_start, i_end, j_end)
    if path == None:
        print "Impossible"
    else:
        print len(path.split())
        print path.strip()
