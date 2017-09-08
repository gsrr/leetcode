# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

import re

def get_child(child):
    ret = []
    bs = 0
    s = 0
    for i in xrange(len(child)):
        if child[i] == "(":
            bs += 1
        elif child[i] == ")":
            bs -= 1
        if bs == 0:
            ret.append(child[s:i+1])
            s = i + 1
    return ret[0], ret[1]

class Codec:

    def serialize(self, root):
        """Encodes a tree to a single string.
        
        :type root: TreeNode
        :rtype: str
        """
        if root == None:
            return ""
        
        ret = str(root.val) + "(" + self.serialize(root.left) + ")" + "(" + self.serialize(root.right) + ")"
        return ret
        

    def deserialize(self, data):
        """Decodes your encoded data to tree.
        
        :type data: str
        :rtype: TreeNode
        """
        if data == "":
            return None
        obj = re.match(r'([-0-9]+)\(.*\)\(.*\)', data)
        val = int(obj.group(1))
        child = data[len(obj.group(1)):]
        lchild, rchild = get_child(child)
        node = TreeNode(val)
        node.left = self.deserialize(lchild[1:-1])
        node.right = self.deserialize(rchild[1:-1])
        return node

# Your Codec object will be instantiated and called as such:
# codec = Codec()
# codec.deserialize(codec.serialize(root))
