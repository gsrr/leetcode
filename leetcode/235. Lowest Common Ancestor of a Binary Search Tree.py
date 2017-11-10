# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

def dfs(root, parr):
    if root.left != None:
        parr[root.left] = root
        dfs(root.left, parr)
        
    if root.right != None:
        parr[root.right] = root
        dfs(root.right, parr)
    
def is_parent(parr, pnode, node):
    while parr.has_key(node):
        if parr[node] == pnode:
            return True
        node = parr[node]
    return False

def lca(parr, p, q):
    if p == q:
        return p
    
    if is_parent(parr, p, q):
        return p
    
    return lca(parr, parr[p], q)
        

def ans_3(root, p, q):
    '''
    Iteration solution
    
    Time complexity : O(log(n))
    '''
    while root:
        if root.val > p.val and root.val > q.val:
            root = root.left
        elif root.val < p.val and root.val < q.val:
            root = root.right
        else:
            return root
    
def ans_2(root, p, q):
    '''
    '''
    parr = {}
    dfs(root, parr)
    return lca(parr, p, q)

def ans_1(root, p, q):
    '''
    1. Create parent mapping array
    2. check is_parent recursively 
    
    Time Complexity : O(n)
    '''
    if root.val > p.val and root.val > q.val:
        return ans_1(root.left, p, q)

    if root.val < p.val and root.val < q.val:
        return ans_1(root.right, p, q)

    return root


class Solution(object):
    def lowestCommonAncestor(self, root, p, q):
        """
        :type root: TreeNode
        :type p: TreeNode
        :type q: TreeNode
        :rtype: TreeNode
        """
        if root == None:
            return root
        print p.val, q.val
        return ans_3(root, p, q)
        
