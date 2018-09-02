# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
arr = []

def ldr(root):
    global arr
    if root.left != None:
        ldr(root.left)
    arr.append(root.val)
    if root.right != None:
        ldr(root.right)
    
    
def ans(root):
    global arr
    arr = []
    ldr(root)
    print arr
    nr = TreeNode(arr[0])
    tmp = nr
    for i in xrange(1, len(arr)):
        tmp.right = TreeNode(arr[i])
        tmp = tmp.right
    return nr
    
class Solution(object):
    def increasingBST(self, root):
        """
        :type root: TreeNode
        :rtype: TreeNode
        """
        return ans(root)
        
