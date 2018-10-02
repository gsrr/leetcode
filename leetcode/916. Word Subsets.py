import collections

def ans(arr, brr):
    bdic = collections.defaultdict(int)
    for i in xrange(len(brr)):
        crr = collections.Counter(brr[i])
        for key in crr.keys():
            if crr[key] > bdic[key]:
                bdic[key] = crr[key]
    #print bdic
    
    ret = []
    for i in xrange(len(arr)):
        crr = collections.Counter(arr[i])
        find = True
        for key in bdic.keys():
            if crr.has_key(key) and crr[key] >= bdic[key]:
                pass
            else:
                find = False
                break
        if find:
            ret.append(arr[i])
    return ret

class Solution(object):
    def wordSubsets(self, A, B):
        """
        :type A: List[str]
        :type B: List[str]
        :rtype: List[str]
        """
        return ans(A, B)
