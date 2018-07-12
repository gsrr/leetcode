import heapq

def ans(nums):
    pq = []
    for i in xrange(len(nums)):
        tq = []
        while len(pq) != 0:
            cnt, val = heapq.heappop(pq)
            if nums[i] - val == 1:
                heapq.heappush(pq, (cnt + 1, nums[i]))
                break
                
            if nums[i] == val:
                tq.append((cnt, val))      
                
            if nums[i] - val > 1:
                if cnt < 3:
                    return False
            
        if len(pq) == 0:
            heapq.heappush(pq, (1, nums[i]))
        
        for i in xrange(len(tq)):
            heapq.heappush(pq, tq[i])
    
    while len(pq) != 0:
        cnt, val = heapq.heappop(pq)
        if cnt < 3:
            return False
    return True
    
class Solution(object):
    def isPossible(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        return ans(nums)
