#!/bin/python

import sys
import collections
import copy
import itertools

def ans_1(dic):
    buy_dic = {}
    q = int(raw_input().strip())
    for a0 in xrange(q):
        d = int(raw_input().strip())
        cameras = raw_input().strip().split(' ')
        k = int(raw_input().strip())
        cameras.sort()
        key = "".join(cameras)
        prices = []
        if buy_dic.has_key(key):
            prices = buy_dic[key]
        else:
            buy_list = {}
            for i in xrange(len(cameras)):
                cprices = dic[int(cameras[i])]
                for j in xrange(len(cprices)):
                    buy_list[cprices[j]] = True
            prices = buy_list.keys()
            prices.sort()
            buy_dic[key] = copy.deepcopy(prices)
        
        if k > len(prices):
            print -1
        else:
            if len(prices) == 0:
                print -1
            else:
                print prices[k - 1]

def mergeUtil(bp , prices):
    for p in prices:
        bp[p] = True
    
def merge(dic):
    merge_dic = collections.defaultdict(dict)
    keys = dic.keys()
    for i in xrange(pow(2, len(keys))):
        bp = {}
        key = 0
        for j in xrange(len(keys)):
            if i & (1<<j) != 0:
                key += (1 << (keys[j] - 1))
                mergeUtil(bp , dic[keys[j]])
        prices = bp.keys()
        prices.sort()
        merge_dic[key] = list(prices)
    return merge_dic

def merge_iter(dic):
    merge_dic = collections.defaultdict(dict)
    keys = dic.keys()
    for i in xrange(len(keys) + 1):
        it = itertools.combinations(keys, i)
        for brand in it:
            bp = {}
            key = 0
            for b in brand:
                key += (1 << (b - 1))
                mergeUtil(bp , dic[b])
            prices = bp.keys()
            prices.sort()
            merge_dic[key] = list(prices)
    return merge_dic

def get_key(cs):
    key = 0
    for val in cs:
        key += (1 << (val - 1))
    return key

def ans_2(dic):
    #merge_dic = merge(dic)
    merge_dic = merge_iter(dic)
    q = int(raw_input().strip())
    for a0 in xrange(q):
        d = int(raw_input().strip())
        cameras = map(int, raw_input().strip().split(' '))
        k = int(raw_input().strip())
        key = get_key(cameras)
        if merge_dic.has_key(key) == False:
            print -1
            continue
        
        prices = merge_dic[key]
        if k > len(prices):
            print -1
        else:
            print prices[k - 1]

def get_dic_ans1():
    n = int(raw_input().strip())
    brands = map(int, raw_input().strip().split(' '))
    prices = map(int, raw_input().strip().split(' '))
    dic = collections.defaultdict(list)
    for i in xrange(len(brands)):
        dic[brands[i]].append(prices[i])
    return dic

def get_dic_ans2():
    n = int(raw_input().strip())
    brands = map(int, raw_input().strip().split(' '))
    prices = map(int, raw_input().strip().split(' '))
    dic = collections.defaultdict(dict)
    for i in xrange(len(brands)):
        dic[brands[i]][prices[i]] = True
    return dic

if __name__ == "__main__":
    #dic = get_dic_ans1()
    dic = get_dic_ans2()
    
    #ans_1(dic)
    ans_2(dic)
    
