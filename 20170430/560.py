def subarraySum(nums, k):
    print nums
    d = {0: 1}

    res = 0
    s = 0
    for num in nums:
        s += num
        delta = s - k
        res += d.get(delta, 0)
        print "num=%d, s=%d, delta=%d, res=%d"%(num, s, delta, res)
        d[s] = d.get(s, 0) + 1
    return res

nums = [2, -1, 2, 1]
print subarraySum(nums, 1)
