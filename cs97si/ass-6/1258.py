

class UFS:
    def __init__(self, n):
        self.parent = [-1] * n
        self.rank = [0] * n

    def union(self, u, v):
        pu = self.find(u)
        pv = self.find(v)
        if pu == pv:
            return
        if self.rank[pu] >= self.rank[pv]:
            self.parent[pv] = pu
            if self.rank[pu] == self.rank[pv]:
                self.rank[pu] += 1
        else:
            self.parent[pu] = pv

    def find(self, v):
        if self.parent[v] == -1:
            return v
        return self.find(self.parent[v])

def mst(n, edges):
    ret = 0
    ufs = UFS(n) 
    edges.sort()
    for e in edges:
        w = e[0]
        u = e[1][0]
        v = e[1][1]
        if ufs.find(u) == ufs.find(v):
            continue
        ufs.union(u, v)
        ret += w
    return ret




def ans(graph):
    #print (graph)
    edges = []
    for u in range(len(graph)):
        for v in range(u + 1, len(graph[u])):
            edges.append([graph[u][v], (u, v)])
    return mst(len(graph), edges)

if __name__ == "__main__":
    n = int(input())
    graph = []
    for _ in range(n):
        row = list(map(int, input().strip().split()))
        graph.append(list(row))
    print (ans(graph))
