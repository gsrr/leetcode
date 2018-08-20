# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

def ans(pre, post):
    #print pre, post
    if len(pre) == 0:
        return None
    
    val = pre[0]
    root = TreeNode(val)
    
    if len(pre) == 1:
        return root
    
    prei = 0
    posti = 0
    for i in xrange(len(post)):
        if post[i] == pre[1]:
            posti = i + 1
            prei = posti + 1
            break
    #print "left:", pre[1:prei], post[0:posti]
    #print "right:", pre[prei:], post[posti:-1]
    root.left = ans(pre[1:prei], post[0:posti])
    root.right = ans(pre[prei:], post[posti:-1])
    return root
    
class Solution(object):
    def constructFromPrePost(self, pre, post):
        """
        :type pre: List[int]
        :type post: List[int]
        :rtype: TreeNode
        """
        return ans(pre, post)    
