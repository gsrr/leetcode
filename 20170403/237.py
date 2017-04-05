#Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

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

def list_insert(lnums, n):
    tmp = lnums
    while tmp.next != None:
        tmp = tmp.next
    tmp.next = ListNode(n)

def arr2list(nums):
    lnums = None
    for n in nums:
        if lnums == None:
            lnums = ListNode(n)
        else:
            list_insert(lnums, n)
    return lnums

def list_delete(lnums, val):
    pre = None
    tmp = lnums
    while tmp.next != None:
        if tmp.val == val:
            if pre == None:
                pre = tmp.next
                tmp.next = None
                lnums = pre
            else:
                pre = tmp.next
                tmp.next = None
            break
        else:
            pre = tmp
            tmp = tmp.next

def ans(a):
    la = arr2list(a)
    list_delete(la, 0)
    while la != None:
        print la.val
        la = la.next
    return la

cases = [
        [[1,2,3,4]],
        [[0, 1]],
]
test(cases,2)

