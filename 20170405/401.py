

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
            return False
        else:
            return True
    return False

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

import itertools

def convert2time(ts):
    dic_t = {
        1 : ("hr", 1),
        2 : ("hr", 2),
        3 : ("hr", 4),
        4 : ("hr", 8),
        5 : ("m", 1),
        6 : ("m", 2),
        7 : ("m", 4),
        8 : ("m", 8),
        9 : ("m", 16),
        10 : ("m", 32),
    }
    hr = 0
    m = 0
    for t in ts:
        tf = dic_t[t]
        if tf[0] == "hr":
            hr += tf[1]
        else:
            m += tf[1]
    return (hr, m)

def iter_combination(table, n):
    return itertools.combinations(table, n)

def ans(a):
    t = [1,2,3,4,5,6,7,8,9,10]
    ret = []
    iter_comb = iter_combination(t, a)
    for i in iter_comb:
        hr, m = convert2time(i)
        if hr < 12 and m < 60:
            ret.append("%d:%02d"%(hr,m))
    return ret

cases = [
        [0],
        [1],
]
test(cases,2)

