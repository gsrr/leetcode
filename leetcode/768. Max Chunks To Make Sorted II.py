class Solution(object):
    def maxChunksToSorted(self, arr):
        """
        :type arr: List[int]
        :rtype: int
        """
        maxarr = [0] * len(arr)
        maxarr[0] = arr[0]
        for i in xrange(1, len(arr)):
            maxarr[i] = maxarr[i - 1]
            if arr[i] > maxarr[i - 1]:
                maxarr[i] = arr[i]
        print maxarr
        
        cnt = 1
        minval = arr[-1]
        for i in xrange(len(arr) - 2, -1, -1):
            if maxarr[i] > minval:
                if arr[i] < minval:
                    minval = arr[i]
            else:
                cnt += 1
                minval = arr[i]
        return cnt
