import heapq
import bisect

def ans7(A, K):
    l, r, N = 0, 1, len(A)
    while True:
        m = (l + r) / 2.0
        print m
        border = [bisect.bisect(A, A[i] / m) for i in range(N)]
        cur = sum(N - i for i in border)
        if cur > K:
            r = m
        elif cur < K:
            l = m
        else:
            return max([(A[i], A[j]) for i, j in enumerate(border) if j < N], key=lambda x: x[0] / float(x[1]))

def ans6(A, K):
    """
    :type A: List[int]
    :type K: int
    :rtype: List[int]
    """
    n = len(A)
    data = [0] * n
    heap = [(A[data[i]]/(A[i] * 1.0), i) for i in xrange(1, n)]
    heapq.heapify(heap)
    for _ in xrange(1, K):
        v, i = heapq.heappop(heap)
        data[i] += 1
        heapq.heappush(heap, (A[data[i]]/(A[i] * 1.0), i))
    _, i = heapq.heappop(heap)
    return [A[data[i]], A[i]]

def ans5(A, K):
    n = len(A)
    data = [0] * n
    '''
    heap = [(A[data[i]]/float(A[i]), i) for i in range(1, n)]
    heapq.heapify(heap)
    '''
    heap = []
    for i in range(1, n):
        heapq.heappush(heap, (A[data[i]]/float(A[i]), i))
    for _ in xrange(1, K):
        v, i = heapq.heappop(heap)
        data[i] += 1
        heapq.heappush(heap, (A[data[i]]/float(A[i]), i))
    _, i = heapq.heappop(heap)
    return [A[data[i]], A[i]]
        
def ans4(arr, k):
    '''
    priority queue
    '''
    n = len(arr)
    #q = [(arr[0]/float(arr[n - 1]), 0, n - 1)]
    q = []
    for i in xrange(1, n):
        heapq.heappush(q, (arr[0]/float(arr[i]), 0, i))
    x, y = 0, n - 1
    while len(q) != 0:
        val, x, y = heapq.heappop(q)
        #print val, x, y
        k -= 1
        if k == 0:
            break
        if x + 1 < y:
            heapq.heappush(q, (arr[x + 1]/float(arr[y]), x + 1, y))
    return [arr[x], arr[y]]
    
def ans3(arr, k):
    '''
    bfs + priority queue
    '''
    hist = {}
    n = len(arr)
    q = [(arr[0]/float(arr[n - 1]), 0, n - 1)]
    x, y = 0, n - 1
    while len(q) != 0:
        val, x, y = heapq.heappop(q)
        #print val, x, y
        hist[(x, y)] = True
        k -= 1
        if k == 0:
            break
        for nx, ny in [(x + 1, y), (x, y - 1)]:
            if nx >= ny:
                continue
            if hist.has_key((nx, ny)):
                continue
            heapq.heappush(q, (arr[nx]/float(arr[ny]), nx, ny))
    return [arr[x], arr[y]]
    
def ans2(arr, k):
    '''
    Result : Wrong Answer
    '''
    tk = k
    i = 0
    while i < len(arr):
        if tk - (i + 1) > 0:
            tk -= (i + 1)
            i += 1
        else:
            break
    
    interval = len(arr) - 1 - i
    print interval
    ret = []
    for j in xrange(len(arr)):
        s = j
        e = j + interval
        if e >= len(arr):
            break
        ret.append([arr[s]/float(arr[e]) , [arr[s], arr[e]]])
    
    ret.sort()
    return ret[tk - 1][1]
    
def ans1(arr, k):
    '''
    Result : Time Exceed
    '''
    farr = []
    for i in xrange(len(arr)):
        for j in xrange(i + 1, len(arr)):
            farr.append([arr[i]/float(arr[j]), arr[i], arr[j]])
    farr.sort()
    print farr
    return farr[k - 1][1]

class Solution(object):
    def kthSmallestPrimeFraction(self, A, K):
        """
        :type A: List[int]
        :type K: int
        :rtype: List[int]
        """
        return ans7(A, K)
        
