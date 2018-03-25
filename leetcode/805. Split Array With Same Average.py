
def ans1(arr, cnt, tval):
    #print avg
    dp = {}
    dp[(0, 0)] = True #[sum, num]
    for i in xrange(len(arr)):
        keys = list(dp.keys())
        for k in keys:
            summ, num = k[0], k[1]
            summ += arr[i]
            num += 1
            if num > cnt:
                continue
            if num == cnt:
                if summ == tval:
                    return True
            if summ <= tval:
                dp[(summ, num)] = True
    return False

def pre_ans1(A):
    A.sort()
    s = sum(A)
    ave = s/float(len(A))
    res = []
    for i in range(1, len(A)//2+1):
        s1 = ave * i
        if s1-int(s1)<0.0000001:
            res.append([i,int(s1)])
    for c, s in res: # count, summ
        if ans1(A, c, s): return True   
    return False
    
def ans2(A):
    s = sum(A)
    ave = s/float(len(A))
    res = []
    for i in range(1, len(A)//2+1):
        s1 = ave * i
        if s1-int(s1)<0.0000001:
            res.append([i,int(s1)])
    
    print res
    
    def dfs(i,cnt,t):
        if cnt == 0 and t == 0: 
            return True
        
        if cnt == 0 or t < 0: 
            return False
        
        if i == len(A): # no element has been choosed.
            return False
        
        if dfs(i + 1, cnt, t): # do not select this element 
            return True
        
        if dfs(i + 1, cnt - 1, t - A[i]): # select this element
            return True

    for c, s in res: # count, summ
        if dfs(0, c, s): return True   
    return False
        

class Solution(object):
    def splitArraySameAverage(self, A):
        """
        :type A: List[int]
        :rtype: bool
        """
        
        return pre_ans1(A)
        
