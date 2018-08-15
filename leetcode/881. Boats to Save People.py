import collections

def ans(arr, limit):
    arr.sort()
    i = 0
    j = len(arr) - 1
    cnt = 0
    while i <= j:
        val = arr[j]
        rval = limit - val
        if arr[i] <= rval:
            i += 1
        j -= 1
        cnt += 1
    return cnt
        
    

class Solution(object):
    def numRescueBoats(self, people, limit):
        """
        :type people: List[int]
        :type limit: int
        :rtype: int
        """
        return ans(people, limit)
        
