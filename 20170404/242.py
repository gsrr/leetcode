



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

def list2dic_cnt(nums):
    dic_nums = {}
    for c in nums:
        if dic_nums.has_key(c) == False:
            dic_nums[c] = 0
        dic_nums[c] += 1
    return dic_nums

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

def ans(a, b):
    print a, b
    if len(a) != len(b):
        return False
    dic_a = {}
    for c in a:
        if dic_a.has_key(c) == False:
            dic_a[c] = 0
        dic_a[c] += 1
    for c in b:
        if dic_a.has_key(c) == False:
            return False
        else:
            dic_a[c] -= 1
            if dic_a[c] == -1:
                return False
    return True

cases = [
        ["anagram", "nagaram"]
]
    
test(cases,1)

