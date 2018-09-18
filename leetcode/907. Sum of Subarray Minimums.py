import math

def descending(arr):
    for i in xrange(1, len(arr)):
        if arr[i] - arr[i - 1] > 0:
            return False
    return True

def ascending(arr):
    for i in xrange(1, len(arr)):
        if arr[i] - arr[i - 1] < 0:
            return False
    return True

def ans(arr):
    if descending(arr):
        #print "descending"
        sval = 0
        for i in xrange(len(arr)):
            sval += (arr[i] * (i + 1))
        return sval
    
    if ascending(arr):
        #print "ascending"
        sval = 0
        for i in xrange(len(arr)):
            sval += (arr[::-1][i] * (i + 1))
        return sval
    
    if len(arr) == 0:
        return 0
    if len(arr) == 1:
        return arr[0]
    
    index = 0
    minval = arr[0]
    for i in xrange(1, len(arr)):
        if arr[i] < minval:
            index = i
            minval = arr[i]
    #print (index + 1), minval, len(arr) - index
    #print arr[0:index]
    #print arr[index + 1:]
    return (index + 1) * (minval * (len(arr) - index)) + ans(arr[0:index]) + ans(arr[index + 1:])

def constructSTUtil(arr, ss, se, st, si):
    if ss == se:
        st[si] = (arr[ss], ss)
        return st[si]
    
    mid = (ss + se) / 2
    lval = constructSTUtil(arr, ss, mid, st, si * 2 + 1)
    rval = constructSTUtil(arr, mid + 1, se, st, si * 2 + 2)
    if lval[0] < rval[0]:
        st[si] = lval
    else:
        st[si] = rval
    return st[si]

def constructST(arr):
    height = int(math.ceil(math.log(len(arr),2)))
    st = [(0x7fffffff, 0)] * (pow(2, height + 1) - 1)
    constructSTUtil(arr, 0, len(arr) - 1, st, 0)
    return st

def getMinUtil(st, ss, se, qs, qe, si):
    if (qs > se or qe < ss):
        return (0x7fffffff, 0)
    
    if (qs <= ss and qe >= se):
        return st[si]
    
    mid = (ss + se) / 2
    lval = getMinUtil(st, ss, mid, qs, qe, 2 * si + 1)
    rval = getMinUtil(st, mid + 1, se, qs, qe, 2 * si + 2)
    if lval[0] < rval[0]:
        return lval
    else:
        return rval
    
def getMin(st, n, q):
    return getMinUtil(st, 0, n - 1, q[0], q[1], 0)
    
def ans2(arr):
    '''
    Method : Min Segment Tree (Recursive, Iterative)
    Result : Time Expired
    
    '''
    
    def get_cnt(arr, start, end):
        if start >= end:
            return 0
        if end - start == 1:
            #print arr[start]
            return arr[start]
    
        minval, index = getMin(st, len(arr), (start, end - 1))
        #print "(start = %d, end = %d, minval = %d, index = %d)"%(start, end, minval, index)
        return (index + 1 - start) * (minval * (end - index)) + get_cnt(arr, start, index) + get_cnt(arr, index + 1, end)
    
    def get_cnt_loop(arr, start, end):
        q = [(start, end)]
        cnt = 0
        while len(q) != 0:
            s, e = q.pop()
            if s >= e:
                continue
            if e - s == 1:
                cnt += arr[s]
                continue
            
            minval, index = getMin(st, len(arr), (s, e - 1))
            cnt += (index + 1 - s) * (minval * (e - index))
            q.append((s, index))
            q.append((index + 1, e))
        return cnt
    
    st = constructST(arr)
    #print st
    return get_cnt_loop(arr, 0, len(arr))

def ans3(arr):
    larr = []
    st = []
    for i in xrange(len(arr)):
        cnt = 1
        while len(st) != 0:
            val, pcnt = st.pop()
            if val >= arr[i]:
                cnt += pcnt
            else:
                st.append((val, pcnt))
                break
        st.append((arr[i], cnt))
        larr.append(cnt)
    #print larr
    
    rarr = []
    st = []
    for i in xrange(len(arr) - 1, -1, -1):
        cnt = 1
        while len(st) != 0:
            val, pcnt = st.pop()
            if val > arr[i]:
                cnt += pcnt
            else:
                st.append((val, pcnt))
                break
        st.append((arr[i], cnt))
        rarr.append(cnt)
    rarr = rarr[::-1]
    #print rarr
    
    cnt = 0
    for i in xrange(len(arr)):
        cnt += (arr[i] * larr[i] * rarr[i])
    return cnt

class Solution(object):
    def sumSubarrayMins(self, A):
        """
        :type A: List[int]
        :rtype: int
        """
        #cnt = ans(A)
        cnt = ans3(A)
        return cnt % (10**9 + 7)
