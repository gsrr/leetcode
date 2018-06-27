#!/bin/python

import math
import os
import random
import re
import sys

import heapq

def find_qy1(pq_dic, qx, deleted):
    qy = heapq.heappop(pq_dic[qx])
    v = qy[2]
    while deleted.has_key(v) == True:
        qy = heapq.heappop(pq_dic[qx])
        v = qy[2]
    heapq.heappush(pq_dic[qx], qy)
    return qy
    

def get_dist1(n, dist, s, t):
    if s == t:
        return 0
    
    if s < t:
        return dist[t] - dist[s]
    
    if t < s:
        return dist[t + n] - dist[s]
    
import collections

tcnt = 0
vcnt = 0


def update_pq(pq_dic, qx, qw, dist, n):
    global tcnt, vcnt
    tcnt -= 1
    for key in pq_dic.keys():
        di = get_dist1(n, dist, key, qx) + qw
        heapq.heappush(pq_dic[key], [-1 * di, tcnt, vcnt])

# Complete the cyclicalQueries function below.
def cyclicalQueries1(n, w, m):
    # Return the list of answers to all queries of type 4. Take the query information from standard input.
    global tcnt, vcnt
    tcnt = 0
    vcnt = n
    
    dist = [0] * (2 * n)
    dist[0] = w[0]
    for i in xrange(1, len(dist)):
        dist[i] = w[i % n] + dist[i - 1]
    '''
    print get_dist1(n, dist, 0, 4) # 4
    print get_dist1(n, dist, 2, 1) # 4
    print get_dist1(n, dist, 3, 1) # 3
    print get_dist1(n, dist, 3, 5)
    '''
    
    pq_dic = collections.defaultdict(list)
    for i in xrange(n):
        di = get_dist1(n, dist, i, i - 1)
        heapq.heappush(pq_dic[i], [-1 * di, 0, (i - 1) % n])
    #print pq_dic
    
    # start query
    deleted = {}
    ret = []
    for i in xrange(m):
        qarr = map(int, raw_input().rstrip().split())
        #print pq_dic
        qx, qy, qw = 0, 0, 0
        if qarr[0] == 1: # add new node for qy
            qx = qarr[1] - 1
            qy = find_qy(pq_dic, qx, deleted)
            qw = qarr[2]
            #print qarr, qy[2], qw
            update_pq(pq_dic, qy[2], qw, dist, n)
            vcnt += 1
        elif qarr[0] == 2: # add new node for qx
            qx = qarr[1] - 1
            qw = qarr[2]
            update_pq(pq_dic, qx, qw, dist, n)
            vcnt += 1
        elif qarr[0] == 3: # delete node
            qx = qarr[1] - 1
            qy = find_qy(pq_dic, qx, deleted)
            deleted[qy[2]] = True
        elif qarr[0] == 4: # print qy
            qx = qarr[1] - 1
            qy = find_qy(pq_dic, qx, deleted)
            ret.append(str(-1 * qy[0]))
            
    return ret


class UFS:
    def __init__(self, n):
        self.parent = [-1] * n
        self.pq = collections.defaultdict(list)
        for i in xrange(n):
            heapq.heappush(self.pq[i], (0, 0))
        
    def find(self, v):
        u = self.parent[v]
        if u == -1:
            return v
        return self.find(u)
    
    def union(self, u, v, w):
        global tcnt
        tcnt -= 1
        pu = self.find(u)
        pv = self.find(v)
        if pu == pv:
            return
        if pu <= pv:
            self.parent[pv] = pu
            heapq.heappush(self.pq[pu], (-1 * w, tcnt, pv))
        else:
            self.parent[pu] = pv
            heapq.heappush(self.pq[pv], (-1 * w, tcnt, pu))
            
def remove(pq, v):
    heapq.heappop(pq[v])
    
def find_qy2(qx, pq, w):
    n = len(w)
    gval = 0
    gdist = 0
    tval = 0
    ridx = qx
    st = qx
    i = 0
    dist = 0
    while i < n:
        st = (qx + i) % n
        qy = heapq.heappop(pq[st])
        #print st, qy
        if dist + (-1 * qy[0]) > gval + gdist:
            gval = (-1 * qy[0])
            gdist = dist
            tval = qy[1]
            ridx = st
        elif dist + (-1 * qy[0]) == gval + gdist:
            if qy[1] < tval:
                gval = (-1 * qy[0])
                gdist = dist
                ridx = st
                tval = qy[1]
        heapq.heappush(pq[st], qy)
        dist += w[st]
        i += 1
    return (gdist, gval, ridx, qy[1])
    
def cyclicalQueries1(n, w, m):
    global tcnt
    tcnt = -1
    pq = collections.defaultdict(list)
    for i in xrange(n):
        heapq.heappush(pq[i], (0, 0))
    
    # start query
    ret = []
    
    for i in xrange(m):
        qarr = map(int, raw_input().rstrip().split())
        qx, qy, qw = 0, 0, 0
        
        if qarr[0] == 1: # add new node for qy
            qx = qarr[1] - 1
            qy = find_qy(qx, pq, w)
            qw = qarr[2]
            #print qarr, qy[2], qw
            #ufs.union(qy[1], vcnt, qw)
            heapq.heappush(pq[qy[2]], (-1 * (qw + qy[1]), tcnt))
            tcnt -= 1
        elif qarr[0] == 2: # add new node for qx
            qx = qarr[1] - 1
            qw = qarr[2]
            #ufs.union(qx, vcnt, qw)
            heapq.heappush(pq[qx], (-1 * qw, tcnt))
            tcnt -= 1
        elif qarr[0] == 3: # delete node
            qx = qarr[1] - 1
            qy = find_qy(qx, pq, w)
            remove(pq, qy[2])
            if len(pq[qy[2]]) == 0:
                heapq.heappush(pq[qy[2]], (0, 0))
        elif qarr[0] == 4: # print qy
            qx = qarr[1] - 1
            qy = find_qy(qx, pq, w)
            #print "qy:", qy
            ret.append(str(qy[0] + qy[1]))
        #print qx, qy, qw , pq
   
    return ret

