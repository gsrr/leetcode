import collections


def ans(n, graph):
    print (graph)

n, m = map(int, input().split())
graph = collections.defaultdict(list)
for _ in range(m):
    u, v = map(int, input().split())
    graph[u].append(v)
    graph[v].append(u)
print (ans(n, graph))

