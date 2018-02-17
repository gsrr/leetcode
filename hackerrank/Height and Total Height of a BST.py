#!/bin/python

#from __future__ import print_function

import os
import sys
sys.setrecursionlimit(10000)


# Complete the function below.
class TreeNode:
    def __init__(self, val):
        self.left = None
        self.right = None
        self.val = val

def bst_insert(root, node):
    if root == None:
        root = node
        return root
    
    if node.val > root.val:
        root.right = bst_insert(root.right, node)
    elif node.val < root.val:
        root.left = bst_insert(root.left, node)
    else:
        pass
    return root


def showTree(root):
    if root.left != None:
        showTree(root.left)
    print root.val
    
    if root.right != None:
        showTree(root.right)

total_height = 0        

def bst_height(root):
    global total_height
    lh = 0
    rh = 0
    if root.left != None:
        lh = 1 + bst_height(root.left)
        
    if root.right != None:
        rh = 1 + bst_height(root.right)
    total_height += max(lh, rh)  
    return max(lh, rh)    
    
def heightAndTotalHeight(arr):
    # Write your code here.
    global total_height
    total_height = 0
    root = None
    for i in xrange(len(arr)):
        node = TreeNode(arr[i])
        root = bst_insert(root, node)
    #print root
    #showTree(root)
    root_height = bst_height(root)
    return [root_height, total_height]

if __name__ == '__main__':
    f = open(os.environ['OUTPUT_PATH'], 'w')

    arr_size = int(raw_input())

    arr = map(int, raw_input().rstrip().split())

    result = heightAndTotalHeight(arr)

    f.write("\n".join(map(str, result)))

    f.write('\n')

    f.close()

