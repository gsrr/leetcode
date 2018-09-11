def set_allsum1(arr):
    sarr = [0]
    for i in xrange(len(arr)):
        for j in xrange(len(sarr)):
            sarr.append(arr[i] + sarr[j])
    return sarr

def set_allsum2(arr):
    r = (1 << len(arr))
    sarr = [0] * r
    for v in xrange(1, len(sarr)):
        tv = v
        i = 0
        while tv != 0:
            if tv & 1 != 0:
                sarr[v] += arr[i]
            i += 1
            tv >>= 1
    return sarr

def set_allsum3(arr):
    r = (1 << len(arr))
    sarr = [0] * r
    for v in xrange(1, r):
        tv = v
        i = 0
        while True:
            if tv & (1 << i) != 0:
                break
            i += 1
        sarr[v] = sarr[v & v - 1] + arr[i]
    return sarr

def set_allsum3_2(arr):
    r = (1 << len(arr))
    sarr = [0] * r
    for v in xrange(1, r):
        tv = v
        i = 0
        while tv & (1 << i) == 0:
            i += 1
        sarr[v] = sarr[v & v - 1] + arr[i]
    return sarr
    
def set_allsum4(arr):
    r = (1 << len(arr))
    sarr = [0] * r
    i = 1
    for v in arr:
        for j in xrange(i, i * 2):
            sarr[j] = sarr[j - i] + v
        i *= 2
    return sarr

def set_allsum5(arr):
    import collections
    dp = collections.defaultdict(int)
    dp[0] = 0
    for v in arr:
        keys = list(dp.keys())
        for key in keys:
            dp[v + key] += 1
    return dp

arr = [1, 1, 1]
sarr = [0, 1, 1, 2, 1, 2, 2, 3]
print "input : %s, output : %s"%(arr, sarr)
print set_allsum1(arr)
print set_allsum2(arr)
print set_allsum3(arr)
print set_allsum3_2(arr)
print set_allsum4(arr)
print set_allsum5(arr)
