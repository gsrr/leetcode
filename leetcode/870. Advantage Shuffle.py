import collections

def ans(arr, brr):
    posb = collections.defaultdict(list)
    for i in xrange(len(brr)):
        posb[brr[i]].append(i)
        
    arr.sort()
    brr.sort()
    cnt = 0
    j = 0
    k = len(brr) - 1
    tret = []
    for i in xrange(len(arr)):
        if arr[i] > brr[j]:
            tret.append([arr[i], brr[j]])
            cnt += 1
            j += 1
        else:
            tret.append([arr[i], brr[k]])
            k -= 1
    
    
    #print cnt, tret
    
    ret = [0] * len(arr)
    for i in xrange(len(tret)):
        #print tret[i]
        ret[posb[tret[i][1]].pop()] = tret[i][0]
    return ret
            

class Solution(object):
    def advantageCount(self, A, B):
        """
        :type A: List[int]
        :type B: List[int]
        :rtype: List[int]
        """
        return ans(A, B)
