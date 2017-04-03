

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

def checkBuy(a, b):
    if b > a:
        return True
    else:
        return False

def checkSell(a, b):
    if b > a :
        return False
    else:
        return True

def ans(a):
    profit = 0
    buy_money = 0
    hand = False # Buy or Sell
    for i in xrange(len(a) - 1):
        if hand == False:
            ret = checkBuy(a[i], a[i + 1])
            if ret == True:
                hand = True
                buy_money = a[i]      
        else:
            ret = checkSell(a[i], a[i + 1])
            if ret == True:
                hand = False
                profit += a[i] - buy_money
    if hand == True:
        profit += a[len(a) - 1] - buy_money
    return profit

cases = [
    [[1,2,3,4,5,6,5,7,8]],
]
test(cases,1)

