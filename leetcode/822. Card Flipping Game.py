import collections

def ans(arr, brr):
    '''
    Time Complexity : n + n + n --> O(n)
    Space Complexity : O(n)
    '''
    carr = collections.Counter(arr)
    cbrr = collections.Counter(brr)
    for i in xrange(len(arr)):
        if arr[i] == brr[i]:
            if carr.has_key(arr[i]):
                del carr[arr[i]]
                del cbrr[arr[i]]
    if len(carr.keys()) == 0 and len(cbrr.keys()) == 0:
        return 0
    if len(carr.keys()) == 0:
        return min(cbrr.keys())
    if len(cbrr.keys()) == 0:
        return min(carr.keys())
    return min(min(carr.keys()), min(cbrr.keys()))
    
class Solution(object):
    def flipgame(self, fronts, backs):
        """
        :type fronts: List[int]
        :type backs: List[int]
        :rtype: int
        """
        return ans(fronts, backs)
        
