import time

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

def findMaxMin(nums):
    min_val, max_val, imin, imax = compare(nums[0], nums[1])
    for i in xrange(2, len(nums)):
        if nums[i] > max_val:
            max_val = nums[i]
            imax = i
        elif nums[i] < min_val:
            min_val = nums[i]
    return (min_val, max_val, imin, imax)

def compare(n1, n2):
    if n1 > n2:
        return (n2, n1, 1, 0)
    else:
        return (n1, n2, 0, 1)

def ans(a):
    if len(a) == 0:
        return 0
    elif len(a) == 1:
        return 0
    elif len(a) == 2:
        return abs(a[0] - a[1])

    ret = 0
    min_val, max_val, imin, imax = findMaxMin(a)
    for i in a:
        ret += (i - min_val)
    return ret

cases = [
    [[83,86,77,15,93,35,86,92,49,21]]
]
test(cases,1)

