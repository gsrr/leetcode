import collections

def dfs(graph, u, ret, quiet):
    ret[u] = quiet[u]
    for v in graph[u]:
        if ret[v] == -1:
            dfs(graph, v, ret, quiet)
        ret[u] = min(ret[u], ret[v])
    
def ans(richer, quiet):
    graph = collections.defaultdict(list)
    for e in richer:
        u = e[1]
        v = e[0]
        graph[u].append(v)
    
    ret = [-1] * len(quiet)
    for u in xrange(len(quiet)):
        dfs(graph, u, ret, quiet)
    
    iquiet = {}
    for i in xrange(len(quiet)):
        iquiet[quiet[i]] = i
    return [ iquiet[x] for x in ret ]
    
class Solution(object):
    def loudAndRich(self, richer, quiet):
        """
        :type richer: List[List[int]]
        :type quiet: List[int]
        :rtype: List[int]
        """
        return ans(richer, quiet)
        
