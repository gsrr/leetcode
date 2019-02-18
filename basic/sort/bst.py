import main

class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

def insert_bst(root, val):
    if root == None:
        return Node(val)

    if val > root.val:
        root.right = insert_bst(root.right, val)
    else:
        root.left = insert_bst(root.left, val)

    return root
    
def create_bst(arr):
    root = None
    for i in xrange(len(arr)):
        root = insert_bst(root, arr[i])
    return root

def pre_order(root, ret):
    if root.left != None:
        pre_order(root.left, ret)
    ret.append(root.val)

    if root.right != None:
        pre_order(root.right, ret)

def bst(arr):
    root = create_bst(arr)
    ret = []
    pre_order(root, ret)
    return ret

def ans(arr):
    arr = bst(arr)
    return ",".join( [str(x) for x in arr] )

if __name__ == "__main__":
    main.main(ans)
