# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

def dfs(root, arr):
    if root.left != None:
        dfs(root.left, arr)
    
    if root.left == None and root.right == None:
        arr.append(root.val)
    if root.right != None:
        dfs(root.right, arr)
    
class Solution(object):
    def leafSimilar(self, root1, root2):
        """
        :type root1: TreeNode
        :type root2: TreeNode
        :rtype: bool
        """
        arr1 = []
        arr2 = []
        dfs(root1, arr1)
        dfs(root2, arr2)
        return arr1 == arr2
        
