#code
def max_sum_subarray(nums):
    maxsum = -0x7ffffff
    tsum = 0
    for n in nums:
        tsum += n
        if tsum > maxsum:
            maxsum = tsum
        if tsum < 0:
            tsum = 0
    print (maxsum)

t = int(input())
for i in range(t):
    n = int(input())
    nums = list(map(int, input().split()))
    #print (n, nums)
    max_sum_subarray(nums)
