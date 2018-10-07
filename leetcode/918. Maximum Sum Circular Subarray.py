def ans(arr):
    all_positive = 1
    for i in xrange(len(arr)):
        if arr[i] < 0:
            all_positive = 0
            break
        
    if all_positive:
        return sum(arr)
    arr2 = arr * 2
    #print (arr2)
    gsum = arr2[0]
    tsum = arr2[0]
    path = 1
    for i in xrange(1, len(arr2)):
        if path == len(arr):
            tsum -= arr2[i - len(arr)]
            path -= 1
            j = i - len(arr) + 1
            ttsum = tsum
            tpath = path
            while j < i:
                ttsum -= arr2[j]
                tpath -= 1
                if ttsum > tsum:
                    tsum = ttsum
                    path = tpath
                j += 1
        if tsum < 0:
        #if tsum < 0:
            tsum = 0
            path = 0
        tsum += arr2[i]
        path += 1
        gsum = max(gsum, tsum)
    return gsum
        

class Solution(object):
    def maxSubarraySumCircular(self, A):
        """
        :type A: List[int]
        :rtype: int
        """
        return ans(A)
        
