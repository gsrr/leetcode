# Definition for an interval.
# class Interval(object):
#     def __init__(self, s=0, e=0):
#         self.start = s
#         self.end = e
import collections
import heapq

def is_relation(arr1, arr2):
    if arr2[0] >= arr1[1]:
        return False
    return True

ghist = {}

def recur_util(graph, u, mis):
    global ghist
    
    key = "%d%s"%(u, mis)
    if ghist.has_key(key) == True:
        return ghist[key]
    
    if u >= len(graph):
        return 0
    
    for v in graph[u]:
        if v in mis:
            return recur_util(graph, u + 1, mis)
    
    mis.add(u)
    v1 = 1 + recur_util(graph, u + 1, mis)
    mis.remove(u)
    v2 = recur_util(graph, u + 1, mis)
    ghist[key] = max(v1, v2)
    return ghist[key]
    
def ans(objarr):
    global ghist
    ghist = {}
    
    arr = []
    for obj in objarr:
        arr.append([obj.start, obj.end])
    arr.sort()
    #print arr
    graph = collections.defaultdict(list)
    for i in xrange(len(arr)):
        if graph.has_key(i) == False:
            graph[i] = []
        for j in xrange(i + 1, len(arr)):
            if is_relation(arr[i], arr[j]):
                graph[i].append(j)
                graph[j].append(i)
    
    #print graph
    mis = set([])
    gmax = recur_util(graph, 0, mis)
    #print len(arr), gmax
    return len(arr) - gmax
        

def dfs(arr):
    if len(arr) == 0:
        return 0
    
    if len(arr) == 1:
        return 1
    
    global ghist
    key = str(arr)
    if ghist.has_key(key):
        return ghist[key]
    
    v1 = dfs(arr[1:])
    v2 = 0
    for i in xrange(1, len(arr)):
        if is_relation(arr[0], arr[i]) == True:
            continue
        v2 = 1 + dfs(arr[i:])
        break
    ghist[key] = max(v1, v2)
    return ghist[key]

def ans1(objarr):     
    global ghist
    ghist = {}
    arr = []
    for obj in objarr:
        arr.append([obj.start, obj.end])
    arr.sort()
    
    #print arr
    gmax = dfs(arr)
    return len(arr) - gmax

def ans2(objarr):
    arr = []
    for obj in objarr:
        arr.append([obj.end, obj.start])
    arr.sort()
    
    end = -0x7fffffff
    cnt = 0
    for i in xrange(len(arr)):
        if arr[i][1] >= end:
            end = arr[i][0]
            cnt += 1
    return len(arr) - cnt
    
class Solution(object):
    def eraseOverlapIntervals(self, intervals):
        """
        :type intervals: List[Interval]
        :rtype: int
        """
        return ans2(intervals)
