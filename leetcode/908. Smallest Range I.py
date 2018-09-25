def ans(arr, k):
    if len(arr) == 1:
        return 0

    min_val = min(arr)
    max_val = max(arr)
    if max_val - min_val <= 2 * k:
        return 0

    return (max_val - k) - (min_val + k)

class Solution(object):
    def smallestRangeI(self, A, K):
        """
        :type A: List[int]
        :type K: int
        :rtype: int
        """
        return ans(A, K)
        
