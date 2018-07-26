def compute(arr, mid, H):
    #print arr, mid, H
    if mid == 0 and len(arr) != 0:
        return False
    cnt = 0
    for i in xrange(len(arr)):
        if arr[i] % mid == 0:
            cnt += arr[i] // mid
        else:
            cnt += (arr[i] // mid + 1)
    return cnt <= H

def ans(arr, H):
    arr.sort()
    low = 0
    high = arr[-1]
    
    while low < high:
        mid = (low + high) // 2
        if compute(arr, mid, H) == True:
            high = mid
        else:
            low = mid + 1
    return (low + high) // 2

class Solution(object):
    def minEatingSpeed(self, piles, H):
        """
        :type piles: List[int]
        :type H: int
        :rtype: int
        """
        return ans(piles, H)
