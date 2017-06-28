

def lds_loop(root, k):
    stack = []
    tmp = root
    while tmp:
        stack.append(tmp)
        tmp = tmp.left
    
    cnt = 0
    while stack and cnt < (k - 1):
        node = stack.pop()
        cnt += 1
        right = node.right
        while right:
            stack.append(right)
            right = right.left
    return stack.pop().val
