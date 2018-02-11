# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

def ldr(node, arr):
    if node.left != None:
        ldr(node.left, arr)
    arr.append(node.val)
    
    if node.right != None:
        ldr(node.right, arr)
    
class Solution(object):
    def minDiffInBST(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if root == None:
            return 0
        arr = []
        ldr(root, arr)    
        minval = arr[1] - arr[0]
        for i in xrange(2, len(arr)):
            minval = min(arr[i] - arr[i - 1], minval)
        return minval
