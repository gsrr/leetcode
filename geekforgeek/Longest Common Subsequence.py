#code
def ans1(str1, str2):
    if len(str1) == 0 or len(str2) == 0:
        return 0
    
    if str1[-1] == str2[-1]:
        return 1 + ans(str1[0:len(str1) - 1], str2[0:len(str2) - 1])
    else:
        return max(ans(str1[0:len(str1) - 1], str2), ans(str1, str2[0:len(str2) - 1]))

def ans2(str1, str2):
    dp = [[0] * (len(str2) + 1) for _ in range(len(str1) + 1)]
    for i in range(1, len(dp)):
        for j in range(1, len(dp[i])):
            if str1[i - 1] == str2[j - 1]:
                dp[i][j] = dp[i - 1][j - 1] + 1
            else:
                dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])
    #print (dp)
    return dp[-1][-1]
    
t = int(input())
for i in range(t):
    len1, len2 = list(map(int, input().split()))
    str1 = input()
    str2 = input()
    #print (ans1(str1, str2))
    print (ans2(str1, str2))
