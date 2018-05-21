import collections

def create_dic_graph(edges):
    graph = collections.defaultdict(list)
    for e in edges:
        graph[e[0]].append(e[1])
    return graph

def ans(edges):
    graph = create_dic_graph(edges)
    keys = graph.keys()

    dic = collections.defaultdict(int)
    for u in keys:
        if dic.has_key(u) == False:
            dic[u] = 0
        for v in graph[u]:
            dic[v] += 1 # in-degree

    root = 0
    cnt = 0
    for key in dic.keys():
        if dic[key] == 0:
            root = key
            cnt += 1
    if cnt > 1:
        #print "multiple roots"
        return False

    cnt = 0
    for key in dic.keys():
        if dic[key] > 1:
            #print "mutiple in-degree"
            cnt += 1

    if cnt > 0:
        return False
    return True


def add_edges(edges, line):
    for i in range(0, len(line), 2):
        edges.append([line[i], line[i + 1]])
    

def find_root(graph):
    keys = graph.keys()

    dic = collections.defaultdict(int)
    for u in keys:
        if u not in dic:
            dic[u] = 0
        for v in graph[u]:
            dic[v] += 1 # in-degree
    for key in dic.keys():
        if dic[key] == 0:
            return (key, dic)
    return (-1, dic)

def bfs(graph, root, nodes):
    q = [root]
    hist = {}
    while len(q) != 0:
        u = q.pop(0)
        if u in hist:
            return False
        hist[u] = True
        for v in graph[u]:
            q.append(v)
    
    for v in nodes.keys():
        if v not in hist:
            return False
    return True

def ans1(edges):
    '''
    bfs
    '''
    if len(edges) == 0:
        return True
    graph = create_dic_graph(edges)
    root, dic = find_root(graph) 
    if root == -1:
        return False
    return bfs(graph, root, dic)

def recur_util(graph, u, hist):
    if u in hist:
        return False

    hist[u] = True
    for v in graph[u]:
        ret = recur_util(graph, v, hist)
        if ret == False:
            return False
    return True

def dfs(graph, root, dic):
    hist = {}
    ret = recur_util(graph, root, hist)
    if ret == False:
        return False
    
    for v in dic.keys():
        if v not in hist:
            return False
    return True

def ans2(edges):
    '''
    adjancency list + dfs
    '''
    if len(edges) == 0:
        return True
    graph = create_dic_graph(edges)
    root, dic = find_root(graph) 
    if root == -1:
        return False
    return dfs(graph, root, dic)

cnt = 1
edges = []
while True:
    line = list(map(int, input().strip().split()))
    if len(line) == 0:
        continue
    
    if line[0] == -1:
        break

    add_edges(edges, line)
    if line[-1] == 0:
        edges.pop()
        if ans2(edges) == True:
            print ("Case %d is a tree."%(cnt))
        else:
            print ("Case %d is not a tree."%(cnt))
        edges = []
        cnt += 1
