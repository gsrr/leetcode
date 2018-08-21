import random
import time

class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

def tree_insert(i, root):
    if root == None:
       return TreeNode(i) 

    q = [root]
    for node in q:
        if node.left != None:
            q.append(node.left)
        else:
            node.left = TreeNode(i)
            break
        if node.right != None:
            q.append(node.right)
        else:
            node.right = TreeNode(i)
            break
    return root

def tree_create(arr):
    root = None
    for i in arr:
        root = tree_insert(i, root)
    return root
