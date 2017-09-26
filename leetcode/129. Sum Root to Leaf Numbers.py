# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
total = 0

def bfs(q):
    global total
    nq = []
    while len(q) != 0:
        tval, node = q.pop(0)
        tval = tval * 10 + node.val
        if node.left == None and node.right == None:
            total += tval
        else:
            if node.left != None:
                nq.append([tval, node.left])
            if node.right != None:
                nq.append([tval, node.right])
        
    if len(nq) != 0:
        bfs(nq)

class Solution(object):
    def sumNumbers(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        global total
        total = 0
        if root == None:
            return 0
        bfs([[0, root]])
        return total
        
