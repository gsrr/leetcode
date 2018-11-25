def ans(arr):
    arr.sort()
    #print arr
    cnt = 0
    for i in xrange(1, len(arr)):
        if arr[i] <= arr[i - 1]:
            cnt += (arr[i - 1] + 1 - arr[i])
            arr[i] = arr[i - 1] + 1
            
    return cnt

class Solution(object):
    def minIncrementForUnique(self, A):
        """
        :type A: List[int]
        :rtype: int
        """
        return ans(A)
