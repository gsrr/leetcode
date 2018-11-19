import collections

def ans(A):
    if len(A) < 3:
        return False
    
    i = 0
    j = len(A) - 1
    while i < len(A) - 1 and A[i + 1] - A[i] > 0:
        i += 1
    
    while j > 0 and A[j - 1] - A[j] > 0:
        j -= 1
    
    if i == 0 or j == len(A) - 1:
        return False
    
    return i == j

class Solution(object):
    def validMountainArray(self, A):
        """
        :type A: List[int]
        :rtype: bool
        """
        return ans(A)
        
