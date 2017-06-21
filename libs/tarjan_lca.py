
def find(x, p):
    while x != p[x]:
        x = p[x]
    return x

def tarjan_lca(node, m, p, visited):
    print "node:", node
    p[node] = node
    visited[node] = True
    for v in xrange(len(m[node])):
        e = m[node][v]
        if e == 1 and visited[v] != True:
            tarjan_lca(v, m, p, visited)
            p[v] = node
    for v in xrange(len(m[node])):
        if visited[v] == True:
            print "(%d,%d) : "%(node, v), find(v, p)
m = [
    [0, 1, 1, 0],
    [1, 0, 0, 1],
    [1, 0, 0, 0],
    [0, 1, 0, 0],

]

visited = [ [0] * 4 for i in xrange(4)]
p = {}
tarjan_lca(0, m, p, visited)
