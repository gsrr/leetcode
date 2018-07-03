# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

def convert_graph(root, graph):
    q = [root]
    while len(q) != 0:
        node = q.pop(0)
        pval = node.val
        if node.left != None:
            cval = node.left.val
            graph[pval][cval] = 1
            graph[cval][pval] = 1
            q.append(node.left)
        if node.right != None:
            cval = node.right.val
            graph[pval][cval] = 1
            graph[cval][pval] = 1
            q.append(node.right)
    


def bfs(graph, target, K):
    ret = {}
    q = [(target.val, 0)]
    hist = {}
    while len(q) != 0:
        u, dist = q.pop(0)
        if hist.has_key(u) == True:
            continue
        hist[u] = True
        if dist == K:
            ret[u] = True
            continue
        if dist > K:
            continue
        for v in xrange(len(graph[u])):
            if graph[u][v] == 1:
                q.append((v, dist + 1))
    return ret.keys()

def ans(root, target, K):
    graph = [ [0] * 501 for _ in xrange(501) ]
    convert_graph(root, graph)
    ret = bfs(graph, target, K)
    return ret

class Solution(object):
    def distanceK(self, root, target, K):
        """
        :type root: TreeNode
        :type target: TreeNode
        :type K: int
        :rtype: List[int]
        """
        return ans(root, target, K)
        
