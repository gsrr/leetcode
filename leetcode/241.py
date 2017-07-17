

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

def re_ex():
    lx = "1*2-1"
    lx = re.split("\*|\+|\-", x)
    print lx
    lx = re.split("[0-9]+", x)
    print lx

import re

def compute(lx, ret):
    if len(lx) == 1:
        ret[lx[0]] = True
    for i in xrange(len(lx)):
        if lx[i] in ["*", "+", "-"]:
            nlx = []
            nlx.extend(lx[0:i-1])
            val = "(%s)"%(lx[i - 1] + lx[i] + lx[i + 1])
            nlx.append(val)
            nlx.extend(lx[i + 2:])
            compute(nlx, ret)

    
def ans_basic(x):
    lx = []
    val = 0
    for i in xrange(len(x)):
        if x[i] in ["*", "+", "-"]:
            lx.append(str(val))
            lx.append(x[i])
            val = 0
        else:
            val = val * 10 + int(x[i])
    lx.append(str(val))
    if len(lx) == 1:
        return [int(lx[0])]
    dic = {}
    compute(lx, dic)
    ret = []
    for expr in dic.keys():
        print expr
        q = []
        val = 0
        for i in xrange(len(expr)):
            if expr[i] == ")":
                op = q.pop()
                a1 = q.pop()
                a2 = val
                if op == "*":
                    val = a1 * a2
                if op == "+":
                    val = a1 + a2
                if op == "-":
                    val = a1 - a2
            elif expr[i] == "(":
                continue
            elif expr[i] in ["*", "+", "-"]:
                q.append(val)
                q.append(expr[i])
                val = 0
            else:
                val = val * 10 + int(expr[i])
        ret.append(val)
    return ret

def ans_eval(x):
    lx = []
    val = 0
    for i in xrange(len(x)):
        if x[i] in ["*", "+", "-"]:
            lx.append(str(val))
            lx.append(x[i])
            val = 0
        else:
            val = val * 10 + int(x[i])
    lx.append(str(val))
    if len(lx) == 1:
        return [int(lx[0])]
    dic = {}
    compute(lx, dic)
    ret = []
    for expr in dic.keys():
        ret.append(eval(expr))
    return ret

def ans_resplit(x):
    '''
    lx = re.split(r'(\D)', x) # \D --> match non-digit character
    print re.split(r'(\*|\+|\-)', x) # as same as \D
    '''
    lx = re.split(r'(\*|\+|\-)', x)
    val = 0
    if len(lx) == 1:
        return [int(lx[0])]
    dic = {}
    compute(lx, dic)
    ret = []
    for expr in dic.keys():
        ret.append(eval(expr))
    return ret

def ans_divide(x):
    if x.isdigit():
        return [int(x)]
    
    ret = []
    for i in xrange(len(x)):
        if x[i] in "*+-":
            left = ans_divide(x[:i])
            right = ans_divide(x[i + 1:])
            for l in left:
                for r in right:
                    ret.append(eval(str(l) + x[i] + str(r)))
    return ret

def ans(x):
    print x
    return ans_divide(x)

cases = [
        ["0"],
        ["11"],
        ["2-1-1"],
        ["2*3-4*5"]
]
test(cases,4)