def get_ceil_int(fn):
    return int(math.ceil(fn))

def get_pq_max(pq, i):
    return -1 * pq[i][0][0]

def get_pq_time(pq, i):
    return pq[i][0][1]

class D_SQRT:
    def __init__(self, n):
        self.root = get_ceil_int(math.sqrt(n))
        self.size = get_ceil_int(n / float(self.root))
        self.arr = [0] * self.size
        self.n = n
    
    def init_max(self, n, dist):
        for i in xrange(self.size):
            left = i * self.root
            right = (i + 1) * self.root
            right = right if right < self.n else self.n
            
            lmax = 0
            node = left
            for j in xrange(left + 1, right):
                tmax = get_dist1(n, dist, left, j) + 0
                if tmax > lmax:
                    lmax = tmax
                    node = j
            self.arr[i] = (lmax, 0, node)
    
    
    
    def find_far_node(self, qx, pq, dist):
        block = qx / self.root
        left=  block * self.root
        right = (block + 1) * self.root
        right = right if right < self.n else self.n
        
        gmax = get_pq_max(pq, qx)
        gtime = get_pq_time(pq, qx)
        gnode = qx
        for i in xrange(left, right):
            if i == qx:
                continue
            tmax = get_dist1(self.n, dist, qx, i) + get_pq_max(pq, i)
            ttime = get_pq_time(pq, i)
            if tmax > gmax:
                gmax = tmax
                gnode = i
                gtime = ttime
            elif tmax == gmax:
                if ttime < gtime:
                    gmax = tmax
                    gtime = ttime
                    gnode = i
                
        
        for i in xrange(self.size):
            if i == block:
                continue
            left = i * self.root
            lmax, ltime, lnode = self.arr[i]
            tmax = get_dist1(self.n, dist, qx, left) + lmax
            if tmax > gmax:
                gmax = tmax
                gtime = ltime
                gnode = lnode
            elif tmax == gmax:
                if ltime < gtime:
                    gmax = tmax
                    gtime = ltime
                    gnode = lnode
        return (gmax, gnode)
    
    def update(self, dist, node, pq):
        block = node / self.root
        left=  block * self.root
        right = (block + 1) * self.root
        right = right if right < self.n else self.n
        
        lmax = get_pq_max(pq, left)
        ltime = get_pq_time(pq, left)
        lnode = left
        for i in xrange(left + 1, right):
            tmax = get_dist1(self.n, dist, left, i) + get_pq_max(pq, i)
            ttime = get_pq_time(pq, i)
            if tmax > lmax:
                lmax = tmax
                lnode = i
                ltime = ttime
            elif tmax == lmax:
                if ttime < ltime:
                    lmax = tmax
                    ltime = ttime
                    lnode = i
        self.arr[block] = (lmax, ltime, lnode)
    
def cyclicalQueries(n, w, m):
    global tcnt
    tcnt = -1
    
    dsq = D_SQRT(n)
    dist = [0] * (2 * n)
    dist[0] = 0
    for i in xrange(1, len(dist)):
        dist[i] = w[(i - 1) % n] + dist[i - 1]
    
    dsq.init_max(n, dist)
    
    pq = collections.defaultdict(list)
    for i in xrange(n):
        heapq.heappush(pq[i], (0, 0))
    
    ret = []
    for i in xrange(m):
        qarr = map(int, raw_input().rstrip().split())
        qx, qy, qw = 0, 0, 0
        
        #print qarr, dsq.arr
        if qarr[0] == 1: # add new node for qy
            qx = qarr[1] - 1
            dmax, qy = dsq.find_far_node(qx, pq, dist)
            qw = qarr[2]
            heapq.heappush(pq[qy], (-1 * (qw + dmax - get_dist1(n, dist, qx, qy)), tcnt))
            dsq.update(dist, qy, pq)
            tcnt -= 1
        elif qarr[0] == 2: # add new node for qx
            qx = qarr[1] - 1
            qw = qarr[2]
            heapq.heappush(pq[qx], (-1 * qw, tcnt))
            dsq.update(dist, qx, pq)
            tcnt -= 1
        elif qarr[0] == 3: # delete node
            qx = qarr[1] - 1
            dmax, qy = dsq.find_far_node(qx, pq, dist)
            if len(pq[qy]) == 1:
                continue
            heapq.heappop(pq[qy])  
            dsq.update(dist, qy, pq)
        elif qarr[0] == 4: # print qy
            qx = qarr[1] - 1
            dmax, qy = dsq.find_far_node(qx, pq, dist)
            ret.append(str(dmax))
    return ret

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(raw_input())

    w = map(long, raw_input().rstrip().split())

    m = int(raw_input())

    result = cyclicalQueries(n, w, m)

    fptr.write('\n'.join(map(str, result)))
    fptr.write('\n')

    fptr.close()

