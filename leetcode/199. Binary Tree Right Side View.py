# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

ret = []

def bfs(q):
    global ret
    ret.append(q[-1].val)
    nq = []
    while len(q) != 0:
        node = q.pop(0)
        if node.left != None:
            nq.append(node.left)
        if node.right != None:
            nq.append(node.right)
    
    if len(nq) != 0:
        bfs(nq)
    return

class Solution(object):
    def rightSideView(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        global ret
        ret = []
        if root == None:
            return []
        q = [root]
        bfs(q)
        return ret
