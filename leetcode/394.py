import sys

import itertools

def test(cases, cn = 1):
    cnt = 0
    while cnt < cn and cnt < len(cases):
        print "case:", cnt + 1 
        ret = ans(*cases[cnt])
        print "\n\tret:", ret
        print "-" * 10
        cnt += 1

def factor(n):
    ret = []
    cnt = 1
    while cnt * cnt <= n:
        if n % cnt == 0:
            ret.append(cnt)
            ops = n / cnt
            if cnt != 1 and ops != cnt:
                ret.append(ops)
        cnt += 1
    return ret

def binsearch(nums, n, l, h):  # nums is sorted array
    if h < l:
        return False
    mid = (l + h)/ 2
    if n < nums[mid]:
        return binsearch(nums, n , l, mid - 1)
    elif n > nums[mid]:
        return binsearch(nums, n , mid + 1, h)
    else:
        return True
    

def linsearch(nums, b):  # nums is sorted array
    for j in xrange(len(nums)):
        if b > nums[j]:
            continue
        elif b < nums[j]:
            return (j, False)
        else:
            return (j, True)
    return (len(nums), False)

def list2dic(nums):
    dic = {}
    for i in nums:
        if dic.has_key(i) == False:
            dic[i] = 0
        dic[i] = dic[i] + 1
    return dic

def list2dic_bool(nums):
    return { item:True for item in nums }

def bfs(a, index, hist):
    q = [index]  # init
    while len(q) != 0:
        i = q.pop(0)
        # do operation
        if hist[i] == 1:
            continue
        hist[i] = 1

        # post
        for j in xrange(len(a[i])):
            if a[i][j] == 1 and i != j:
                q.append(j)


def iter_combination(table, n):
    return itertools.combinations(table, n)

def iter_permutations(table, n):
    return itertools.permutations(table, n)

def dist(a,b):
    x_diff = abs(b[0] - a[0])
    y_diff = abs(b[1] - a[1])
    return x_diff * x_diff + y_diff * y_diff

def boomerangs(tup):
    if dist(tup[0], tup[1]) == dist(tup[0], tup[2]):
        return True
    else:
        return False

def isPalindrome(x):
    if x < 0:
        return False
    px = 0
    tmp = x
    while tmp != 0:
        r = tmp % 10
        tmp = tmp / 10
        px = (px * 10) + r
    return px == x


def is_number(c):
    try:
        int(c)
        return True
    except:
        return False   

def is_char(c):
    if ord(c) >= 97:
        if ord(c) - 97 < 26:
            return True
    return False

def num_state(c, pre, ret):
    if is_number(c):
        pre.append(c)
        return (1,1)
    else:
        return (0, 0)

def char_state(c, pre, ret):
    if is_char(c):
        pre.append(c)
        return (1,2)
    else:
        return (0, 0)

def start_state(c, pre, ret):
    if is_number(c):
        if len(pre) != 0:
            ret.append("".join(pre))
            del pre[:]
        return (0, 1)
    elif c == "[":
        n = "".join(pre)
        ret.append(n)
        del pre[:]
        return (1, 0)
    elif is_char(c):
        return (0, 2)
    elif c == "]":
        s = "".join(pre)
        n = "1"
        while len(ret) != 0 and is_number(ret[-1]) != True:
            s = ret.pop() + s
        if is_number(ret[-1]) == True:
            n = ret.pop()
        ret.append(s * int(n))
        del pre[:]
        return (1, 0)

def ans(x):
    print x
    i = 0
    ss = ['start_state', 'num_state', 'char_state']
    csi = 0
    ret = []
    pre = [] 
    while i < len(x):
        cs = ss[csi]
        func = getattr(sys.modules[__name__], cs)
        cnt, nsi = func(x[i], pre, ret)
        csi = nsi
        i += cnt
    ret.append("".join(pre))
    print "".join(ret) 
'''
s = "ef2[c]", return "efcc".
s = "3[a]2[bc]", return "aaabcbc".
s = "3[a2[c]]", return "accaccacc".
s = "2[abc]3[cd]ef", return "abcabccdcdcdef".
'''

cases = [
        ["100[leetcode]"],
        ["ef2[c]"],
        ["3[a]2[bc]"],
        ["3[a2[c]]"],
        ["2[abc]3[cd]ef"],
]
test(cases,4)

