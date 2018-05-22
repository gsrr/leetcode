from collections import defaultdict
  
class Graph:
  
    def __init__(self,vertices):
        self.V = vertices 
        self.graph = defaultdict(list) 
        self.Time = 0
  
    def addEdge(self,u,v):
        self.graph[u].append(v)
         
    def SCCUtil(self,u, low, visited, path):
        visited[u] = self.Time
        low[u] = self.Time
        self.Time += 1
        path.append(u)
 
        for v in self.graph[u]:
            if visited[v] == -1 :
                self.SCCUtil(v, low, visited, path)
                low[u] = min(low[u], low[v])

            elif v in path: 
                low[u] = min(low[u], low[v])
 
        w = -1
        if low[u] == visited[u]:
            while w != u:
                w = path.pop()
             
    def SCC(self):
        visited = [-1] * (self.V)
        low = [-1] * (self.V)
        st =[]
         
        for u in range(self.V):
            if visited[u] == -1:
                path = []
                self.SCCUtil(u, low, visited, path)
        print low
  
# Create a graph given in the above diagram
'''
g1 = Graph(5)
g1.addEdge(1, 0)
g1.addEdge(0, 2)
g1.addEdge(2, 1)
g1.addEdge(0, 3)
g1.addEdge(3, 4)
print "SSC in first graph "
g1.SCC()
'''
g1 = Graph(5)
g1.addEdge(0, 1)
g1.addEdge(1, 2)
g1.addEdge(2, 3)
g1.addEdge(3, 0)
g1.addEdge(3, 4)
g1.addEdge(4, 1)
print "SSC in first graph "
g1.SCC()

g2 = Graph(4)
g2.addEdge(0, 1)
g2.addEdge(1, 2)
g2.addEdge(2, 3)
print "nSSC in second graph "
g2.SCC()
 
  
g3 = Graph(7)
g3.addEdge(0, 1)
g3.addEdge(1, 2)
g3.addEdge(2, 0)
g3.addEdge(1, 3)
g3.addEdge(1, 4)
g3.addEdge(1, 6)
g3.addEdge(3, 5)
g3.addEdge(4, 5)
print "nSSC in third graph "
g3.SCC()
 
g4 = Graph(11)
g4.addEdge(0, 1)
g4.addEdge(0, 3)
g4.addEdge(1, 2)
g4.addEdge(1, 4)
g4.addEdge(2, 0)
g4.addEdge(2, 6)
g4.addEdge(3, 2)
g4.addEdge(4, 5)
g4.addEdge(4, 6)
g4.addEdge(5, 6)
g4.addEdge(5, 7)
g4.addEdge(5, 8)
g4.addEdge(5, 9)
g4.addEdge(6, 4)
g4.addEdge(7, 9)
g4.addEdge(8, 9)
g4.addEdge(9, 8)
print "nSSC in fourth graph "
g4.SCC();
 
 
g5 = Graph (5)
g5.addEdge(0, 1)
g5.addEdge(1, 2)
g5.addEdge(2, 3)
g5.addEdge(2, 4)
g5.addEdge(3, 0)
g5.addEdge(4, 2)
print "nSSC in fifth graph "
g5.SCC();
 
#This code is contributed by Neelam Yadav

