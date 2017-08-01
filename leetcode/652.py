# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

def bfs(root):
    ret = []
    q = [("",root)]
    while len(q) != 0:
        key, nd = q.pop(0)
        ret.append((key,nd))
        if nd.left != None:
            q.append((key + "l", nd.left))
        if nd.right != None:
            q.append((key + "r", nd.right))
    return ret

def bfsval(root):
    ret = []
    q = [root]
    while len(q) != 0:
        nd = q.pop(0)
        if nd != None:
            ret.append(str(nd.val))
        else:
            ret.append("null")
            continue
        q.append(nd.left)
        q.append(nd.right)
    return ret

def tree_comp(r1, r2):
    if r1 == None and r2 == None:
        return True
    elif r1 == None and r2 != None:
        return False
    elif r1 != None and r2 == None:
        return False
    else:
        if r1.val != r2.val:
            return False
        if tree_comp(r1.left, r2.left) == True:
            return tree_comp(r1.right, r2.right)
        else:
            return False
         
def dfs(node, dic_tree, dic_keyNode, dic_str):
    if node == None:
        keystr = "none"
    else:  
        dfs(node.left, dic_tree, dic_keyNode, dic_str)
        dfs(node.right, dic_tree, dic_keyNode, dic_str)
        keystr = "(" + dic_str[node.left] + ")" + str(node.val) + "(" + dic_str[node.right] + ")"
    dic_str[node] = keystr
    dic_keyNode[keystr] = node
    dic_tree[keystr] += 1

import collections
class Solution(object):
    def findDuplicateSubtrees(self, root):
        """
        :type root: TreeNode
        :rtype: List[TreeNode]
        """
        if root == None:
            return []
        dic_tree = collections.defaultdict(int)
        rret = []
        dic_str = {}
        dic_keyNode = {}
        dfs(root, dic_tree, dic_keyNode, dic_str)
        for key in dic_tree.keys():
            if key != "none" and dic_tree[key] > 1:
                rret.append(dic_keyNode[key])
        return rret
