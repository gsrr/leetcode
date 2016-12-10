# 58ms , 61.06%
class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        sorted_nums = sorted(nums)
        ret = []
        for i in xrange(len(sorted_nums)):
            fir_num = sorted_nums[i]
            for j in xrange(i, len(sorted_nums)):
                sec_num = sorted_nums[j]
                if i == j:
                    continue
                if fir_num + sec_num  > target:
                    break
                else:
                    if sorted_nums[i] + sorted_nums[j] == target:
                        fir = nums.index(sorted_nums[i])
                        nums[fir] = sorted_nums[i] + 1
                        sec = nums.index(sorted_nums[j])
                        return [fir, sec]