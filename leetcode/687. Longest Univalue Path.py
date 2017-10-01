# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

mlens = 0

def dfs(root):
    global mlens
    llen = 0
    rlen = 0
    if root.left != None:
        if root.left.val == root.val:
            llen = 1 + dfs(root.left)
        else:
            dfs(root.left)
    if root.right != None:
        if root.right.val == root.val:
            rlen = 1 + dfs(root.right)
        else:
            dfs(root.right)
    mlens = max(mlens, llen + rlen)
    return max(llen, rlen)
    

class Solution(object):
    def longestUnivaluePath(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if root == None:
            return 0
        global mlens
        mlens = 0
        dfs(root)
        return mlens
