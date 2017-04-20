import itertools
import math

def test(cases, cn = 1):
    cnt = 0
    while cnt < cn and cnt < len(cases):
        print "case:", cnt + 1 
        ret = ans(*cases[cnt])
        print "\n\tret:", ret
        print "-" * 10
        cnt += 1

def is_prime_v2(n, primes):
    for p in primes:
        if p * p > n:
            return True
        if n % p == 0:
            return False
    return True
    
def is_prime(n):
    if n == 1:
        return False
    cnt = 2
    while cnt * cnt <= n:
        if n % cnt == 0:
            return False
        cnt += 1
    return True

def find_primes(n):
    ret = [2]
    for i in xrange(3, n):
        if is_prime(i, ret):
            ret.append(i)
    return ret

def prime_factor(n):
    #primes = find_primes(int(math.sqrt(n)))
    ret = []
    cnt = 1
    while cnt * cnt <= n:
        if n % cnt == 0:
            if cnt == 1 or is_prime(cnt): 
                ret.append(cnt)
                ops = n / cnt
                if is_prime(ops) and ops != cnt:
                    ret.append(ops)
        cnt += 1
    return ret

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

def ans(a):
    primes = prime_factor(a)
    print a, primes
    for p in primes[1:]:
        if p not in [2, 3, 5]:
            return False
    return True

cases = [
        [50],
        [1355394467],
        [2073365937],
]
test(cases,20)

