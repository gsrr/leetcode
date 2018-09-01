import collections
import heapq

def create_graph(edges):
    graph = collections.defaultdict(list)
    for e in edges:
        u = e[0]
        v = e[1]
        w = e[2]
        graph[u].append((v, w))
        graph[v].append((u, w))
    return graph
    
def ans(edges, M, N):
    graph = create_graph(edges)
    #print graph
    pq = []
    visited = [-1] * N
    heapq.heappush(pq, (-1 * M, 0))
    hist = {}
    while len(pq) != 0:
        move, u = heapq.heappop(pq)
        move = -1 * move
        if visited[u] != -1:
            continue
        visited[u] = move
        for item in graph[u]:
            v = item[0]
            w = item[1]
            if move - w > 0:
                hist[(u, v)] = (w, w)
                heapq.heappush(pq, (-1 * (move - w - 1), v))
            else:
                hist[(u, v)] = (move, w)
    #for key in hist.keys():
        #print key, hist[key]
    #print visited
    cnt = 0
    for key in hist.keys():
        u, v = key
        rkey = (v, u)
        wu, w = hist[key]
        if hist.has_key(rkey):   
            wv, w = hist[rkey]
        else:
            wv = 0
        if wu + wv >= w:
            cnt += w
        else:
            cnt += (wu + wv)
        hist[key] = (0, 0)
        if hist.has_key(rkey): 
            hist[rkey] = (0, 0)
    #print cnt
    for v in visited:
        if v != -1:
            cnt += 1
    return cnt
        
    
class Solution(object):
    def reachableNodes(self, edges, M, N):
        """
        :type edges: List[List[int]]
        :type M: int
        :type N: int
        :rtype: int
        """
        return ans(edges, M, N)
