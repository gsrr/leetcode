def ans(arr):
    larr = [0] * len(arr)
    rarr = [0] * len(arr)
    larr[0] = arr[0]
    for i in xrange(1, len(arr)):
        larr[i] = max(larr[i - 1], arr[i])
    
    rarr[-1] = arr[-1]
    for i in xrange(len(arr) - 2, -1, -1):
        rarr[i] = min(rarr[i + 1], arr[i])
        
    #print larr
    #print rarr
    for i in xrange(len(arr) - 1):
        if larr[i] <= rarr[i + 1]:
            return i + 1
    return 0
    

class Solution(object):
    def partitionDisjoint(self, A):
        """
        :type A: List[int]
        :rtype: int
        """
        return ans(A)
        
