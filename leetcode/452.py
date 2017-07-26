

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


def is_same_range(a, b):
    if a[1] - b[0] >= 0 and b[1] - a[1] >= 0:
        return True
    if b[0] - a[0] >= 0 and a[1] - b[0] >= 0:
        return True
    return False

def update_crange(cr, a):
    x = max(cr[0], a[0])
    y = min(cr[1], a[1])
    return [x,y]

def ans(x):
    if len(x) == 0:
        return 0
    x.sort()
    lx = [x[0]]
    crange = x[0]
    for i in xrange(1, len(x)):
        if is_same_range(crange, x[i]) == True:
            crange = update_crange(crange, x[i])
        else:
            lx.append(x[i])
            crange = x[i]
    return len(lx)

cases = [
        [[[10,16], [2,8], [1,6], [7,12]]],
        [[[3,9],[7,12],[3,8],[6,8],[9,10],[2,9],[0,9],[3,9],[0,6],[2,8]]],
        [[[9,12],[1,10],[4,11],[8,12],[3,9],[6,9],[6,7]]]
]
test(cases,3)

