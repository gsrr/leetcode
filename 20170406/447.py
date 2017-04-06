
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


def iter_combination(table, n):
    return itertools.combinations(table, n)

def iter_permutations(table, n):
    return itertools.permutations(table, n)

def dist(a,b):
    x_diff = b[0] - a[0]
    y_diff = b[1] - a[1]
    return x_diff * x_diff + y_diff * y_diff

def boomerangs(tup):
    if dist(tup[0], tup[1]) == dist(tup[0], tup[2]):
        return True

    if dist(tup[1], tup[0]) == dist(tup[1], tup[2]):
        return True

    if dist(tup[2], tup[0]) == dist(tup[2], tup[1]):
        return True
    
    return False

def ans(a):
    ret = 0
    for i in xrange(len(a)):
        dic_n = {}
        for j in xrange(len(a)):
            if i != j:
                #d = (a[j][0] - a[i][0]) **2 + (a[j][1] - a[i][1]) ** 2
                d = dist(a[i], a[j])
                if dic_n.has_key(d) == False:
                    dic_n[d] = 0
                dic_n[d] += 1
        for key, item in dic_n.items():
            if item > 1:
                ret += (item * (item - 1))
    return ret

cases = [
        [[[0,0],[1,0],[2,0]]],
]
test(cases,2)

