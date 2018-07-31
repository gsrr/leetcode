#code

import bisect

def ans(arr):
    if len(arr) == 0:
        return 0
        
    dp = [arr[0]]
    for i in range(1, len(arr)):
        pos = bisect.bisect_right(dp, arr[i])
        #print (arr[i], pos, dp)
        if arr[i] == dp[pos - 1]:
            continue
        if pos == len(dp):
            dp.append(arr[i])
            continue
        dp[pos] = arr[i]
    #print(dp)
    return len(dp)
    
if __name__ == "__main__":
    t = int(input())
    for i in range(t):
        n = int(input())
        arr = list(map(int, input().strip().split()))
        print (ans(arr))
