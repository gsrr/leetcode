#code
def recur_util(arr, sarr, s1):
    mid = sarr / 2
    if s1 >= mid:
        return s1 - (sarr - s1)
    
    ss1 = 0
    diff = 0x7fffffff
    for i in range(len(arr)):
        diff = min(diff, recur_util(arr[i + 1:], sarr, s1 + arr[i]))
    return diff
    
def ans_recur(arr):
    '''
    Time complexity : O(n * (n - 1) * ... (n - k + 1))
    '''
    if len(arr) == 1:
        return 0
    if len(arr) == 2:
        return abs(arr[0] - arr[1])
    
    k = len(arr) // 2
    if len(arr) % 2 != 0:
        k += 1
        
    sarr = sum(arr)
    s1 = 0
    diff = 0x7fffffff
    for i in range(k):
        diff = min(diff, recur_util(arr[i + 1:], sarr, arr[i]))
    return diff
    
import collections

def ans(arr):
    if len(arr) == 1:
        return 0
    if len(arr) == 2:
        return abs(arr[0] - arr[1])
    
    sarr = sum(arr)
    mid = sum(arr) // 2
    arr.sort()
    dp = collections.defaultdict(int)
    dp[0] = 1
    v1 = 0
    diff = mid - v1
    for i in range(len(arr)):
        keys = list(dp.keys())
        for key in keys:
            tmp = key + arr[i]
            if tmp > mid:
                continue
            dp[tmp] += 1
            if mid - tmp < diff:
                v1 = tmp
                diff = mid - v1
    #print (v1, mid, (sarr - v1))
    return (sarr - v1) - v1
    
t = int(input())
for i in range(t):
    n = int(input())
    arr = list(map(int, input().split()))
    print (ans(arr))
