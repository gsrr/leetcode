def ans(arr):
    for i in xrange(1, len(arr)):
        if arr[i] < arr[i - 1]:
            return i - 1

class Solution(object):
    def peakIndexInMountainArray(self, A):
        """
        :type A: List[int]
        :rtype: int
        """
        return ans(A)    
