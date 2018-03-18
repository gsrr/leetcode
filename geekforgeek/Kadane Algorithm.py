#code
def max_sum_subarray(nums):
    if len(nums) == 0:
        return 0
    maxsum = nums[0]
    tsum = 0
    for n in nums:
        tsum += n
        if tsum > maxsum:
            maxsum = tsum
        if tsum < 0:
            tsum = 0
    print (maxsum)

def ans1(A):
    '''
    Result : Time expired
    '''
    maxsum = 0
    for i in range(len(A)):
        tsum = 0
        for j in range(i, len(A)):
            tsum += A[i]
            if tsum > maxsum:
                maxsum = tsum
    return maxsum

def ans2(A):
    '''
    Result : Time expired
    '''
    maxsum = 0
    for i in range(len(A)):
        tsum = 0
        for j in range(i, -1, -1):
            tsum += A[i]
            if tsum > maxsum:
                maxsum = tsum
    return maxsum

def ans3(A):
    maxsum = A[0]
    tsum = A[0]
    for i in range(1, len(A)):
        if A[i] > A[i] + tsum: #若tsum為負
            tsum = A[i]
        else:
            tsum = A[i] + tsum #若tsum > 0
        maxsum = max(tsum, maxsum)
    return maxsum
    
def ans4(A):
    maxsum = A[0]
    tsum = A[0]
    for i in range(1, len(A)):
        if tsum < 0:
            tsum = A[i]
        else:
            tsum += A[i]
        maxsum = max(tsum, maxsum)
    return maxsum
    
def ans5(A):
    maxsum = A[0]
    tsum = A[0]
    for i in range(1, len(A)):
        tsum = A[i] if tsum < 0 else tsum + A[i]
        maxsum = max(tsum, maxsum)
    return maxsum

t = int(input())
for i in range(t):
    n = int(input())
    nums = list(map(int, input().split()))
    #print (n, nums)
    #max_sum_subarray(nums)
    print (ans5(nums))
