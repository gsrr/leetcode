def ans3(nums):
    s = 0 
    e = len(nums)
    while s < e:
        mid = (s + e) / 2
        val = nums[mid] - nums[mid - 1]
        if val < 0:
            return nums[mid]
        else:
            if nums[mid] > nums[0]:
                s = mid + 1
            else:
                e = mid
            

def ans2(nums):
    cnt = 1
    while cnt < len(nums):
        if nums[cnt] - nums[cnt - 1] < 0:
            return nums[cnt]
        cnt += 1

def ans1(nums):
    return min(nums)

class Solution(object):
    def findMin(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums) == 1:
            return nums[0]
        if nums[0] < nums[-1]:
            return nums[0]
        return ans3(nums)
