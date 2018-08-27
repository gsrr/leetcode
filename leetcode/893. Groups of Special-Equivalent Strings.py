import collections

def is_same(arr1, arr2):
    dic11 = collections.defaultdict(int)
    dic12 = collections.defaultdict(int)
    dic21 = collections.defaultdict(int)
    dic22 = collections.defaultdict(int)
    i = 0
    while i < len(arr1):
        dic11[arr1[i]] += 1
        i += 2
    i = 0
    while i < len(arr2):
        dic21[arr2[i]] += 1
        i += 2
    if dic11 != dic21:
        return False
    
    i = 1
    while i < len(arr1):
        dic12[arr1[i]] += 1
        i += 2
    i = 1
    while i < len(arr2):
        dic22[arr2[i]] += 1
        i += 2
    if dic12 != dic22:
        return False
    return True
        
def get_arr2(arr):
    arr2 = []
    for i in xrange(len(arr)):
        dic1 = collections.defaultdict(int)
        dic2 = collections.defaultdict(int)
        j = 0
        while j < len(arr[i]):
            dic1[arr[i][j]] += 1
            j += 2
            
        j = 1
        while j < len(arr[i]):
            dic2[arr[i][j]] += 1
            j += 2
        arr2.append([dic1, dic2])
    return arr2    

def is_same2(arr1, arr2):
    if arr1[0] != arr2[0]:
        return False
    if arr1[1] != arr2[1]:
        return False
    return True

def ans(arr):
    arr2 = get_arr2(arr)
    #print arr2
    ret = [-1] * len(arr)
    for i in xrange(len(arr)):
        if ret[i] != -1:
            continue
        for j in xrange(i + 1, len(arr)):
            if is_same2(arr2[i], arr2[j]):
                ret[j] = i
    
    cnt = 0
    for i in xrange(len(ret)):
        if ret[i] == -1:
            cnt += 1
    return cnt
    
    
class Solution(object):
    def numSpecialEquivGroups(self, A):
        """
        :type A: List[str]
        :rtype: int
        """
        return ans(A)
        
