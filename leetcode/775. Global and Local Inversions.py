'''
當local count被調換後,
後面若在存在local count, 就代表global count與local count不相同.
'''


class Solution(object):
    def isIdealPermutation(self, A):
        """
        :type A: List[int]
        :rtype: bool
        """
        i = 0
        while i < len(A) - 1:
            if A[i] > A[i + 1]:
                A[i], A[i + 1] = A[i + 1], A[i]
                i += 2
            else:
                i += 1
        
        i = 0
        while i < len(A) - 1:
            if A[i] > A[i + 1]:
                return False
            i += 1
        return True
