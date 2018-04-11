def recur_util(A, K, curr_sum):
    if len(A) <= K:
        return curr_sum + sum(A)
    
    if K == 1:
        return curr_sum + sum(A)/float(len(A)) 
    
    max_sum = 0
    tmp_sum = 0
    for i in xrange(len(A)):
        tmp_sum += A[i]
        max_sum = max(max_sum, recur_util(A[i + 1:], K - 1, curr_sum + tmp_sum / float(i + 1)))
    return max_sum

def ans1(A, K):
    '''
    Method : Recursive
    Time complexity : n * (n - 1) * ... * (n - k) --> how many times you should lookup the element of the array.
    Space complexity : O(k) --> stack of function call
    '''
    if len(A) <= K:
        return sum(A)
    
    if K == 1:
        return sum(A)/float(len(A))
    
    max_sum = 0
    summ = 0
    for i in xrange(len(A)):
        summ += A[i]
        max_sum = max(max_sum, recur_util(A[i + 1:], K - 1, summ / float(i + 1)))
    return max_sum

def ans2(A, K):
    '''
    Method : Greedy + Dynamic programming
    Result : Wrong answer, it can not be solved by greedy method.
    Time complexity : O(k * n)
    Space complexity : O(1)
    '''
    if K >= len(A):
        return sum(A)
    
    if K == 1:
        return sum(A)/float(len(A))
    
    dp = {(0, len(A)) : sum(A)/float(len(A))}
    while len(dp.keys()) < K:
        print dp
        tdp = {}
        tsum = (0, 0)
        idx = [(0, 0), 0]
        for key in dp.keys():
            s = key[0]
            e = key[1]
            for i in xrange(s + 1, e):
                lsum = sum(A[s:i]) / float(len(A[s:i]))
                rsum = sum(A[i:e]) / float(len(A[i:e]))
                print "s = %d, mid = %d, e = %d, lsum = %f, rsum = %f"%(s, i, e, lsum, rsum)
                if lsum + rsum > (tsum[0] + tsum[1]):
                    tsum = (lsum, rsum)
                    idx = [(s, e), i]
            tdp[(s, e)] = dp[(s, e)]
        del tdp[idx[0]]
        tdp[(idx[0][0], idx[1])] = tsum[0]
        tdp[(idx[1], idx[0][1])] = tsum[1]
        dp = tdp
    print dp
    summ = 0
    for key in dp.keys():
        summ += dp[key]
    return summ


def recur_util3(hist, A, K, curr_sum):
    if len(A) <= K:
        return curr_sum + sum(A)
    
    if K == 1:
        return curr_sum + sum(A)/float(len(A)) 
    
    if hist.has_key((len(A), K)) == True:
        return curr_sum + hist[(len(A), K)]
    max_sum = 0
    tmp_sum = 0
    for i in xrange(len(A)):
        tmp_sum += A[i]
        max_sum = max(max_sum, recur_util(hist, A[i + 1:], K - 1, tmp_sum / float(i + 1)))
    hist[(len(A), K)] = max_sum
    return curr_sum + max_sum

def ans3(A, K):
    '''
    Method : Recursive with cache
    Result : Accept
    Time complexity : 
    Space complexity : O(K * N) and function stack : O(n)
    '''
    if len(A) <= K:
        return sum(A)
    
    if K == 1:
        return sum(A)/float(len(A))
    
    hist = {}
    max_sum = 0
    summ = 0
    for i in xrange(len(A)):
        summ += A[i]
        max_sum = max(max_sum, recur_util(hist, A[i + 1:], K - 1, summ / float(i + 1)))
        #print hist
    return max_sum    


class Solution(object):
    def largestSumOfAverages(self, A, K):
        """
        :type A: List[int]
        :type K: int
        :rtype: float
        """
        #return ans1(A, K)
        #return ans2(A, K)
        return ans3(A, K)
