# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

def compare(node, t):
    q1 = [node]
    q2 = [t]
    while len(q1) != 0 and len(q2) != 0:
        n1 = q1.pop(0)
        n2 = q2.pop(0)
        if n1.val != n2.val:
            return False
        if n1.left != None:
            q1.append(n1.left)
        if n1.right != None:
            q1.append(n1.right)
        if n2.left != None:
            q2.append(n2.left)
        if n2.right != None:
            q2.append(n2.right)   
    if len(q1) == 0 and len(q2) == 0:
        return True
    else:
        return False
    
def bfs(s, t):
    q = [s]
    while len(q) != 0:
        node = q.pop(0)
        if node.val == t.val:
            print node.val, t.val
            ret = compare(node, t)
            if ret == True:
                return True
        if node.left != None:
            q.append(node.left)
        if node.right != None:
            q.append(node.right)
    return False

def ans1(s, t):
    return bfs(s, t)

def dfs(s, tarr):
    tarr.append(s.val)
    if s.left != None:
        dfs(s.left, tarr)
    if s.right != None:
        dfs(s.right, tarr)
    tarr.append(s.val)
    
def ans(s, t):
    sarr = []
    tarr = []
    dfs(s, sarr)
    dfs(t, tarr)
    #print sarr
    #print tarr
    for i in xrange(len(sarr) - len(tarr) + 1):
        j = 0
        while j < len(tarr):
            if sarr[i + j] != tarr[j]:
                break
            j += 1
        if j == len(tarr):
            return True
    return False
    
class Solution(object):
    def isSubtree(self, s, t):
        """
        Is t a subtree of s?
        
        :type s: TreeNode
        :type t: TreeNode
        :rtype: bool
        """
        if s == None and t == None:
            return True
        elif s == None and t != None:
            return False
        elif s != None and t == None:
            return False
        return ans(s, t)    
        
