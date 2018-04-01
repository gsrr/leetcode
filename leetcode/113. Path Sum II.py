# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

def dfs(node, summ, path, ret):
    path.append(node.val)
    if node.left == None and node.right == None: # is leaf node
        if node.val == summ:
            ret.append(list(path))
    else:
        if node.left != None:
            dfs(node.left, summ - node.val, path, ret)

        if node.right != None:
            dfs(node.right, summ - node.val, path, ret)
    path.pop()
    
def ans1(root, summ):
    if root == None:
        return []
    
    ret = []
    path = []
    dfs(root, summ, path, ret)
    return ret
    
class Solution(object):
    def pathSum(self, root, summ):
        """
        :type root: TreeNode
        :type sum: int
        :rtype: List[List[int]]
        """
        return ans1(root, summ)        
