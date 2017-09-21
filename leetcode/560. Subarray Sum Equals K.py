import collections

def ans1(nums, k):
    dic = collections.defaultdict(int)
    cnt = 0
    s = 0
    for i in xrange(len(nums)):
        dic[s] += 1
        s += nums[i]
        key = s - k
        cnt += dic.get(key, 0)
    return cnt
    
class Solution(object):
    def subarraySum(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        return ans1(nums, k)   
        
            
            
                
                
