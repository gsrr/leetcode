#code
import collections

def ans2(arr):
    #print (arr)
    summ = sum(arr)
    if summ % 2 != 0:
        return "NO"
    mid = summ / 2
    dp = collections.defaultdict(int)
    dp[0] = 1
    for i in range(len(arr)):
        keys = list(dp.keys())
        for k in keys:
            if arr[i] + k == mid:
                return "YES"
            dp[arr[i] + k] += 1
    return "NO"

def bfs(arr):
    '''
    DP method
    Result : Time expired
    '''
    summ = sum(arr)
    if summ % 2 != 0:
        return "NO"
    arr.sort()
    mid = summ // 2
    dp = [0] * (summ + 1)
    dp[0] = 1
    for i in range(mid):
        if dp[i] != 0:
            for j in range(len(arr)):
                if i + arr[j] > mid:
                    break
                if i + arr[j] == mid:
                    return "YES"
                dp[i + arr[j]] += dp[i]
    return "NO"

from collections import deque

def ans_bfs(arr):
    '''
    bfs method
    '''
    summ = sum(arr)
    if summ % 2 != 0:
        return "NO"
    mid = summ // 2
    #q= deque([(0, 0)]) # (val, index)
    q= [(0, 0)] # (val, index)
    hist = {}
    while len(q) != 0:
        #val, index = q.popleft()
        val, index = q.pop(0)
        if val == mid:
            return "YES"
        hist[val] = True
        for i in range(index, len(arr)):
            if val + arr[i] in hist:
                continue
            if val + arr[i] > mid:
                continue
            q.append((val + arr[i], i + 1))
    return "NO"

def dfs(arr, mid):
    if mid == 0:
        return 1
    
    if mid < 0:
        return 0
        
    ret = 0
    for i in range(len(arr)):
        ret += dfs(arr[i + 1:], mid - arr[i])
        if ret > 0:
            return ret
    return ret
    
def ans(arr):
    '''
    dfs method
    '''
    summ = sum(arr)
    if summ % 2 != 0:
        return "NO"
    mid = summ // 2
    ret = 0
    for i in range(len(arr)):
        ret += dfs(arr[i + 1:], mid - arr[i])
        if ret > 0:
            return "YES"
    return "NO"

t = int(input())
for i in range(t):
    n = int(input())
    arr = list(map(int, input().split()))
    print (ans_bfs(arr))
    
