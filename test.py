

class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

ret = []
def bst_inorder(node):
    if node == None:
        return
    bst_inorder(node.left)
    ret.append(node.val)
    bst_inorder(node.right)

t = TreeNode(5)
t1 = TreeNode(3)
t2 = TreeNode(6)
t.left = t1
t.right = t2
bst_inorder(t)
print ret
data = ret

min_val = data[1] - data[0]
for i in xrange(1, len(data)):
    tmp = data[i] - data[i-1]
    min_val = tmp if tmp < min_val else min_val

print min_val
