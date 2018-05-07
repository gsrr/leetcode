def ans1(N):
    if N == 1:
        return 1
    end = N // 2
    if N % 2 != 0:
        end += 1
    
    cnt = 0
    i = end
    j = end
    tsum = 0
    while i > 0:
        tsum += i
        if tsum >= N:
            if tsum == N:
                cnt += 1
            tsum -= j
            j -= 1
        i -= 1
 
    return cnt + 1

def ans2(N):
    cnt = 1
    i = 2
    isum = 1 + 2
    while isum <= N:
        if (N - isum) % i == 0:
            cnt += 1
        i += 1
        isum += i
    return cnt

class Solution(object):
    def consecutiveNumbersSum(self, N):
        """
        :type N: int
        :rtype: int
        """
        return ans2(N)        

cases = [
    5,
    9,
    15,
]

for i in xrange(len(cases)):
    print ans1(cases[i])
