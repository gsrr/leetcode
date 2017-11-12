# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

def is_parent(parr, p, q):
    while parr.has_key(q):
        if parr[q] == p:
            return True
        q = parr[q]
    return False


def lca(root, parr, p, q):
    if p == q:
        return p
    
    if is_parent(parr, p, q):
        return p
        
    return lca(root, parr, parr[p], q)

def dfs(node, parr):
    if node.left != None:
        parr[node.left] = node
        dfs(node.left, parr)
    if node.right != None:
        parr[node.right] = node
        dfs(node.right, parr)

def ans_1(root, p, q):
    '''
    1. Create parent array
    2. lca algorithm
    
    Time Complexity : O(n)
    Space Complexity : O(n)
    '''
    parr = {}
    dfs(root, parr)
    return lca(root, parr, p , q)

def dfs_path(root, p, p_path):
    if root == p:
        p_path.append(root)
        return True
    
    p_path.append(root)
    if root.left != None:
        if dfs_path(root.left, p, p_path) == True:
            return True
        
    if root.right != None:
        if dfs_path(root.right, p, p_path) == True:
            return True
    p_path.pop()
    return False

def ans_2(root, p, q):
    '''
    1. traverse path of p and path of q
    2. compare path of (p, q)
    
    Time Complexity : O(n)
    Space Complexity : O(n)
    '''
    p_path, q_path = [], []
    dfs_path(root, p, p_path)
    dfs_path(root, q, q_path)
    
    i = 0
    while i < len(p_path) and i < len(q_path):
        if p_path[i] != q_path[i]:
            break
        i += 1
    return p_path[i - 1]

def ans_3(root, p, q):
    '''
    Traverse once from root
    
    Time Complexity : O(n)
    Space Complexity : O(1)
    '''
    if root == None:
        return root
    
    if root == p or root == q:
        return root
    
    left = ans_3(root.left, p, q)
    right = ans_3(root.right, p, q)
    
    if left != None and right != None:
        return root
    
    return left if left != None else right
    
    

class Solution(object):
    def lowestCommonAncestor(self, root, p, q):
        """
        :type root: TreeNode
        :type p: TreeNode
        :type q: TreeNode
        :rtype: TreeNode
        """
        return ans_3(root, p, q)
        
        
