# Enter your code here. Read input from STDIN. Print output to STDOUT

import collections

def bellman(graph, s):
    #print graph, s
    n = 4
    dp = [float("inf")] * n 
    dp[s] = 0
    prev = [-1] * n
    x = s
    for i in xrange(n):
        for u in graph.keys():
            if dp[u] == float("inf"):
                continue
            for e in graph[u]:
                v = e[0]
                c = e[1]
                if dp[u] + c < dp[v]:
                    dp[v] = dp[u] + c
                    prev[v] = u
                    x = v
     
    
    neg_cycle = False
    for u in graph.keys():
        if dp[u] == float("inf"):
            continue
        for e in graph[u]:
            v = e[0]
            c = e[1]
            if dp[u] + c < dp[v]:
                neg_cycle = True
    
    if neg_cycle == False:
        return []
    
    for i in xrange(n):
        x = prev[x]
        
    cycle = [x]
    v = prev[x]
    while v != x:
        cycle.append(v)
        v = prev[v]
    cycle.append(v)
    return cycle[::-1] 
    
pval = 0

def dfs(graph, u, visited, sum_path):
    #print u, visited 
    global pval
    if visited[u] == 1:
        pval = max(pval, -1 * sum_path)
        return
    else:
        visited[u] = 1
        for e in graph[u]:
            v = e[0]
            c = e[1]
            sum_path += c
            #print "\b", u, v, visited
            dfs(graph, v, visited, sum_path)
            sum_path -= c
    visited[u] = 0
    
def ans(arr):
    global pval
    pval = 0
    
    edges = [(3, 0), (0, 1), (1, 2), (2, 3), (0, 2), (1, 3)]
    #print arr
    graph = collections.defaultdict(list)
    
    for i in xrange(len(edges)):
        u = edges[i][0]
        v = edges[i][1]
        cost = arr[i]
        graph[u].append([v, cost])
    #print graph                  
    #ret = bellman(graph, 0)
    visited = [0] * 4
    sum_path = 0
    dfs(graph, 0, visited, sum_path)
    #print pval
    return pval

def ans_bellman(arr):
    edges = [(3, 0), (0, 1), (1, 2), (2, 3), (0, 2), (1, 3)]
    #print arr
    graph = collections.defaultdict(list)
    
    for i in xrange(len(edges)):
        u = edges[i][0]
        v = edges[i][1]
        cost = arr[i]
        graph[u].append([v, cost])
        
    ret = {}
    cycle = bellman(graph, 0)
    while len(cycle) != 0:
        sc = 0
        imin = (0, 0)
        tmin = 0x7fffffff
        for i in xrange(1, len(cycle)):
            u = cycle[i - 1]
            v = cycle[i]
            for j in xrange(len(graph[u])):
                if graph[u][j][0] == v:
                    sc += graph[u][j][1]
                    if graph[u][j][1] < tmin:
                        tmin = graph[u][j][1]
                        imin = (u, v)
        #print cycle, sc, imin, tmin
        if ret.has_key(imin) == False:
            ret[imin] = 0
        
        ret[imin] += (-1 * sc)
        
        u = imin[0]
        v = imin[1]
        for j in xrange(len(graph[u])):
            if graph[u][j][0] == v:
                graph[u][j][1] += (-1 * sc)
        cycle = bellman(graph, 0)
    #print ret
    gmax = 0
    for key in ret.keys():
        if ret[key] > gmax:
            gmax = ret[key]
    return gmax

if __name__ == "__main__":
    arr = map(int, raw_input().strip().split())
    print ans_bellman(arr)
