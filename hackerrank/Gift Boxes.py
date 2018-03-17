#!/bin/python

import os
import sys

def prefix_function(s):
    f = [-1] * len(s)
    for i in xrange(1, len(f)):
        j = f[i - 1] # last match string index
        while j > -1 and s[i] != s[j + 1]:
            j = f[j]
        if s[i] == s[j + 1]:
            f[i] = j + 1
        
    return f
#
# Complete the giftBoxes function below.
#
def giftBoxes(g, c):
    #
    # Return the number of gift boxes that can be packaged.
    #
    f = prefix_function(g)
    #print f
    stack = []
    i = 0 
    j = 0
    cnt = 0
    while i < len(c) and j < len(g):
        if c[i] == g[j]:
            stack.append((c[i], j))
            i += 1
            j += 1
            if j == len(g):
                cnt += 1
                while j != 0:
                    stack.pop()
                    j -= 1
                if len(stack) > 0:
                    j = stack[-1][1] + 1 # next index
        else:
            if j == 0:
                i += 1
                while len(stack) > 0:
                    stack.pop()
            else:
                j = f[j - 1] + 1
    
    return cnt

if __name__ == '__main__':
    f = open(os.environ['OUTPUT_PATH'], 'w')

    t = int(raw_input())

    for t_itr in xrange(t):
        g = raw_input()

        c = raw_input()

        result = giftBoxes(g, c)

        f.write(str(result) + '\n')

    f.close()

