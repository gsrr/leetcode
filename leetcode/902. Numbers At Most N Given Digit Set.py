def recur_util(val, arr, M):
    cnt = 0
    if val <= M:
        cnt += 1
    else:
        return 0
    
    for i in xrange(len(arr)):
        val = val * 10 + int(arr[i])
        cnt += recur_util(val, arr, M)
        val = val // 10
    return cnt
    
def ans(arr, M):
    cnt = 0
    for i in xrange(len(arr)):
        cnt += recur_util(int(arr[i]), arr, M)
    return cnt
    
def get_cnt(arr, M, val, i):
    M_str = str(M)
    mdig = int(M_str[::-1][i - 1])
    #print "val:%d, mdig:%d, i:%d"%(val, mdig, i)
    if val < mdig:
        return pow(len(arr), i - 1)
    if val > mdig:
        return 0
    
    if i == 1:
        return 1
    
    cnt = 0
    for j in xrange(len(arr)):
        tcnt = get_cnt(arr, M, int(arr[j]), i - 1)
        #print "sub", arr[j], i, tcnt
        cnt += tcnt
    return cnt
    
def ans1(arr, M):
    digs = len(str(M))
    cnt = 0
    for i in xrange(digs):
        for j in xrange(len(arr)):
            tcnt = 0
            if i + 1 < digs:
                tcnt = pow(len(arr), i)
            elif i + 1 > digs:
                tcnt = 0
            else:    
                tcnt = get_cnt(arr, M, int(arr[j]), i + 1)
            #print arr[j], i + 1, tcnt
            cnt += tcnt
    return cnt

class Solution(object):
    def atMostNGivenDigitSet(self, D, N):
        """
        :type D: List[str]
        :type N: int
        :rtype: int
        """
        return ans1(D, N)
        
