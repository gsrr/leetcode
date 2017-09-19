import collections
class Solution(object):
    def calcEquation(self, equations, values, queries):
        """
        :type equations: List[List[str]]
        :type values: List[float]
        :type queries: List[List[str]]
        :rtype: List[float]
        """
        graph = collections.defaultdict(dict)
        for i in xrange(len(equations)):
            v1 = equations[i][0]
            v2 = equations[i][1]
            val = values[i]
            graph[v1][v2] = val
            graph[v2][v1] = float(1/val)
        
        for i in graph.keys():
            for j in graph.keys():
                if i == j:
                    graph[i][j] = 1
                else:
                    if graph[i].has_key(j) == False:
                        graph[i][j] = 0x7fffffff
        for k in graph.keys():
            for i in graph.keys():
                for j in graph.keys():
                    if graph[i][k] != 0x7fffffff and graph[k][j] != 0x7fffffff:
                        if graph[i][k] * graph[k][j] < graph[i][j]:
                            graph[i][j] = graph[i][k] * graph[k][j]
        
        ret = []
        for i in xrange(len(queries)):
            v1 = queries[i][0]
            v2 = queries[i][1]
            if graph.has_key(v1) and graph[v1].has_key(v2):
                if graph[v1][v2] == 0x7fffffff:
                    ret.append(-1.0)
                else:
                    ret.append(graph[v1][v2])
            else:
                ret.append(-1.0)
        return ret
