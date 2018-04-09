tion for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

def recur_util(node):
    if node.left == None and node.right == None:
        return node.val
    
    lval = 0
    rval = 0
    if node.left != None:
        lval = recur_util(node.left)
    if node.right != None:
        rval = recur_util(node.right)
    if lval == 0:
        node.left = None
    if rval == 0:
        node.right = None
    return lval + rval + node.val    
    
def ans1(root):
    if root == None:
        return root
    lval = 0
    rval = 0
    if root.left != None:
        lval = recur_util(root.left)
    if root.right != None:
        rval = recur_util(root.right)
    if lval == 0:
        root.left = None
    if rval == 0:
        root.right = None
    return root

class Solution(object):
    def pruneTree(self, root):
        """
        :type root: TreeNode
        :rtype: TreeNode
        """
        return ans1(root)
