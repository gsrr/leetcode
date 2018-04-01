'''Please note that it's Function problem i.e.
you need to write your solution in the form of Function(s) only.
Driver Code to call/invoke your function would be added by GfG's Online Judge.'''


# Your task is to complete this function
# Function should return Topologically Sorted List
# Graph(graph) is a defaultict of type List
# n is no of edges

def topoSort_util(v, graph, hist, stack):
    hist[v] = True
    
    for nv in graph[v]:
        if nv not in hist:
            topoSort_util(nv, graph, hist, stack)
    stack.append(v)
    
def topoSort(n, graph):
    # Code here
    '''
    Time complexity : O(V + E) --> we will run all nodes and all edges.
    '''
    hist = {}
    stack = []
    for v in range(n):
        if v not in hist:
            topoSort_util(v, graph, hist, stack)
    #print (stack)
    #print (stack[::-1])
    return stack[::-1]`
