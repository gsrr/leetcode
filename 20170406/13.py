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

def ans(a):
    dic_r = {
        "I" : 1,
        "V" : 5,
        "IV" : 4,
        "X" : 10,
        "IX" : 9,
        "L" : 50,
        "XL" : 40,
        "C" : 100,
        "XC" : 90,
        "D" : 500,
        "CD" : 400,
        "M" : 1000,
        "CM" : 900,
    }
    ret = 0
    s = 0
    while s < len(a):
        if dic_r.has_key(a[s:s+2]):
            ret += dic_r[a[s:s+2]]
            s = s + 2
        else:
            ret += dic_r[a[s]]
            s = s + 1
    return ret

cases = [
        ["DCXXI"],
        ["DCXIX"],
]
test(cases,2)

