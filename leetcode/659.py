class Solution(object):
    def isPossible(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        ret = []
        hist = [0] * len(nums)
        for i in xrange(len(nums)):
            if hist[i] == 1:
                continue
            else:
                hist[i] = 1
                tmp = [nums[i]]
                val = nums[i]
                for j in xrange(i + 1, len(nums)):
                    if hist[j] == 1:
                        continue
                        
                    if len(tmp) == 3:
                        break
                        
                    if nums[j] - val == 0:
                        continue
                    elif nums[j] - val == 1:
                        tmp.append(nums[j])
                        val = nums[j]
                        hist[j] = 1
                    else:
                        break
                ret.append(list(tmp))
        
        i = len(ret) - 1
        hist = [0] * len(ret)
        print ret
        while i > -1:
            if len(ret[i]) < 3:
                comb_ret = False
                min_val = ret[i][0]
                for j in xrange(i, -1, -1):
                    if hist[j] == 0:
                        if min_val - ret[j][-1] == 1:
                            hist[j] = 1
                            hist[i] = 1
                            comb_ret = True
                            break
                if comb_ret == False:
                    print ret[i]
                    return False
            i -= 1
        return True
