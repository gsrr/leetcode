


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
        dic[i] + 1
    return dic

def list2dic_bool(nums):
    return { item:True for item in nums }

def issub(a, b):
    s = 0
    find = False
    for i in xrange(len(a)):
        find = False
        for j in xrange(s, len(b)):
            if a[i] == b[j]:
                s = j + 1
                find = True
                break
    return find

def ans(a, b):
    print a, b
    if len(a) > len(b):
        if issub(b, a):
            return len(a)
        else:
            return len(a)
    elif len(a) < len(b):
        if issub(a, b):
            return len(b)
        else:
            return len(b)
    else:
        if a != b:
            return len(a)
        else:
            return -1
cases = [
    ["aba", "cdc"],
    ["aefawfawfawfaw","aefawfeawfwafwaef"],
]
test(cases,10)

