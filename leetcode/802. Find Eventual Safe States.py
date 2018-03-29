'''
It is not only one circle for eveny node.
maybe have two circle for a node

0 -> 1 -> 0
0 -> 2 -> 0

'''

def find_circle(graph, path, node):
    path[node] = True
    for next_node in graph[node]:
        if path.has_key(next_node):
            return True
        ret = find_circle(graph, path, next_node)
        if ret == True:
            return True
    del path[node]
    return False

def find_all_circle(graph, path, hist, node, safe_node):
    path[node] = True
    if len(graph[node]) == 0: # terminal node
        for p_node in path.keys():
            if safe_node[p_node] != 2:
                safe_node[p_node] = 1 # type 1 is terminal node.

    for next_node in graph[node]:
        if path.has_key(next_node): # have cycle
            #print path
            for p_node in path.keys():
                safe_node[p_node] = 2 # type 2 is cycle node.
            continue
        if safe_node[next_node] != 0:
            if safe_node[next_node] == 2:
                for p_node in path.keys():
                    safe_node[p_node] = 2
            else:
                for p_node in path.keys():
                    if safe_node[p_node] != 2:
                        safe_node[p_node] = 1
            continue
        find_all_circle(graph, path, hist, next_node, safe_node)
    del path[node]
    return False

def ans1(graph):
    '''
    Result : Time expired
    Time Complexity : O(v^2)
    '''
    safe_node = [0] * len(graph)
    for i in xrange(len(graph)):
        hist = [0] * len(graph)
        path = {}
        find_all_circle(graph, path, hist, i, safe_node)
    return [i for i in xrange(len(safe_node)) if safe_node[i] == 0]

# ok, so... how to optimal this solution?
def ans2(graph):
    cycle_node = [0] * len(graph)
    for i in xrange(len(graph)):
        if cycle_node[i] != 0:
            continue
        hist = [0] * len(graph)
        path = {}
        find_all_circle(graph, path, hist, i, cycle_node)
    return [i for i in xrange(len(cycle_node)) if cycle_node[i] == 1]

class Solution(object):
    def eventualSafeNodes(self, graph):
        """
        :type graph: List[List[int]]
        :rtype: List[int]
        """
        return ans2(graph)
