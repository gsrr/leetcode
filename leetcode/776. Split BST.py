# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

def split(root, V):
    if root == None:
        return [None, None]
    
    if V >= root.val:
        ret = split(root.right, V)
        root.right = ret[0]
        ret[0] = root
    else:
        ret = split(root.left, V)
        root.left = ret[1]
        ret[1] = root
        
    return ret
    
class Solution(object):
    def splitBST(self, root, V):
        """
        :type root: TreeNode
        :type V: int
        :rtype: List[TreeNode]
        """
        return split(root, V)
