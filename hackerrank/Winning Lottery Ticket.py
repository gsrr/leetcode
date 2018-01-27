#!/bin/python

import sys
import collections


def tsets_add(num, tsets):
    tn = num
    while tn != 0:
        rid = tn % 10
        tsets[rid].add(num)
        tn = tn / 10
    
def tsets_count(sn, tsets):
    dic = {}
    for k in "01234567890":
        dic[k] = True
    for c in sn:
        if dic.has_key(c):
            del dic[c]
    items = None
    for k in dic.keys():
        if items == None:
            items = set(tsets[k])
        else:
            items &= tsets[k]
    
    if items == None:
        return 0
    print sn, items
    return len(items)
    
def winningLotteryTicket(tickets):
    # Complete this function
    '''
    Type : Array : Finding number of pair
    
    case 1: it ticket already has 0 ~ 9 --> it should filter self.
    '''
    base = set("0123456789")
    dic = collections.defaultdict(int)
    for t in tickets:
        dic["".join(set(t))] += 1
    cnt = 0
    for t in dic.keys():
        if len(set(t)) == 10:
            cnt += ((len(tickets) - 1) * dic[t])
            continue
        for key in dic.keys():
            if len(key) + len(t) < 10:
                continue
            skey = set(key)
            if len(set(t).union(skey)) == 10:
                cnt += (dic[key] * dic[t])
    return cnt / 2
    
if __name__ == "__main__":
    n = int(raw_input().strip())
    tickets = []
    tickets_i = 0
    for tickets_i in xrange(n):
        tickets_t = str(raw_input().strip())
        tickets.append(tickets_t)
    result = winningLotteryTicket(tickets)
    print result

