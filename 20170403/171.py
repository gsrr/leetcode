


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

def ans(a):
    letters = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    dic_letters = {c: i+1 for i,c in enumerate(letters)}
    ret = 0
    for cnt, c in enumerate(a[::-1]):
        ret += pow(26, cnt) * dic_letters[c]
    return ret


cases = [
    ["AB"],
]
test(cases,1)

