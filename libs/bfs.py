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

def bfs(root):
    ret = []
    q = [root]
    for item in q:
        if item != None:
            ret.append(item.val)
            q.append(item.left)
            q.append(item.right)
    return ret

def test_bfs_tree():
    arr = [random.randint(0,100) for i in xrange(10)]
    print arr
    root = tree_create(arr)
    print bfs(root)

test_bfs_tree()
