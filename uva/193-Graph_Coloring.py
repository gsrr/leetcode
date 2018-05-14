
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

def ans1(graph):
    '''
    Wrong
    '''
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

import time

def dfs(graph, u, color, path, visited, preblock, local = []):
    path.append(u)
    visited[u] = 1
    cnt = 1 if color == "b" else 0
    gb = [str(u)] if color == "b" else []
    for v in range(len(graph[u])):
        if v in path: 
            continue
        if graph[u][v] != 0:
            if color == "b":
                block = [ v for v in range(len(graph[u])) if graph[u][v] != 0 ]
                tcnt, tb = dfs(graph, v, "w", path, visited, preblock + block)
                tcnt += 1
                tb = [str(u)] + tb
            else:
                if v in preblock:
                    tcnt, tb = dfs(graph, v, "w", path, visited, preblock)
                else:
                    tcnt, tb = dfs(graph, v, "w", path, visited, preblock)
                    tcnt2, tb2 = dfs(graph, v, "b", path, visited, preblock)
                    if tcnt < tcnt2:
                        tcnt = tcnt2
                        tb = tb2
                
            if tcnt > cnt:
                cnt = tcnt
                gb = tb

    path.pop()
    return (cnt, gb)

def ans2(graph):
    '''
    Complicated
    '''
    show_graph(graph)
    cnt = 0
    gb = []
    visited = [0] * len(graph)
    for i in range(len(graph)):
        if visited[i] == 0:
            path = []
            block = []
            t1, b1 = dfs(graph, i, "w", path, visited, block)
            t2, b2 = dfs(graph, i, "b", path, visited, block)
            if t1 > t2:
                cnt += t1
                gb += b1
            else:
                cnt += t2
                gb += b2

    print (cnt, gb)
    return cnt

ret = 0
colors = None
gcnt = 0

def valid(graph, u, lcolors):
    for v in graph[u]:
        if lcolors[v] == 'b':
            return False
    return True


def recur_uril(n, graph, u, lcolors):
    global colors
    global ret
    global gcnt
    gcnt += 1

    if u == n:
        cnt = 0
        for c in lcolors:
            if c == 'b':
                cnt += 1
        if cnt > ret:
            ret = cnt
            colors = list(lcolors)
        return 

    for c in ['b', 'w']:
        lcolors[u] = c
        if c == 'b':
            if valid(graph, u, lcolors) == False:
                continue
            for v in graph[u]:
                lcolors[v] = "w"
        else:
            for v in graph[u]:
                lcolors[v] = 0
        if lcolors[u + 1] == 0: 
            recur_uril(n, graph, u + 1, lcolors)
        lcolors[u] = 0

def ans(n, graph):
    global colors
    global ret
    global gcnt
    colors = [0] * n
    ret = 0
    lcolors = [0] * n
    recur_uril(n, graph, 0, lcolors)
    print (ret)
    for i in range(len(colors)):
        if colors[i] == 'b':
            print (i + 1, end = " ")
    print ("")
    print ("gcnt:", gcnt)
import collections

t = int(input())
for _ in range(t):
    n, e = map(int, input().split())
    graph = collections.defaultdict(list)
    for i in range(e):
        u, v = map(int, input().split())
        graph[u - 1].append(v - 1)
        graph[v - 1].append(u - 1)
    ans(n, graph)
