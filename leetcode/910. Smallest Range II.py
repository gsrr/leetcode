def ans_time_expired(arr, k):
    if len(arr) == 1:
        return 0
    
    arr.sort()
    for i in xrange(len(arr)):
        arr[i] += k
    
    #print arr
    gmin = arr[0]
    gmax = arr[-1]
    for i in xrange(len(arr) - 1, 0, -1):
        #print i, arr
        arr[i] = arr[i] - 2 * k
        if arr[i] >= gmin:
            gmax = max(arr[i - 1], arr[-1])
        else:
            tmax = max(arr[i - 1], arr[-1])
            tmin = arr[i]
            if tmax - tmin < gmax - gmin:
                gmax = tmax
                gmin = tmin
    return gmax - gmin

def ans(arr, k):
    if len(arr) == 1:
        return 0
    
    arr.sort()
    for i in xrange(len(arr)):
        arr[i] += k
    
    #print arr
    gmin = arr[0]
    gmax = arr[-1]
    for i in xrange(len(arr) - 1, 0, -1):
        #print i, arr
        arr[i] = arr[i] - 2 * k
        if arr[i] >= gmin:
            gmax = max(arr[i - 1], arr[-1])
        else:
            tmax = max(arr[i - 1], arr[-1])
            tmin = arr[i]
            if tmax - tmin < gmax - gmin:
                gmax = tmax
                gmin = tmin
    return gmax - gmin
                
                
        
        
class Solution(object):
    def smallestRangeII(self, A, K):
        """
        :type A: List[int]
        :type K: int
        :rtype: int
        """
        return ans(A, K)
        
