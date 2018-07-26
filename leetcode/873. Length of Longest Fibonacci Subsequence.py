import collections

def compute(carr, v1, v2):
    cnt = 2
    a = v1
    b = v2
    c = a + b
    while carr.has_key(c):
        a = b
        b = c
        c = a + b
        cnt += 1
    
    if cnt == 2:
        return 0
    return cnt

def ans(arr):
    carr = collections.Counter(arr)
    gcnt = 0
    for i in xrange(len(arr)):
        for j in xrange(i + 1, len(arr)):
            tcnt = compute(carr, arr[i], arr[j])
            if tcnt > gcnt:
                gcnt = tcnt
    return gcnt

class Solution(object):
    def lenLongestFibSubseq(self, A):
        """
        :type A: List[int]
        :rtype: int
        """
        return ans(A)
        
