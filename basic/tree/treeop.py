import main

class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

def get_sub_ts(ts, i):
    j = i + 1
    cnt = 1
    while j < len(ts):
        if cnt == 0:
            return j
        if ts[j] == "(":
            cnt += 1
        elif ts[j] == ")":
            cnt -= 1
        j += 1
    return j 

def get_tree(ts):
    if ts == "":
        return None

    i = 0
    left = True
    root = Node(0)
    while i < len(ts):
        if ts[i] == "(":
            if left == True:
                j = get_sub_ts(ts, i)
                root.left = get_tree(ts[i + 1 : j - 1])
                i = j
                left = False
            else:
                j = get_sub_ts(ts, i)
                root.right = get_tree(ts[i + 1 : j - 1])
                i = j
        else:
            root.val = root.val * 10 + int(ts[i])
            i += 1
    return root

def dlr(root, ret):
    if root == None:
        return
    ret.append(str(root.val))
    dlr(root.left, ret)
    dlr(root.right, ret)
        

def ldr(root, ret):
    if root == None:
        return
    ldr(root.left, ret)
    ret.append(str(root.val))
    ldr(root.right, ret)
    

def ans(ts):
    root = get_tree(ts)
    ret1, ret2 = [], []

    dlr(root, ret1)
    ldr(root, ret2)
    return "%s+%s"%("".join(ret1), "".join(ret2))

def tree_height(root):
    if root == None:
        return 0
    return 1 + max(tree_height(root.left), tree_height(root.right))

def ans_height(ts):
    root = get_tree(ts)
    return "height=%d"%(tree_height(root))



if __name__ == "__main__":
    main.main(ans, 'cases')
    main.main(ans_height, 'cases.height')
