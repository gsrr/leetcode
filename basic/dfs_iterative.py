import tree

'''
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
'''
def dfs_iterative(root):
    # DLR
    ret = []
    st = [root]
    while len(st) != 0:
        node = st.pop()
        ret.append(node.val)
        if node.right != None:
            st.append(node.right)
        if node.left != None:
            st.append(node.left)
    return ret
    

def test_dfs_iterative_tree():
    '''
            1
          /   \
         2     3
        / \   / \
       4   5 6   7

    bfs : 1,2,3,4,5,6,7
    dfs_iterative(dlr) : 1,2,4,5,3,6,7
    '''
    arr = [1,2,3,4,5,6,7]
    print "arr:", arr
    root = tree.tree_create(arr)
    print "dfs_iterative:", dfs_iterative(root)

test_dfs_iterative_tree()
