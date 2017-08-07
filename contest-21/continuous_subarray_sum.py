def checkSubarraySum(nums, k):
    for i in xrange(len(arr)):
        s = arr[i]
        for j in xrange(i + 1, len(arr)):
            s += arr[j]
        if s % k == 0:
            return True
    return False      


k = 6
arr = [23, 2, 4, 6, 7]
print checkSubarraySum(arr, k)
print 123



