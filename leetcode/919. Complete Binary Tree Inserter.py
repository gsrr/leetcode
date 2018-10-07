# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class CBTInserter(object):

    def __init__(self, root):
        """
        :type root: TreeNode
        """
        self.root = root
        

    def insert(self, v):
        """
        :type v: int
        :rtype: int
        """
        # bfs
        q = [self.root]
        while len(q) != 0:
            node = q.pop(0)
            if node.left == None:
                node.left = TreeNode(v)
                return node.val
            q.append(node.left)
            if node.right == None:
                node.right = TreeNode(v)
                return node.val
            q.append(node.right)
            
            
    def get_root(self):
        """
        :rtype: TreeNode
        """
        return self.root


# Your CBTInserter object will be instantiated and called as such:
# obj = CBTInserter(root)
# param_1 = obj.insert(v)
# param_2 = obj.get_root()
