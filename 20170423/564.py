
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

def isPalindrome_str(x):
    for i in xrange(len(x)/2):
        if x[i] != x[len(x) - 1 - i]:
            return False
    return True

def conver2pa(lpa):
    cnt = 0
    if len(lpa) == 1:
        return

    lower = False
    while int(lpa[cnt]) == 0:
        lpa.pop(0)
        lower = True
    print "lower", lower
    if lower == True:
        for i in xrange(len(lpa)):
            lpa[len(lpa) - 1 - i]= "9"
    elif len(lpa) != 1:
        for i in xrange(len(lpa)/2):
            lpa[len(lpa) - 1 - i]= lpa[i]

def get_pre_pa(pa):
    lpa = list(pa)
    for i in xrange(int(round(len(lpa)/2.0)) - 1, -1, -1):
        if int(lpa[i]) != 0:
            lpa[i] = str(int(lpa[i]) - 1)
            conver2pa(lpa)
            return "".join(lpa)
        else:
            lpa[i] = "9"
            
def get_next_pa(pa):
    lpa = list(pa)
    c = 0
    for i in xrange(int(round(len(lpa)/2.0)) - 1, -1, -1):
        if int(lpa[i]) != 9:
            lpa[i] = str(int(lpa[i]) + 1)
            conver2pa(lpa)
            return "".join(lpa)
        else:
            lpa[i] = "0"
            c = 1
    if c == 1:
        lpa.insert(0, "1")
        conver2pa(lpa)
    return "".join(lpa)


def diff(p, n):
    return int(n) - int(p)

def ans(x):
    if isPalindrome_str(x):
        print True
        pre_pa = get_pre_pa(x)
        next_pa = get_next_pa(x)
        print pre_pa
        print next_pa
        if diff(pre_pa, x) <= diff(x, next_pa):
            return pre_pa
        else:
            return next_pa
    else:
        print False
        lx = list(x)
        for i in xrange(len(x) / 2):
            lx[len(x) - 1 - i] = lx[i]    
        pa = "".join(lx)
        pre_pa = ""
        next_pa = ""
        if pa > x:
            next_pa = pa
            pre_pa = get_pre_pa(pa)
        else:
            pre_pa = pa
            next_pa = get_next_pa(pa)
        print pre_pa
        print next_pa
        if diff(pre_pa, x) <= diff(x, next_pa):
            return pre_pa
        else:
            return next_pa
cases = [
        ["10"], # 9
        ["999"], # 1001
        ["88"], # 9
        ["1000"], # 9
        ["10000"], # 9
        ["100000"], # 9
        ["1223"],
        ["1221"],
]
test(cases,6)

