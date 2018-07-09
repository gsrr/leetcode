# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

def is_parent(parent, v1, v2):
    while parent[v2] != -1:
        if parent[v2] == v1:
            return True
        v2 = parent[v2]
    return False

def find_parent(parent, v1, v2):
    while is_parent(parent, v1, v2) == False:
        v1 = parent[v1]    
    return v1

def bfs(root):
    parent = [-1] * 500
    arr = []
    q = [(0, root)]
    depth = 0
    while len(q) != 0:
        depth, node = q.pop(0)
        arr.append([depth, node.val])
        if node.left != None:
            parent[node.left.val] = node.val
            q.append((depth + 1, node.left))
        if node.right != None:
            parent[node.right.val] = node.val
            q.append((depth + 1, node.right))
    #arr.sort()
    rarr = arr[::-1]
    #print rarr
    #print parent
    gmax = rarr[0][0]
    tval = rarr[0][1]
    for i in xrange(1, len(rarr)):
        if rarr[i][0] != gmax:
            break
        tval = find_parent(parent, tval, rarr[i][1])
    #print tval
    
    q = [root]
    while len(q) != 0:
        node = q.pop(0)
        if node.val == tval:
            return node
        if node.left != None:
            q.append(node.left)
        if node.right != None:
            q.append(node.right)

class Solution(object):
    def subtreeWithAllDeepest(self, root):
        """
        :type root: TreeNode
        :rtype: TreeNode
        """
        return bfs(root)
