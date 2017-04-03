


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

def bfs_matrix(a, hist):
    for i in xrange(len(a)):
        for j in xrange(len(a[i])):
            if a[i][j] == 0:
                continue
            if hist[i][j] == 1:
                continue
            q = [(i,j)]
            while len(q) != 0:



def ans(a):
    hist = []
    for i in xrange(len(a)):
        hist.append([])
        for j in xrange(len(a[i])):
            hist[i].append(0)
    bfs_matrix(a, hist)

cases = [
        [[[1,1,0],
            [1,1,0],
            [0,0,1]]],
]
test(cases,1)

