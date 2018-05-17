import sys
import collections
# your task is to complete this function
# Function should return sum of weights of  the edges of the Minimum Spanning Tree
# graph is of form adjancy matrix
# e is the number of edges and n is the no of nodes

def find_min(nodes):
    keys = list(nodes.keys())
    idx = keys[0]
    min_val = nodes[idx]
    for k in keys:
        if nodes[k] < min_val:
            min_val = nodes[k]
            idx = k
    return idx

def update_nodes(graph, nodes, u):
    for v in range(len(graph[u])):
        if graph[u][v] != 0 and v in nodes:
            nodes[v] = min(nodes[v], graph[u][v])

def spanningTree(graph, n, e):
    # Code here
    edges = []
    nodes = {}
    for u in range(len(graph)):
        for v in range(len(graph)):
            if graph[u][v] != 0:
                edges.append([graph[u][v], (u, v)])
                nodes[u] = sys.maxsize
    #print (nodes)
    # start search by vertex 0
    
    keys = list(nodes.keys())
    #print (keys)
    n = len(keys)
    nodes[keys[0]] = 0
    
    mst = set([])
    ret = 0
    while len(mst) != n:
        u = find_min(nodes)
        mst.add(u)
        ret += nodes[u]
        del nodes[u]
        update_nodes(graph, nodes, u)
    return ret
