class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

def levelorder(root):
    ret = []
    q = [root]
    for item in q:
        if item == None:
            ret.append(item)
        else:
            ret.append(item.val)
            q.append(item.left)
            q.append(item.right)
    return ret

def ans(s):
    start = 0
    for i in xrange(len(s)):
        if s[i] == "(" or s[i] == ")":
            break
        else:
            start += 1
    root = TreeNode(int(s[:start]))
    if start == len(s):
        return root
    para = 0
    left_s = 0
    left_e = 0
    right_s = 0
    right_e = 0
    for i in xrange(len(s)):
        if s[i] == "(":
            para -= 1
        elif s[i] == ")":
            para += 1
        if s[i] == "(" and para == -1:
            if left_e != 0:
                right_s = i
            else:
                left_s = i
        if s[i] == ")" and para == 0:
            if left_e != 0:
                right_e = i
            else:
                left_e = i
    if s[left_s + 1:left_e] != "":
        root.left = ans(s[left_s + 1 : left_e]) 
    if s[right_s + 1:right_e] != "":
        root.right = ans(s[right_s + 1 : right_e]) 
    return root

s = "4(2(3)(1))(6(5))"
print ans(s)
print "----------------"
s = "4(2(31)(1))(6(5))"
print ans(s)
print "----------------"
s = "4(-2(31)(1))(6(5))"
print ans(s)
print "----------------"
s = "-4(-2(31)(1))(6(5))"
root =  ans(s)
print levelorder(root)
