# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None




class Solution(object):
    
    
    def sort_bst(self, root):
        if root == None:
            return
    
        self.sort_bst(root.left)
        self.ret.append(root.val)
        self.sort_bst(root.right)
    
    def getMinimumDifference(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        self.ret = []
        self.sort_bst(root)
        print self.ret
        min_val = self.ret[1] - self.ret[0]
        cnt = 1
        while cnt < len(self.ret) - 1:
            temp = self.ret[cnt + 1] - self.ret[cnt]
            min_val = min_val if temp > min_val else temp
            cnt += 1
        return min_val
        
