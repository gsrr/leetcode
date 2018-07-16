def ans(tp):
    arr = []
    for i in xrange(len(tp)):
        hr, mi = tp[i].split(":")
        arr.append(int(hr) * 60 + int(mi))
    arr.sort()
    arr.append(arr[0] + 60 * 24)
    gmin = 0x7fffffff
    for i in xrange(1, len(arr)):
        gmin = min(arr[i] - arr[i - 1], gmin)
    return gmin

class Solution(object):
    def findMinDifference(self, timePoints):
        """
        :type timePoints: List[str]
        :rtype: int
        """
        return ans(timePoints)
        
