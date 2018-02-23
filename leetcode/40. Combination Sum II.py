import itertools

def ans1(arr, target):
    '''
    Result : Time Exceed
    '''
    arr.sort()
    ret = {}
    for i in xrange(1, len(arr) + 1):
        it = itertools.combinations(arr, i)
        for line in it:
            if sum(line) == target:
                ret[line] = True
    return [ list(x) for x in ret.keys()]

def findcomb(arr, start, target, r, tmp, ret):
    #print target, tmp, arr
    if r == 0:
        if target == 0:
            ret[tuple(tmp)] = True
    
    for i in xrange(start, len(arr)):
        if i - 1 > start and arr[i - 1] == arr[i]:
            continue
        if arr[i] > target:
            break
        elif arr[i] <= target:
            tmp.append(arr[i])
            findcomb(arr, i + 1, target - arr[i], r - 1, tmp, ret)
            tmp.pop()
            
def ans2(arr, target):
    ret = {}
    arr.sort()
    for i in xrange(1, len(arr) + 1):
        tmp = []
        findcomb(arr, 0, target, i, tmp, ret)
    return [ list(x) for x in ret.keys()]

class Solution(object):
    def combinationSum2(self, arr, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        return ans2(arr, target)
