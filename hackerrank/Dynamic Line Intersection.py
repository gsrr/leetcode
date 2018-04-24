#!/bin/python

#from __future__ import print_function

import os
import sys
import collections

#
# Complete the dynamicLineIntersection function below.
#
def dynamicLineIntersection1(n):
    #
    # Write your code here.
    #
    dic = collections.defaultdict(int)
    all = 0
    for _ in xrange(n):
        line = raw_input().strip()
        line = line.split()
        op = line[0]
        a = int(line[1])
        if op == "+":
            if a == 1:
                all += 1
                continue
            b = int(line[2])
            dic[(a, b % a)] += 1
        if op == "-":
            if a == 1:
                all -= 1
                continue
            b = int(line[2])
            dic[(a, b % a)] -= 1
        if op == "?":
            cnt = 0
            for key in dic.keys():
                a1 = key[0]
                a2 = key[1]
                if (a - a2) % a1 == 0:
                    cnt += dic[key]
            print all + cnt

def dynamicLineIntersection2(n):
    #
    # Write your code here.
    #
    dic = collections.defaultdict(int)
    all = 0
    for _ in xrange(n):
        line = raw_input().strip()
        line = line.split()
        op = line[0]
        a = int(line[1])
        if op == "+":
            if a == 1:
                all += 1
                continue
            b = int(line[2])
            dic[(a, b % a)] += 1
        if op == "-":
            if a == 1:
                all -= 1
                continue
            b = int(line[2])
            dic[(a, b % a)] -= 1
        if op == "?":
            cnt = 0
            for key in dic.keys():
                a1 = key[0]
                a2 = key[1]
                if a % a1 == a2:
                    cnt += dic[key]
            print all + cnt


def update_arr(arr, dic):
    for key in dic.keys():
        a = key[0]
        b = key[1]
        val = b
        cnt = 1
        while val < len(arr):
            arr[val] += dic[key]
            val = a * cnt + b
            cnt += 1
            
def dynamicLineIntersection(n):
    arr = [0] * 100001
    dic = collections.defaultdict(int)
    query = []
    base_cnt = 10
    rarr = [[0] * base_cnt for _ in xrange(base_cnt)]
    for _ in xrange(n):
        #print dic
        line = raw_input().strip()
        line = line.split()
        op = line[0]
        a = int(line[1])
        if op == "+":
            b = int(line[2])
            if a <= base_cnt:
                rarr[a - 1][b % a] += 1
                continue
            dic[(a, b % a)] += 1
        if op == "-":
            b = int(line[2])
            if a <= base_cnt:
                rarr[a - 1][b % a] -= 1
                continue
            dic[(a, b % a)] -= 1
        if op == "?":
            update_arr(arr, dic)
            dic = collections.defaultdict(int)
            ret = arr[a]
            for i in xrange(1, base_cnt + 1):
                ret += rarr[i - 1][a % i]
            print ret
    #update_arr(arr, dic)
    #print arr
if __name__ == '__main__':
    n = int(raw_input())

    dynamicLineIntersection(n)

