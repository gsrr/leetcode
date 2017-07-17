

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

def compare_pre(nums, s, i, k, tk):
    lens = k + abs(tk)
    os = s/float(lens)
    rs = s
    ts = s
    rtk = tk
    while tk < 0:
        ns = ts - nums[i - lens + 1]
        a1 = ns/float(lens - 1)
        a2 = ts/float(lens)
        ts = ns
        tk += 1
        lens -= 1
        '''
        if a1 > a2:
            s = ns
            tk += 1
        '''
        if a1 > os:
            rs = ns
            rtk = tk
            break
    return (rs, rtk)

def ans_nn(nums, k):
    max_val = -0x80000000
    tk = k
    s = 0
    for i in xrange(len(nums)):
        s += nums[i]
        tk -= 1
        if tk < 0:
            if nums[i] > 0:
                ts, rtk = compare_pre(nums, s, i, k, tk)
                s = ts
                tk = rtk
        if tk <= 0:
            ts = (s / float(k + abs(tk)))
            if ts > max_val:
                max_val = ts
    return max_val


def ans_nn2(nums, k):
    max_val = -0x80000000
    for i in xrange(len(nums) - k + 1):
        sval = 0
        cnt = 0
        for j in xrange(i, len(nums)):
            sval += nums[j]
            cnt += 1
            if cnt < k:
                continue
            tval = sval / float(cnt)
            max_val = max(max_val, tval)

    return max_val 

def ans(nums, k):
    print nums, k
    s = [0] * (len(nums) + 1)
    max_val = -0x80000000
    # sum array
    for i in xrange(len(nums)):
        s[i + 1] = s[i] + nums[i]

    for i in xrange(len(nums) - k + 1):
        for j in xrange(k, len(nums) - i + 1):
            tval = (s[i + j] - s[i]) / float(j)
            max_val = max(max_val, tval)
    return max_val

cases = [
        #[[-6662,5432,-8558,-8935,8731,-3083,4115,9931,-4006,-3284,-3024,1714,-2825,-2374,-2750,-959,6516,9356,8040,-2169,-9490,-3068,6299,7823,-9767,5751,-7897,6680,-1293,-3486,-6785,6337,-9158,-4183,6240,-2846,-2588,-5458,-9576,-1501,-908,-5477,7596,-8863,-4088,7922,8231,-4928,7636,-3994,-243,-1327,8425,-3468,-4218,-364,4257,5690,1035,6217,8880,4127,-6299,-1831,2854,-4498,-6983,-677,2216,-1938,3348,4099,3591,9076,942,4571,-4200,7271,-6920,-1886,662,7844,3658,-6562,-2106,-296,-3280,8909,-8352,-9413,3513,1352,-8825],90],
[[1,12,-5,-6,50,3],4],
[[7,4,5,8,8,3,9,8,7,6],7]
]
test(cases,3)

