import collections

def create_dic_graph(edges):
    graph = collections.defaultdict(list)
    for e in edges:
        if e[0] == 0 and e[1] == 0:
            continue
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

cnt = 1
edges = []
while True:
    line = map(int, raw_input().strip().split())
    if len(line) == 0:
        if ans(edges) == True:
            print "Case %d is a tree."%(cnt)
        else:
            print "Case %d is not a tree."%(cnt)

        edges = []
        cnt += 1
        continue

    if line[0] == -1 and line[1] == -1:
        if ans(edges) == True:
            print "Case %d is a tree."%(cnt)
        else:
            print "Case %d is not a tree."%(cnt)
        cnt += 1
        break
    
    for i in xrange(0, len(line), 2):
        edges.append([line[i], line[i + 1]])
     
