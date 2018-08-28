# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

import copy

def dfs(n):
    if n == 0:
        return []
    
    if n == 1:
        return [TreeNode(0)]
    
    ret = []
    n = n - 1
    for i in xrange(1, n):
        larr = dfs(i)
        rarr = dfs(n - i)
        for j in xrange(len(larr)):
            for k in xrange(len(rarr)):
                root = TreeNode(0)
                root.left = larr[j]
                root.right = rarr[k]
                ret.append(root)
    return ret
        
def ans(n):
    '''
    Result : Fail (Time Exceed)
    Analysis:
    1. Catalan number
    '''
    
    if n % 2 == 0:
        return []
    
    if n == 1:
        return [TreeNode(0)]
    
    ret = []
    n = n - 1
    for i in xrange(1, n):
        larr = dfs(i)
        rarr = dfs(n - i)
        for j in xrange(len(larr)):
            for k in xrange(len(rarr)):
                root = TreeNode(0)
                root.left = larr[j]
                root.right = rarr[k]
                ret.append(root)
    return ret
    
class Solution(object):
    def allPossibleFBT(self, N):
        """
        :type N: int
        :rtype: List[TreeNode]
        """
        return ans(N)
