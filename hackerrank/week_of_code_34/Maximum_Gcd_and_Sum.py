

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

from fractions import gcd
import collections

def is_prime(n):
    i = 2
    while i * i <= n:
        if n % i == 0:
            return False
        i += 1
    return True

def ans_nn(aa, bb):
    # 1. duplicate items
    # 2. prime number
    dica = collections.Counter(aa)
    dicb = collections.Counter(bb)
    a = dica.keys()
    b = dicb.keys()
    gval = 0
    ca = 0
    cb = 0
    for kb in b:
        if is_prime(kb):
            if dica.has_key(kb) == None:
                tval = 1

    '''
                    
    a.sort(reverse=True)
    b.sort(reverse=True)
    print a, b
    
    for i in xrange(len(a)):
        if a[i] <= gval:
            break
        #is_p = is_prime(a[i])
        for j in xrange(len(b)):
            if b[j] <= gval or a[i] <= gval:
                break
            print a[i], b[j], gval
            tval = gcd(a[i], b[j])
            if tval > gval:
                gval = tval
                ca, cb = a[i], b[j]
    '''
    return ca + cb

def ans(a, b):
    a.sort(reverse = True)
    b.sort(reverse = True)
    dic_a = {}
    for i in xrange(len(a)):
        if dic_a.get(a[i], 0) != 0:
            continue
        c = 1
        while c * c <= a[i]:
            if a[i] % c == 0:
                fv = c
                sv = a[i] / c
                dic_a[fv] = a[i]
                dic_a[sv] = a[i]
            c += 1
    dic_b = {}
    for i in xrange(len(b)):
        if dic_b.get(b[i], 0) != 0:
            continue
        c = 1
        while c * c <= b[i]:
            if b[i] % c == 0:
                fv = c
                sv = b[i] / c
                dic_b[fv] = b[i]
                dic_b[sv] = b[i]
            c += 1
    print dic_a
    print dic_b
    bkey = dic_b.keys()
    bkey.sort()
    for k in bkey:
        if dic_a.has_key(k):
            return dic_b[k] + dic_a[k]
cases = [
        [[17,11,7,5,16], [3,101,29,41,43]],
        [[1], [5,2,12,8,3]],
]
test(cases,2)

