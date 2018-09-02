import collections

def ans(arr):
    dic = collections.defaultdict(int)
    for i in xrange(len(arr)):
        dic[arr[i]] += 1
        bi = arr[i]
        for j in xrange(i + 1, len(arr)):
            bi = bi | arr[j]
            dic[bi] += 1
    return len(dic.keys())
            
def ans1(arr):
    dic = collections.defaultdict(int)
    for i in xrange(len(arr)):
        dic[arr[i]] += 1
        bi = 0
        for j in xrange(i + 1, len(arr)):
            if bi & arr[i] == arr[i]:
                break
            bi = bi | arr[j]
            dic[bi | arr[i]] += 1
    return len(dic.keys())

class Solution(object):
    def subarrayBitwiseORs(self, A):
        """
        :type A: List[int]
        :rtype: int
        """
        #return ans(A)
        return ans1(A)
        
