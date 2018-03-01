#!/bin/python3

import os
import sys
import collections


# Complete the function below.

def maximumPermutation2(w, s):
    # Return the string representing the answer.
    dic = collections.defaultdict(int)
    maxcnt = 0
    maxss = "-1"
    cw = collections.Counter(w)
    for i in xrange(len(s) - len(w) + 1):
        cs = collections.Counter(s[i : i + len(w)])
        if cw == cs:
            ss = s[i : i + len(w)]
            dic[ss] += 1
            if dic[ss] > maxcnt:
                maxcnt = dic[ss]
                maxss = ss
    return maxss

def maximumPermutation(w, s):
    # Return the string representing the answer.
    dic = {}
    maxcnt = 0
    maxss = "-1"
    cw = [0] * 26
    for i in range(len(w)):
        cw[ord(w[i]) - ord('a')] += 1
        
    cs = None
    for i in range(len(s) - len(w) + 1):
        if cs == None:
            cs = [0] * 26
            for j in range(i, i + len(w)):
                cs[ord(s[j]) - ord('a')] += 1
        else:
            cs[ord(s[i + len(w) - 1]) - ord('a')] += 1
            cs[ord(s[i - 1]) - ord('a')] -= 1

        if cw == cs:
            ss = s[i : i + len(w)]
            hash_ss = hash(ss)
            if hash_ss not in dic:
                dic[hash_ss] = 0
            dic[hash_ss] += 1
            
            if dic[hash_ss] > maxcnt:
                maxcnt = dic[hash_ss]
                maxss = ss
            elif dic[hash_ss] == maxcnt:
                if ss < maxss:
                    maxss = ss
    return maxss

if __name__ == '__main__':
    f = open(os.environ['OUTPUT_PATH'], 'w')

    t = int(input())

    for t_i in range(t):
        w = input()

        s = input()

        result = maximumPermutation(w, s)

        f.write(result + "\n")

    f.close()

