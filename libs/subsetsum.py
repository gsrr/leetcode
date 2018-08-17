#code

import collections

def ans(arr, tval):
    dp = collections.defaultdict(int)
    dp[0] = 0
    arr.sort()
    for i in range(len(arr)):
        keys = list(dp.keys())
        for key in keys:
            nkey = arr[i] + key
            if nkey > tval:
                continue
            
            if nkey == tval:
                return "YES"
                
            dp[nkey] += 1
    
    return "NO"

'''
Given a numeric array and a target value, make sure the target value is equal to sum of subset,
which extracted from the numeric array.
'''
def ans1(arr,  tval):
    dp = [0] * (tval + 1)
    dp[0] = 1
    arr.sort()
    for i in range(len(arr)):
        for j in range(len(dp) - 1, -1, -1):
            if dp[j] == 0:
                continue
            
            if arr[i] + j >= len(dp):
                continue
            
            if arr[i] + j == tval:
                return "YES"
                
            dp[arr[i] + j] = 1

    return "NO"
    
t = int(input())
for _ in range(t):
    n = int(input())
    arr = list(map(int, input().strip().split()))
    sval = sum(arr)
    if sval % 2 != 0:
        print("NO")
    else:
        tval = sval // 2
        print(ans1(arr, tval))
