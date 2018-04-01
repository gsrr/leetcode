def ans1():
    pass

import collections

def create_graph(numCourses, relations):
    graph = collections.defaultdict(list)
    for r in relations:
        n1 = r[0]
        n2 = r[1]
        graph[n2].append(n1)
    return graph

def topo_dfs_util(v, graph, hist, stack):
    hist[v] = True
    for nv in graph[v]:
        if hist.has_key(v) == False:
            topo_dfs_util(nv, graph, hist, stack)
    stack.append(v)
    
def cycle_util(v, graph, hist, path):   
    hist[v] = True
    path.append(v)
    for nv in graph[v]:
        if hist.has_key(nv) == False:
            if cycle_util(nv, graph, hist, path) == True:
                return True
        else:
            if nv in path:
                return True
    path.pop()
    return False
    
def cycle(n, graph):
    hist = {}
    for v in xrange(n):
        path = []
        if hist.has_key(v) == False:
            if cycle_util(v, graph, hist, path) == True:
                return True
    return False

def topo_dfs(n, graph):
    #print cycle(n, graph)
    if cycle(n, graph):
        return False
    else:
        return True
    stack = []
    hist = {}
    for v in range(n):
        if hist.has_key(v) == False:
            topo_dfs_util(v, graph, hist, stack)
    print stack[::-1]
    return True
        
class Solution(object):
    def canFinish(self, numCourses, prerequisites):
        """
        :type numCourses: int
        :type prerequisites: List[List[int]]
        :rtype: bool
        """
        graph = create_graph(numCourses, prerequisites)
        return topo_dfs(numCourses, graph)
