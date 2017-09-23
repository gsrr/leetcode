def ans2(nums):
    dic = {
        0 : -1,
        1 : 1
    }
    mlen = 0
    s = 0
    hist = {0 : 0}
    for i in xrange(len(nums)):
        s += dic[nums[i]]
        if hist.has_key(s):
            hist[s] = min(hist[s], i + 1)
        else:
            hist[s] = i + 1
        mlen = max(mlen, i + 1 - hist[s])
    return mlen

def ans1(nums):
    dic = {
        0 : -1,
        1 : 1
    }
    arr = [0]
    s = 0
    for i in xrange(len(nums)):
        s += dic[nums[i]]
        arr.append(s)
            
    mlen = 0
    for i in xrange(len(arr)):
        for j in xrange(i + 1, len(arr)):
            if arr[j] == arr[i]:
                mlen = max(mlen, j - i)
    return mlen
    
class Solution(object):
    def findMaxLength(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums) <= 1:
            return 0
        return ans2(nums)
