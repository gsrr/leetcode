#!/bin/python

import math
import os
import random
import re
import sys

def bfs(board, x, y):
    q = [(x, y)]
    hist = {}
    while len(q) != 0:
        x, y = q.pop(0)
        if hist.has_key((x, y)) == True:
            continue
        hist[(x, y)] = True
        for nx, ny in [(x - 1, y), (x + 1, y), (x, y - 1), (x, y + 1)]:
            if nx >= 0 and ny >= 0 and nx < len(board) and ny < len(board[nx]):
                if board[x][y] == board[nx][ny]:
                    return "No"
                q.append((nx, ny))
    return "Yes"

# Complete the solve function below.
def solve(board):
    #print board
    return str(bfs(board, 0, 0))
    
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    t = int(raw_input().strip())

    for t_itr in xrange(t):
        n = int(raw_input().strip())

        board = []

        for _ in xrange(n):
            board.append(map(int, raw_input().rstrip().split()))

        result = solve(board)

        fptr.write(result + '\n')

    fptr.close()

