

import itertools
import json

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

import collections
import itertools
import math

def findsubsets(S,m):
        return set(itertools.combinations(S, m))

def same_occurrence_v2(q, ss):
    cnt = 0
    for s in ss:
        if s.get(q[0],0) == s.get(q[1],0):
            cnt += 1
    return cnt

def same_occurrence_v3(q, n, carr):
    n1 = carr[q[0]]
    n2 = carr[q[1]]
    n3 = n - n1 - n2
    cnt = 0
    fn1 = math.factorial(n1)
    fn2 = math.factorial(n2)
    print n1, n2, n3
    for i in xrange(0, min(n1, n2) + 1):
        if i == 0:
            cnt += (max(pow(2, n3) - 1 - 1, 0))
        else:
            nn1 = fn1 / (math.factorial(i) * math.factorial(n1 - i))
            nn2 = fn2 / (math.factorial(i) * math.factorial(n2 - i))
            cnt += (nn1 * nn2 * pow(2,n3))
    return cnt


def zero_occur(arr):
    return sum(xrange(1, len(arr) + 1))

def single_occur(arr, qn1, qn2):
    if len(qn1) == 0:
        qn = qn2
    else:
        qn = qn1
    
    cnt = 0
    pre = -1
    for i in xrange(len(qn)):
        cnt += sum(xrange(1, 1 + qn[i] - pre - 1))
        pre = qn[i]

    cnt += sum(xrange(1, 1 + len(arr) - pre - 1))
    return cnt

def same_occurrence(q, arr, carr, narr):
    cnt = 0
    qc1 = narr.get(q[0], 0)
    qc2 = narr.get(q[1], 0)
    qn1 = carr.get(q[0], [])
    qn2 = carr.get(q[1], [])
    if len(qn1) == 0 and len(qn2) == 0:
        return zero_occur(arr)
    else:
        if len(qn1) == 0 or len(qn2) == 0:
            return single_occur(arr, qn1, qn2)

    '''
    i = 0
    j = 0
    p1 = qn1[i]
    p2 = qn2[j]
    if p1 >= p2:
        cnt += sum(xrange(1, 1 + p2 - 0))
    else:
        cnt += sum(xrange(1, 1 + p1 - 0))

    while i < len(qn1) and j < len(qn2):
        p1 = qn1[i]
        p2 = qn2[j]
        if p1 <= p2:
            cnt += (p1 - 0 + 1)
            cnt += sum(xrange(1, 1 + p2 - p1 - 1))
        else:
            cnt += (p2 -0 + 1)
            cnt += sum(xrange(1, 1 + p1 - p2 - 1))
        i += 1
        j += 1
    '''
    i = len(qn1) - 1
    j = len(qn2) - 1
    p1 = qn1[i]
    p2 = qn2[j]
    cnt += sum(xrange(1, 1 + len(arr) - 1 - max(p1, p2)))
    
    cq1 = 0
    cq2 = 0
    while i > -1 and j > -1:
        p1 = qn1[i]
        p2 = qn2[j]
        if p1 >= p2:
            cnt += (len(arr) - p1)
            i -= 1
        else:
            cnt += (len(arr) - p2)
            j -= 1
        i -= 1
        j -= 1
    return cnt

def ans(x):
    n, qn = 7, 4
    arr = [1,2,1,2,7,5,6]
    qarr = [(1,2), (4,5), (2,5), (6,8)]
    #slist = find_all_sets(arr)
    carr = collections.defaultdict(list)
    narr = collections.defaultdict(list)
    for i in xrange(len(arr)):
        carr[arr[i]].append(i)
    for q in qarr:
        print same_occurrence(q, arr, carr, narr)

cases = [
        [5],
]
test(cases,2)

