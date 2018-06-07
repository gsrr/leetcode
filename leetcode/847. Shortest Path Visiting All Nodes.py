visited = None
pvisited = None
n = 0
mval = 0x7fffffff

def dfs(graph, u, v):
    global mval, n, visited, pvisited
    if len(pvisited.keys()) > mval:
        return
    
    if len(pvisited.keys()) > 2 * n:
        return
    
    if len(visited.keys()) == n:
        tval = len(pvisited.keys())
        #print pvisited
        if tval < mval:
            mval = tval
        return
    
    for w in graph[v]:
        if pvisited.has_key((v, w)) == False:
            if visited.get(w, False) == False:
                pvisited[(v, w)] = True
                visited[w] = True
                dfs(graph, v, w)
                del pvisited[(v, w)]
                del visited[w]
            else:
                pvisited[(v, w)] = True
                dfs(graph, v, w)
                del pvisited[(v, w)]
    
        

def ans1(graph):
    global mval, n, visited, pvisited
    n = len(graph)
    mval = 0x7fffffff
    visited = {}
    pvisited = {}
    
    for u in xrange(n):
        visited[u] = True
        for v in graph[u]:
            pvisited[(0, v)] = True
            visited[v] = True
            dfs(graph, 0, v)
            del pvisited[(0, v)]
            del visited[v]
        del visited[u]
        
    return mval if mval != 0x7fffffff else 0


import heapq

def bfs(graph, u):
    q = []
    n = len(graph)
    used = set([(1 << u, u)])
    #print used
    heapq.heappush(q, (0, u, 1 << u))
    while len(q) != 0:
        d, u, visited = heapq.heappop(q)
        
        vist = visited | ( 1 << u)
        if 1 << n  == vist + 1:
            return d
        
        if d > 2 * n:
            continue
        for v in graph[u]:
            if (vist,v) in used:
                continue
            used.add((vist, v))
            heapq.heappush(q, (d + 1, v, vist))
            
def ans(graph):
    n = len(graph)
    if n < 2:
        return 0
    mval = 0x7fffffff
    for i in xrange(n):
        tval = bfs(graph, i)
        if tval < mval:
            mval = tval
    return mval if mval != 0x7fffffff else 0

class Solution(object):
    def shortestPathLength(self, graph):
        """
        :type graph: List[List[int]]
        :rtype: int
        """
        return ans(graph)
        
