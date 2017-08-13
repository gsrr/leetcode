

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

def ans(n, nines, indx):
    if n < 10:
        if n == 9:
            return 10
        else:
            return n
    b, ns = nines[indx]
    qs = 0
    r = n
    while r >= b:
        q = r / b
        r = r % b
        offset = q * ns
        r = r + offset
        qs += q
        print "b = %d, qs = %d, r = %d"%(b, qs, r)
    if qs >= 9:
        qs += 1
    qs = qs * b
    offset = ans(r, nines, indx + 1)
    print "b = %d, qs = %d, offset = %d"%(b, qs, offset)
    return qs + offset
       

class Solution(object):
    def newInteger(self, n):
        """
        :type n: int
        :rtype: int
        """
        '''
        s = 0
        ns = 1
        b = 10
        nines = []
        for i in xrange(1, 9):
            nines.append([b, ns])
            ns = ns * 9 + b
            b *= 10
        '''
        nines = [
            [10, 1], 
            [100, 19], 
            [1000, 271], 
            [10000, 3439], 
            [100000, 40951], 
            [1000000, 468559], 
            [10000000, 5217031], 
            [100000000, 56953279],
            [1000000000, 0]
        ]
        return ans(n, nines[::-1], 0)
        

cases = [
        [9],
]
test(cases,2)

