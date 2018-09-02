def ans(arr):
    inc = True
    dec = True
    for i in xrange(1, len(arr)):
        if arr[i] - arr[i - 1] < 0:
            inc = False
            break
    
    for i in xrange(1, len(arr)):
        if arr[i] - arr[i - 1] > 0:
            dec = False
    
    if inc == False and dec == False:
        return False
    return True

class Solution(object):
    def isMonotonic(self, A):
        """
        :type A: List[int]
        :rtype: bool
        """
        return ans(A)
        
