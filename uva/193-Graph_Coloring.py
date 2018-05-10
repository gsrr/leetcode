
def show_graph(graph):
    index = [ str(i) for i in range(len(graph))]
    print ("  ", ", ".join(index))
    for i in range(len(graph)):
        print (i, graph[i])


def bfs(graph, idx, visited):
    path = {'w':[], 'b' : []}
    for color in ['w', 'b']:
        lvisited = [0] * len(graph)
        q = [(idx, color)]
        while len(q) != 0:
            u, vc = q.pop(0)
            if lvisited[u] == 1:
                continue
            if vc == 'b':
                path[color].append(u)
            lvisited[u] = 1
            visited[u] = 1
            for v in range(len(graph[u])):
                if graph[u][v] != 0:
                    if vc == "w":
                        q.append((v, "b"))
                    else:
                        q.append((v, "w"))
    if len(path['w']) > len(path['b']):
        return path['w']
    else:
        return path['b']

def ans(graph):
    #show_graph(graph)
    visited = [0] * len(graph)
    ret = []
    for i in range(len(graph)):
        if visited[i] == 0:
            p = bfs(graph, i, visited)
            ret.extend(p)
    print(len(ret))
    for i in range(len(ret)):
        print(ret[i], end=" ")
    print("")

t = int(input())
for _ in range(t):
    n, e = map(int, input().split())
    graph = [ [0] * n for i in range(n) ]
    for i in range(e):
        u, v = map(int, input().split())
        graph[u - 1][v - 1] = 1
        graph[v - 1][u - 1] = 1
    ans(graph)
