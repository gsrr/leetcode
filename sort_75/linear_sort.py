class Solution(object):
    def linear_sort(self, nums):
        for i in xrange(len(nums)):
            for j in xrange(i, 0, -1):
                if nums[j] < nums[j-1]:
                    temp = nums[j]
                    nums[j] = nums[j-1]
                    nums[j-1] = temp
                    
    def quick_sort_v1(self, nums): # return
        if len(nums) <= 1:
            return nums
            
        pivot = nums[0]
        small_nums = []
        big_nums = []
        for i in range(1, len(nums)):
            if nums[i] < pivot:
                small_nums.append(nums[i])
            else:
                big_nums.append(nums[i])
        return self.quick_sort(small_nums) + self.quick_sort(big_nums)
        
    def quick_sort(self, nums, s, e):
        if s < e:
            pivot = nums[s]
            i = s + 1
            j = e 
            while True:
                while i <= e:
                    if nums[i] <= pivot:
                        i += 1
                    else:
                        break
                    
                while j >= s :
                    if nums[j] > pivot:
                        j -= 1
                    else:
                        break
                    
                if i < j:
                    nums[i], nums[j] = nums[j], nums[i]
                else:
                    nums[s], nums[i-1] = nums[i-1], nums[s]
                    break
            self.quick_sort(nums, s, i-2)
            self.quick_sort(nums, i, e)
            
    def sortColors(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        #return self.linear_sort(nums)
        self.quick_sort(nums, 0, len(nums) - 1)

        
s = Solution()
nums = [3,3,1,0]
s.sortColors(nums)
print nums
nums = [1,0]
s.sortColors(nums)
print nums
nums = [0,0,1,0,1,1]
s.sortColors(nums)
print nums


