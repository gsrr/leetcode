
from collections import deque


def ans3(a, k):
    n = len(a)
    s = [0]*(n+1)
    for i in range(n): s[i+1]=s[i]+a[i]
    dq=deque()
    res=n+1

    for i,v in enumerate(s):
        while dq and s[dq[0]]<=v-k: res=min(res, i-dq.popleft())
        while dq and v<=s[dq[-1]]: dq.pop()
        dq.append(i)
        
    return res if res!=n+1 else -1

def ans2(a, k):
    n = len(a)
    s = [0]*(n+1)
    for i in range(n): s[i+1]=s[i]+a[i]
    dq=deque()
    res=n+1

    for i,v in enumerate(s):
        for j in range(len(dq)):
            if s[dq[j]]>v-k: break
            res=min(res, i-dq[j])
        while dq and v<=s[dq[-1]]: dq.pop()
        dq.append(i)

    return res if res!=n+1 else -1


def ans(arr, k):
    gmin = 0x7fffffff
    tsum = 0
    st = []
    i = 0
    j = 0
    while j < len(arr):
        tsum += arr[j]
        if arr[j] < 0:
            st.append([tsum, j])
        j += 1
        #print tsum, i, j, st
        
        
        
        if tsum <= 0:
            tsum = 0
            i = j
         
        while tsum >= k:
            #print "big thank k:", tsum, i, j, st
            if j - i < gmin:
                gmin = j - i
            tsum -= arr[i]
            movei = False
            for si in xrange(len(st) - 1, -1, -1):
                ni = st[si][1]
                if ni <= i:
                    break
                st[si][0] -= arr[i]
                
                if st[si][0] <= 0:
                    i = (ni + 1)
                    #j = i
                    #tsum = 0
                    tsum -= st[si][0]
                    movei = True
                    for sj in xrange(si + 1, len(st)):
                        st[sj][0] -= st[si][0]
                    break
            if movei == False:
                i += 1
    if gmin == 0x7fffffff:
        gmin = -1
    return gmin
            

class Solution(object):
    def shortestSubarray(self, A, K):
        """
        :type A: List[int]
        :type K: int
        :rtype: int
        """
        return ans3(A, K)
        
